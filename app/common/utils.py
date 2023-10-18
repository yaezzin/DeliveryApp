import uuid
import boto3

from django.contrib.auth.mixins import UserPassesTestMixin
from django.conf import settings
from django.core.files import File
from django.shortcuts import redirect
from django.http import JsonResponse


class GroupRequiredMixin(UserPassesTestMixin):
    group_name = None

    def test_func(self):
        return self.request.user.groups.filter(name=self.group_name).exists()

    def handle_no_permission(self):
        for group in self.request.user.groups.all():
            if self.request.user.groups.filter(name=group.name).exists():
                return redirect(f"/{group.name}/home")

        return redirect("/")


class CustomerRequiredMixin(GroupRequiredMixin):
    group_name = "customer"


class SajjangRequiredMixin(GroupRequiredMixin):
    group_name = "sajjang"


class DeliveryCrewRequiredMixin(GroupRequiredMixin):
    group_name = "delivery_crew"


def image_handler(request, exsiting_post=None):
    image_url = exsiting_post if exsiting_post else None

    try:
        if request.FILES.get("store_pic"):
            folder_name = "sajjang_store"
            image = request.FILES.get("store_pic")
        elif request.FILES.get("menu_pic"):
            print(request.FILES.get("menu_pic"))
            folder_name = "sajjang_menu"
            image = request.FILES.get("menu_pic")
        else:
            print("FILES.get ?, neither store_pic nor menu_pic")
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e)}, status=400)

    if image:
        image: File
        endpoint_url = settings.IMAGE_BUCKET_ENDPOINT
        access_key = settings.NCP_ACCESS_KEY
        secret_key = settings.NCP_SECRET_KEY
        buket_name = "del-app-mh"

        s3 = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )
        image_id = str(uuid.uuid4())

        # split 이후 마지막 값 가져오기 (jpg, png, gif 등등)
        file_extension = image.name.split(".")[-1]
        image_name = f"{image_id}.{file_extension}"
        s3_key = f"{folder_name}/{image_name}"

        try:
            s3.upload_fileobj(image.file, buket_name, s3_key)
            s3.put_object_acl(ACL="public-read", Bucket=buket_name, Key=s3_key)
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=400)

        image_url = f"{endpoint_url}/{buket_name}/{s3_key}"
        print("image_url out:", image_url)

    return image_url
