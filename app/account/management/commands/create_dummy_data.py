import csv

from django.contrib.auth.models import User, Group
from django.utils import timezone

from account.models import Address
from customer.models import Cart

# from delivery_crew.models import DeliveryLocation
from sajjang.models import Category, Stores, Menus, Order
from delivery_crew.models import DeliveryLocation

from random import randint, choice, random, sample
from faker import Faker

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Creating dummy data"
    fake = Faker("ko_KR")

    def handle(self, *args, **options):
        print("더미 데이터 생성을 시작합니다.")

        addresses = []
        with open("./account/management/store_data.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                addresses.append(row[2])

        def get_random_address(addresses):
            from_selected_address = choice(addresses)
            addresses.remove(from_selected_address)
            return from_selected_address

        def get_two_location_address(addresses):
            two_locaton_address = []

            for address in addresses:
                if "서울특별시 서초구" in address:
                    addresses.remove(address)
                    two_locaton_address.append(address)
                    break

            for address in addresses:
                if "서울특별시 종로구" in address:
                    addresses.remove(address)
                    two_locaton_address.append(address)
                    break

            return two_locaton_address

        fake = self.fake
        group_names = ["customer", "sajjang", "delivery_crew"]

        # Group 생성
        for name in group_names:
            group = Group.objects.create(name=name)

        groups = Group.objects.all()

        # test 용 유저 생성
        for group in groups:
            test_user = User.objects.create_user(
                username=f"test_{group.name}", password="1234"
            )
            test_user.groups.add(group)

        def generate_unique_username():
            while True:
                generated_username = fake.user_name()
                if not User.objects.filter(username=generated_username).exists():
                    return generated_username

        def create_users(group, num_users):
            for _ in range(num_users):
                unique_username = generate_unique_username()
                user = User.objects.create_user(
                    username=unique_username, password="1234"
                )
                user.groups.add(group)

        # 그룹 별 랜덤 유저 30개씩 생성
        for group in groups:
            create_users(group, 30)

        customer_users = User.objects.filter(groups__name="customer")
        sajjang_users = User.objects.filter(groups__name="sajjang")
        delivery_crew_users = User.objects.filter(groups__name="delivery_crew")

        # 고객 유저 주소 3개씩 생성 하나는 default 주소
        for user in customer_users:
            # default = False
            for _ in range(2):
                from_selected_address = get_random_address(addresses)

                Address.objects.create(
                    customer_id=user,
                    address_name=fake.user_name(),
                    address=from_selected_address,
                    is_default=False,
                    created_at=timezone.now(),
                )

            # default = True
            from_selected_address = get_random_address(addresses)
            Address.objects.create(
                customer_id=user,
                address_name=fake.user_name(),
                address=from_selected_address,
                is_default=True,
                created_at=timezone.now(),
            )

        for user in delivery_crew_users:
            from_selected_address = get_two_location_address(addresses)
            active_area_list = ["서울특별시 서초구", "서울특별시 종로구"]
            active_area_list = choice([True, False])

            DeliveryLocation.objects.create(
                user_id=user,
                active_area=active_area_list,
                address=from_selected_address[0],
            )

            DeliveryLocation.objects.create(
                user_id=user,
                active_area=not active_area_list,
                address=from_selected_address[1],
            )

        categories = ["Pizza", "Burger", "Chicken", "Korean", "Japanese", "Indian"]

        # 카테고리 생성
        for category in categories:
            Category.objects.create(name=category)

        category_objects = Category.objects.all()

        # 사장 유저 스토어 3개씩 생성
        for user in sajjang_users:
            for _ in range(2):
                from_selected_address = get_random_address(addresses)
                Stores.objects.create(
                    user_id=user,
                    name=fake.company(),
                    address=from_selected_address,
                    store_pic=fake.image_url(),
                    category_id=choice(category_objects),
                    status=choice([True, False]),
                    created_at=timezone.now(),
                )

        store_objects = Stores.objects.all()

        menu_names = [
            "Apple Pie",
            "Beef Stew",
            "Caesar Salad",
            "Dumplings",
            "Eggs Benedict",
            "Fajitas",
            "Grilled Cheese",
            "Hot Dogs",
            "Ice Cream",
            "Jambalaya",
            "Kebabs",
            "Lasagna",
            "Miso Soup",
            "Nachos",
            "Omelette",
            "Pancakes",
            "Quiche",
            "Ramen",
            "Sushi",
            "Tacos",
            "Udon",
            "Vegetable Curry",
            "Waffles",
            "Xiao Long Bao",
            "Yogurt",
            "Zucchini Bread",
            "Burrito",
            "Chicken Parmesan",
            "Donuts",
            "Fish and Chips",
            "Guacamole",
            "Hummus",
            "Italian Sub",
            "Jelly",
            "Katsu Curry",
            "Lobster Roll",
            "Mac and Cheese",
            "Noodles",
            "Onion Rings",
            "Pizza",
        ]

        # 스토어당 10개의 메뉴 생성
        for store in store_objects:
            for _ in range(10):
                random_price = randint(4000, 30000)
                rounded_price = (random_price // 100) * 100

                Menus.objects.create(
                    store_id=store,
                    category_id=choice(category_objects),
                    name=choice(menu_names),
                    unit_price=rounded_price,
                    menu_pic=fake.image_url(),
                    is_available=True,
                    created_at=timezone.now(),
                )

        # 고객 유저의 카트 생성
        for user in customer_users:
            selected_store = choice(store_objects)
            store_menus = Menus.objects.filter(store_id=selected_store)

            for _ in range(randint(1, 10)):
                store_menus_list = list(store_menus)

                selected_menus = (
                    sample(store_menus_list, 3)
                    if len(store_menus_list) >= 3
                    else store_menus_list
                )

                for selected_menu in selected_menus:
                    Cart.objects.create(
                        user_id=user,
                        store_id=selected_store,
                        menu_id=selected_menu,
                        order_id=None,
                        quantity=randint(1, 10),
                        created_at=timezone.now(),
                    )

        # 유저의 카트 정보를 기반으로 오더 생성
        for user in customer_users:
            selected_user_cart = Cart.objects.filter(user_id=user, order_id=None)

            # 하나의 스토어 정보로 오더를 생성할 카트 설정
            if selected_user_cart.exists():
                selected_store = selected_user_cart.first().store_id
                selected_address = choice(Address.objects.filter(customer_id=user))
                total_price = 0

                # 샘플링으로 오더에 담을 카트정보 선택
                cart_list = list(selected_user_cart)
                cart_for_order = sample(cart_list, min(3, len(cart_list)))

                # 샘플링으로 선택된 카트 정보의 메뉴 정보로 총 가격 뽑아내기
                for cart in cart_for_order:
                    menu_price = Menus.objects.get(id=cart.menu_id.id).unit_price
                    total_price += menu_price * cart.quantity

                # 오더 생성
                order = Order.objects.create(
                    user_id=user,
                    store_id=selected_store,
                    address_id=selected_address,
                    total_price=total_price,
                    receipt=None,
                    created_at=timezone.now(),
                )

                # 만들어진 오더의 정보를 카트 정보에 업데이트
                for cart in cart_for_order:
                    cart.order_id = order
                    cart.save()

        order_objects = Order.objects.all()

        # 결제될 확률
        def simple_payment(success_rate):
            return random() < success_rate

        # 결제 과정을 거쳐서 오더의 정보를 업데이트
        for order in order_objects:
            payment_success = simple_payment(0.95)

            try:
                if payment_success:
                    order.order_status = "paid"
                    order.receipt = fake.uuid4()
            except Exception as e:
                print(f"Payment failed: {e}")

            order.save()

        order_objects = Order.objects.all()

        # 사장이 수락할 확률
        def sajjang_acceptance(success_rate):
            return random() < success_rate

        for order in order_objects:
            sajjang_acceptance_success = sajjang_acceptance(0.80)

            if sajjang_acceptance_success:
                order.order_status = "sajjang_accepted"
            else:
                order.order_status = "sajjang_rejected"

            order.save()
