from django.contrib.auth.models import Group

# Create your models here.


def create_group(group_name):
    try:
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            return f"그룹 '{group_name}'이 생성되었습니다."
        else:
            return f"그룹 '{group_name}'은 이미 존재합니다."
    except Exception as e:
        return f"그룹 생성 중 오류 발생: {str(e)}"
