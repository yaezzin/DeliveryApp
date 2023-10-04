from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group

# ContentType을 가져옵니다.
content_type = ContentType.objects.get_for_model(Group)

# "그룹A 페이지 접근 권한" 퍼미션 생성
permission_customer, created = Permission.objects.get_or_create(
    codename='access_customer_page',
    name='Can access customer Group Page',
    content_type=content_type,
)
group, created = Group.objects.get_or_create(name='customer')
group.permissions.add(permission_customer)

# "그룹B 페이지 접근 권한" 퍼미션 생성
permission_sajjang, created = Permission.objects.get_or_create(
    codename='access_sajjang_page',
    name='Can access sajjang Group Page',
    content_type=content_type,
)
group, created = Group.objects.get_or_create(name='sajjang')
group.permissions.add(permission_sajjang)

permission_delivery_crew, created = Permission.objects.get_or_create(
    codename='access_delivery_crew_page',
    name='Can access delivery_crew Group Page',
    content_type=content_type,
)
group, created = Group.objects.get_or_create(name='delivery_crew')
group.permissions.add(permission_delivery_crew)