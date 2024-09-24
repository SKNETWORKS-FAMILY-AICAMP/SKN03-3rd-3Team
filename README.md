## 👋🏻 팀 소개 👋🏻
### 📌 팀 명
SKN03-3nd-3Team : **5️⃣❎5️⃣**

<br/><br/>

### 📌 팀 멤버
| 박종명 | 박용주 | 서민정 | 이주원 | 하은진 |
|:--:|:--:|:--:|:--:|:--:|
|![Group 11](https://github.com/user-attachments/assets/17bf149f-471e-4c95-80a1-66effa211bf9)|![Group 12](https://github.com/user-attachments/assets/e7217b02-c9f8-4bc9-ae2d-0a31c5f75349)|![image 23](https://github.com/user-attachments/assets/7dea616b-7a83-4cba-b6ef-f29fd597a440)|![Group 10](https://github.com/user-attachments/assets/e0e30c18-d852-4e13-9122-938d8a2a9292)|![Group 13](https://github.com/user-attachments/assets/04e43b07-22c3-4f08-9d7b-79a0c8bef36d)|
| @ | @ | @seom-j | @ | @ha000jin |
| Project Leader | Web | Modeling | Data Analysis | Data Analysis |


<br/><br/><br/>


## 5️⃣❎5️⃣
### 📌 개발 기간
2024-09-23 ~ 2024-09-24 (총 2일)

<br/><br/>

### 📌 프로젝트 소개
통신사 관리자가 고객에 대한 영업 정보를 얻을 수 있도록 Teleco Customer 데이터를 사용하여 통신사 이탈 고객을 예측한다. 또한 학습된 모델을 바탕으로 고객이 이탈하게 된 주요 원인들을 분석하여 이탈을 방지하는 솔루션 제시한다.


<br/><br/>

### 📌 프로젝트 목표
텔레콤 고객 이탈 방지 웹서비스 제작
: 이탈 관련 대시보드 제공 및 이탈 예방 수단 제공

<br/><br/>

### 📌 데이터 정보
Telecom Customer Churn Prediction (Kaggle)
> 7,043 rows
> 
> 21 columns

![image](https://github.com/user-attachments/assets/98b320fd-580f-49c8-a1f8-9786c23f41dd)


<br/><br/>

### 📌 프로젝트 내용
**① 이탈 관련 데이터 분석 대시보드**
>  전체 사용자 이탈률 및 서비스별 이탈률 분석 대시보드 제공 
>
>  목적 : 관리자의 이탈 원인 파악

<br/>

**② 이탈 예측 수행 & 이탈 예방 수단 탐색**
> 이탈 예측 수행 및 이탈 예방 수단 제공 
>
> 목적 : 한명의 사용자에 대한 퍼스널 솔루션 제공

<br/><br/>

### 📌 사이트 플로우차트
![image](https://github.com/user-attachments/assets/528bb3d9-1f2e-4d8d-9aaa-3faaafe5ec84)

<br/><br/>

### 📌 중요 컬럼 이탈률 시각화


<br/><br/>

### 📌 프로젝트 결과 

👉🏻 

<br/><br/>

### 📌 EDA
총 21개의 컬럼 중 17개의 범주형 데이터를 가지고 있는 데이터셋이다. 
사용자의 개인정보 중 이탈여부와 연관된 데이터를 가진 컬럼은 Partner와 Dependents일 것으로 예상하여 해당 여부에 따라 달리 학습하여 5개의 모델을 생성하였다.

이탈여부와 일정 이상의 상관관계를 보이는 컬럼 10개
(InternetService, Contract, PaymentMethod, PaperlessBilling, 
OnlineSecurity, OnlineBackup, DeviceProtection,TechSupport, StreamingTV, StreamingMovies)

7개의 컬럼이 변수에 따라 이탈률의 차이를 보여 이분형 로지스틱 회귀를 활용해 상관계수를 확인해보았다. 높은 상관계수를 가지는 컬럼을 이탈률의 요인이라 판단하여 그리드서치 알고리즘에 적용하였다.
(InternetService ,OnlineSecurity, TechSupport, PaymentMethod, PaperlessBilling)
![image](https://github.com/user-attachments/assets/76ae21db-6af1-465a-aa44-f3d2ce109cee)


<br/><br/>

### 📌 모델링


<br/><br/>

### 📌 프로젝트 에러 로그


<br/><br/>

### 📌 프로젝트 후기


