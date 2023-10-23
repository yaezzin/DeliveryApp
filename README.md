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

#### 문건우

#### 이한솔

#### 정해민 - [해민's task list](https://www.notion.so/7845ddd52ef74cdda467b4a1ebfafb2a?v=9960c551d69944e58671cfe491287647&pvs=4)

- DataBase - design ERD
- BackEnd - account function (urls, views, templates)
- BackEnd - customer function (urls, views, templates)
- BackEnd - payment (using Stripe)
- BackEnd - delivery Crew (T Map API navigation)

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

## API statements - 건우

## Page Work Flow - 해민

## Main Functionality - 해민, 건우, 한솔, 예진

#### Frontend

#### Backend

- Account

  - Sign-in, Sign-out, Sign-up

    <img src="static/images/page_work_flow/accounts/signin, signup.png" width=60%>

- Customer

  - Add or Edit address
  - Search stores by categories or string
  - Add to Cart
  - Payment

    <img src="static/images/page_work_flow/customer/payment.png" width=60%>

- Sajjang

  - Add or Edit own store, menu
  - Accept or Deny orders

- Delivery Crew

  - Accept or Deny delivery_orders
  - Navigate from store to customer

    <img src="static/images/page_work_flow/delivery_crew/delivery_home_and_navigate.png" width='70%'>

  - Set delivery complete

    <img src="static/images/page_work_flow/delivery_crew/delivery_complete.png" width='50%'>

#### Infra

## Architecture - 민혁

(아키텍쳐: 백엔드와 프론트엔드가 어떻게 소통하는지)

## Installation & Run - 민혁

---

# If we need to use image file, please use the below method

<img src="static/images/argocdmornitoring.png" >
