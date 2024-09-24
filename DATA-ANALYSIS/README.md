### 📌 EDA
총 21개의 컬럼 중 17개의 범주형 데이터를 가지고 있는 데이터셋이다. 
사용자의 개인정보 중 이탈여부와 연관된 데이터를 가진 컬럼은 Partner와 Dependents일 것으로 예상하여 해당 여부에 따라 달리 학습하여 5개의 모델을 생성하였다.

이탈여부와 유의미한 상관관계를 보이는 컬럼 10개 선정
-> InternetService, Contract, PaymentMethod, PaperlessBilling, OnlineSecurity, OnlineBackup, DeviceProtection,TechSupport, StreamingTV, StreamingMovies

이 중 7개의 컬럼이 변수에 따라 이탈률의 차이를 보여 이분형 로지스틱 회귀를 활용해 상관계수를 확인. 높은 상관계수를 가지는 컬럼을 이탈률의 요인이라 판단하여 그리드서치 알고리즘에 적용
-> InternetService ,OnlineSecurity, TechSupport, PaymentMethod, PaperlessBilling

![image](https://github.com/user-attachments/assets/35f096f9-d638-4ed1-9f10-68a9ec1d0845)



 # Grid search
 1. InternetService ,OnlineSecurity, TechSupport, PaymentMethod, PaperlessBilling 해당 5개의 컬럼에 대해서 모델에서 이탈률을 0(No) 이라고 예측하는 파라미터값 찾기
 2. 다수의 조합 중 서비스를 가입하는 방향으로 최적의 솔루션 정하기
 3. 이 중 charges에 대해 영향을 끼치는 컬럼들의 기존값과 솔루션값의 평균의 차이만큼 charges에 반영하기
 4. 다시 모델에 넣고 이탈률 0(No) 확인하면 최종 솔루션으로 제공
