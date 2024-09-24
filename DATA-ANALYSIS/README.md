### 📌 EDA
총 21개의 컬럼 중 17개의 범주형 데이터를 가지고 있는 데이터셋이다. 
사용자의 개인정보 중 이탈여부와 연관된 데이터를 가진 컬럼은 Partner와 Dependents일 것으로 예상하여 해당 여부에 따라 달리 학습하여 5개의 모델을 생성하였다.

이탈여부와 유의미한 상관관계를 보이는 컬럼 10개 선정
-> InternetService, Contract, PaymentMethod, PaperlessBilling, OnlineSecurity, OnlineBackup, DeviceProtection,TechSupport, StreamingTV, StreamingMovies

이 중 7개의 컬럼이 변수에 따라 이탈률의 차이를 보여 이분형 로지스틱 회귀를 활용해 상관계수를 확인. 높은 상관계수를 가지는 컬럼을 이탈률의 요인이라 판단하여 그리드서치 알고리즘에 적용
-> InternetService ,OnlineSecurity, TechSupport, PaymentMethod, PaperlessBilling

![image](https://github.com/user-attachments/assets/35f096f9-d638-4ed1-9f10-68a9ec1d0845)



 ### 📌 Grid search
 1. InternetService ,OnlineSecurity, TechSupport, PaymentMethod, PaperlessBilling 해당 5개의 컬럼에 대해서 모델에서 이탈률을 0 (No) 이라고 예측하는 파라미터값 찾기
 2. 다수의 조합 중 서비스를 가입하는 방향으로 최적의 솔루션 정하기
 3. 이 중 charges에 대해 영향을 끼치는 컬럼들의 기존값과 솔루션값의 평균의 차이만큼 charges에 반영하기
 4. 다시 모델에 넣고 이탈률 0(No) 확인하면 최종 솔루션으로 제공

    * 종속변동이 있는 컬럼들 변동 시 동기화시키기
 5. 코드구현
  optimizechurn 함수
    
주요 역할:
      주어진 입력 데이터를 바탕으로 이탈률을 최적화
      각 피처의 SHAP 값을 확인 + 가능한 조합을 시도 => 이탈률이 0인 경우를 찾아내는 기능.
주요 구성:
    results, shap_dic = inference_on_data(input_list, 'all', True): 입력 리스트에 대한 예측 및 SHAP 값 계산
    if all(value is None for value in shap_dic.values()): 모든 SHAP 값이 None일 경우 경고 메시지를 반환
    important_columns: 이탈률을 최적화할 때 중점을 두는 주요 피처 리스트
    output_list: 결과를 저장 리스트

SHAP 값에 기반한 피처 조합 탐색
 int_shap_keys = [key for key, value in shap_dic.items() if isinstance(value, int)]: SHAP 값이 정수형인 피처를 필터링하여 int_shap_keys 리스트 생성
 ○ 조합 생성:
     itertools.combinations(int_shap_keys, i): 각 피처의 조합 생성
 ○ 각 조합에 대한 반복:
     temp_input = input_list.copy(): 원본 입력을 복사하여 진행
 ○ 각 피처의 가능한 값을 확인하고, 변경된 피처의 값 수정

이탈률 최적화 로직
 if modified_input[5] == 0:
         modified_input[6:12] = [0] * 6
 elif modified_input[5] == 1 and any(modified_input[6:12]):
         modified_input[5] = 1
 ○ modified_input[5] (InternetService)의 값에 따라 다른 피처(OnlineSecurity, OnlineBackup 등)를 조정

가격 계산
 new_monthly_charge, new_total_charge = calculate_mapped_charges(input_list, modified_input)
 calculate_mapped_charges 함수를 호출해 새로운 월별 및 총 요금을 계산

원래 값으로 되돌리기
 modified_input = revert_mapped_values(modified_input) : 변경된 피처 값을 원래의 값으로 되돌리기

이탈률 확인 및 결과 저장
 new_results, 
 = inference_on_data(modified_input, 'all', True)
    if new_results == 0:
            output_list.append((tuple(modified_input), feature_combination, new_value, previous_value))
: 새로운 입력에 대해 이탈률을 확인 & 이탈률이 0인 경우 output_list에 추가

결과 정렬 및 출력
 best_list = sorted(output_list, key=lambda x: (x[0][5], x[0][6], x[0][9]), reverse=True): 이탈률을 최적화한 결과를 기준으로 output_list를 정렬

최종 결과 생성
: 변경된 피처를 출력, 변경 사항이 없으면 경고 메시지를 반환
  최적의 결과가 없으면 별도의 메시지를 출력

보조 함수
 ○ get_possible_values(feature): 각 피처의 가능한 값을 반환 함수
 ○ get_index(feature): 피처 이름에 따른 인덱스 반환 함수
 ○ calculate_mapped_charges(original_input, modified_input): 요금 계산 함수
 ○ revert_mapped_values(input_list): 매핑된 값을 원래대로 되돌리는 함수
 ○ map_feature_value(feature, value): 피처 값에 대한 매핑을 반환
