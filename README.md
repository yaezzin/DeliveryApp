# 3-way Communication

(대표 이미지 or 로고) - 한솔님

![Badge](https://img.shields.io/badge/version-1.1.1-orange.svg)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Flikelion-backend-6th%2Fdelivery_app&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## Project Detail

주문, 오더를 중심으로 고객, 사장, 배달크루 이렇게 3개의 주체가 같은 정보를 바라보며 움직여야 합니다. 고객의 요구사항을 정확히 파악해서 전달하고 각 파트에서 담당한 일들이 처리되는 과정들의 진행상황을 공유하여 발생한 이벤트에 대한 같은 정보를 인지할 수 있게 합니다.

#### 기간 : 2023.09.24 - 2023.10.24

#### 배포 주소 : - 예진

## Team

#### 김민혁 - [민혁's task list](https://fire-apartment-b43.notion.site/8657cd5eb06247d9b3d30b6e5f233d77?v=3cdeb751b90d4de0affbf249d3ffd771&pvs=4)

- Terraform - IaC NCP kubernetest cluster
- Helm - helpers, Deployment, SVC, PVC, Configmap, Secret
- Helm - Seal Secret, Horizontal Pod Autoscaler
- Argo CD - CD (Automate sync, ref github repo)
- Backend - sajjang function(urls, views, templates)
- Backend - delivery_crew function(urls, views, templates)
- Dev env - Dummy data creation command
- Dev env - Mixin (permission check for each Group)

#### 전예진

#### 문건우 - [건우's task list](https://www.notion.so/bc23e3c6244e4862aa0d123ccb10288b?v=566d2a8680ce471c9d3a32b56e815d9e)

- Backend - customer function(views, templates)
- Backend - sajjang function(views, templates)
- Backend - delivery crew function(urls, views, templates)
- Frontend - account, customer, sajjang, delivery crew(Bootstrap)

#### 이한솔

#### 정해민

#### 한승훈 - [승훈's task list](https://fire-apartment-b43.notion.site/260896c24f46404da53f49b728bdaba0?v=04f0c5a217a14c1595b5598704d9b42c&pvs=4)

- Order 기능 모델링
- Cart, Menu 모델 구현
- customer basic template & cancel function 구현

## Tech Stack

#### Frontend - 건우

#### Backend - 해민

#### Infra - 예진

## Requirements - 한솔

- aa
- bb
- cc

## ERD - 해민

## API statements

<details>
<summary>Account</summary>
<div markdown="1">

| Method | URL             | Description   |
| ------ | --------------- | ------------- |
| GET    | /               | 홈 화면       |
| POST   | /account/signin | 로그인        |
| GET    | /account/signup | 회원가입 화면 |
| POST   | /account/signup | 회원가입      |
| POST   | /logout         | 로그아웃      |

</div>
</details>

<details>
<summary>Customer</summary>
<div markdown="1">

| Method | URL                                                     | Description                   |
| ------ | ------------------------------------------------------- | ----------------------------- |
| GET    | /customer/home                                          | customer 홈페이지             |
| GET    | /customer/address                                       | 주소 조회 페이지              |
| GET    | /customer/address/add                                   | 주소 추가 페이지              |
| POST   | /customer/address/add                                   | 주소 추가                     |
| GET    | /customer/address/<<int:address_id>>                    | 주소 상세 페이지              |
| GET    | /customer/address/<<int:address_id>>/edit               | 주소 수정 페이지              |
| POST   | /customer/address/<<int:address_id>>/edit               | 주소 수정                     |
| POST   | /customer/address/<<int:address_id>>/delete             | 주소 삭제                     |
| GET    | /customer/store/<<int:stores_id>>                       | 가게 상세보기                 |
| GET    | /customer/store/<<int:stores_id>>/menu                  | 가게 메뉴 리스트 보기         |
| GET    | /customer/store/<<int:stores_id>>/menu/<<int:menus_id>> | 가게 메뉴 상세 보기           |
| POST   | /customer/store/<<int:stores_id>>/menu/<<int:menus_id>> | 장바구니 추가                 |
| GET    | /customer/cart                                          | 고객의 장바구니 조회          |
| GET    | /customer/orders                                        | 유저의 주문 내역 리스트 조회  |
| GET    | /customer/order/<<int:order_id>>                        | 주문 내역 상세보기            |
| GET    | /customer/order/create/<<int:store_id>>                 | 주문서 작성 결과 보기         |
| POST   | /customer/order/create/<<int:store_id>>                 | 주문 항목 수정                |
| POST   | /customer/payment                                       | Stripe 결제 페이지 리다이렉트 |
| GET    | /customer/pay_complete                                  | 고객 결제 완료                |
| GET    | /customer/pay_cancel                                    | 고객 결제 취소                |

</div>
</details>

<details>
<summary>Sajjang</summary>
<div markdown="1">

| Method | URL                                                                   | Description             |
| ------ | --------------------------------------------------------------------- | ----------------------- |
| GET    | /sajjang/home                                                         | sajjang 홈페이지        |
| GET    | /sajjang/store/add                                                    | 가게 등록 페이지        |
| POST   | /sajjang/store/add                                                    | 가게 등록               |
| GET    | /sajjang/store/<<int:store_id>>                                       | 가게 정보 상세 보기     |
| GET    | /sajjang/store/<<int:store_id>>/edit                                  | 가게 정보 수정 페이지   |
| POST   | /sajjang/store/<<int:store_id>>/edit                                  | 가게 정보 수정          |
| POST   | /sajjang/store/<<int:store_id>>/delete                                | 가게 삭제               |
| GET    | /sajjang/store/<<int:store_id>>/menu                                  | 가게 메뉴 보기          |
| GET    | /sajjang/store/<<int:store_id>>/menu/add                              | 가게 메뉴 등록          |
| POST   | /sajjang/store/<<int:store_id>>/menu/add                              | 가게 메뉴 등록          |
| GET    | /sajjang/store/<<int:store_id>>/menu/<<int:menu_id>>                  | 가게 메뉴 상세보기      |
| GET    | /sajjang/store/<<int:store_id>>/menu/<<int:menu_id>>/edit             | 가게 메뉴 수정 페이지   |
| POST   | /sajjang/store/<<int:store_id>>/menu/<<int:menu_id>>/edit             | 가게 메뉴 수정          |
| POST   | /sajjang/store/<<int:store_id>>/menu/<<int:menu_id>>/delete           | 가게 메뉴 삭제          |
| GET    | /sajjang/store/<<int:store_id>>/order                                 | 가게 수락한 주문 조회   |
| GET    | /sajjang/store/<<int:store_id>>/order/<<int:order_id>>                | 가게 주문 상세 페이지   |
| GET    | /sajjang/store/<<int:store_id>>/order/confirm                         | 고객이 결제한 주문 조회 |
| GET    | /sajjang/store/<<int:store_id>>/order/confirm/<<int:order_id>>        | 결제한 주문 상세보기    |
| POST   | /sajjang/store/<<int:store_id>>/order/confirm/<<int:order_id>>/accept | 고객이 결제한 주문 수락 |
| POST   | /sajjang/store/<<int:store_id>>/order/confirm/<<int:order_id>>/reject | 고객이 결제한 주문 거절 |

</div>
</details>

<details>
<summary>Delivery Crew</summary>
<div markdown="1">

| Method | URL                                                       | Description                    |
| ------ | --------------------------------------------------------- | ------------------------------ |
| GET    | /delivery_crew/home                                       | delivery_crew 홈페이지         |
| GET    | /delivery_crew/delivery_history                           | 해당 크루의 배달 기록          |
| GET    | /delivery_crew/delivery_history/<<int:order_id>>          | 배달항목의 디테일              |
| POST   | /delivery_crew/<<int:order_id>>/accept                    | 배달 요청 수락                 |
| POST   | /delivery_crew/<<int:order_id>>/deny                      | 배달 거절                      |
| POST   | /delivery_crew/delivery_history/<<int:order_id>>/pickup   | 배달 배정 완료 → 배달 중       |
| POST   | /delivery_crew/delivery_history/<<int:order_id>>/complete | 배달 중 → 배달 완료            |
| GET    | /delivery_crew/address/                                   | delivery_crew 위치             |
| GET    | /delivery_crew/address/add/                               | delivery_crew 위치 추가 페이지 |
| POST   | /delivery_crew/address/add/                               | delivery_crew 위치 추가        |
| GET    | /delivery_crew/address/<<int:address_id>>/                | delivery_crew 위치 상세보기    |
| GET    | /delivery_crew/address/<<int:address_id>>/edit/           | delivery_crew 위치 수정 페이지 |
| POST   | /delivery_crew/address/<<int:address_id>>/edit/           | delivery_crew 위치 수정        |
| POST   | /delivery_crew/address/<<int:address_id>>/delete/         | delivery_crew 위치 삭제        |

</div>
</details>

## Page Work Flow - 해민

## Main Functionality - 해민, 건우, 한솔, 예진

#### Frontend

- `Django Template` 상속을 통해 코드가 중복되지 않도록 합니다.
- `Bootstrap`을 활용해 HTML 태그에 class 속성을 추가해 디자인합니다.

#### Backend

#### Infra

## Architecture - 민혁

(아키텍쳐: 백엔드와 프론트엔드가 어떻게 소통하는지)

## Installation & Run - 민혁

---

# If we need to use image file, please use the below method

<img src="static/images/argocdmornitoring.png" >
