import itertools
from .pred_with_model import inference_on_data

def optimize_churn(input_list):
    try:
        results, shap_dic = inference_on_data(input_list, 'all', True)

        if all(value is None for value in shap_dic.values()):
            return "전부 None입니다."

        important_columns = ['PaymentMethod', 'TechSupport', 'OnlineSecurity', 'InternetService', 'PaperlessBilling']
        output_list = []
        result_str = ""

        int_shap_keys = [key for key, value in shap_dic.items() if isinstance(value, int)]
        num_int_features = len(int_shap_keys)

        # 각 피처 조합 반복
        for i in range(1, num_int_features + 1):
            for feature_combination in itertools.combinations(int_shap_keys, i):
                temp_input = input_list.copy()

                for feature in feature_combination:
                    if shap_dic[feature] is not None:
                        possible_values = get_possible_values(feature)
                        for new_value in possible_values:
                            modified_input = temp_input.copy()
                            previous_value = modified_input[get_index(feature)]
                            modified_input[get_index(feature)] = new_value

                            if modified_input[5] == 0:
                                modified_input[6:12] = [0] * 6
                            elif modified_input[5] == 1 and any(modified_input[6:12]):
                                modified_input[5] = 1

                            # 매핑 후 가격 계산
                            new_monthly_charge, new_total_charge = calculate_mapped_charges(input_list, modified_input)
                            modified_input[15] = new_monthly_charge
                            modified_input[16] = new_total_charge
                            # 원래 값으로 복구
                            modified_input = revert_mapped_values(modified_input)
                            # 이탈 확인
                            new_results, _ = inference_on_data(modified_input, 'all', True)

                            if new_results == 0:
                                output_list.append((tuple(modified_input), feature_combination, new_value, previous_value))

        best_list = sorted(output_list, key=lambda x: (x[0][5], x[0][6], x[0][9]), reverse=True)
        if best_list:
            best_case = best_list[0][0]
            # print(best_case)
            # 변경된 컬럼 변수
            changes_made = False

            for feature in important_columns:
                index = get_index(feature)
                new_value = best_case[index]
                previous_value = input_list[index]

                if new_value != previous_value:
                    # 각 컬럼의 값을 매핑하여 출력
                    result_str += f"{feature}: {map_feature_value(feature, new_value)} (이전 값: {map_feature_value(feature, previous_value)})\n"
                    result_str += f'MonthlyCharges : {best_case[15]}\n'
                    result_str += f'TotalCharges : {best_case[16]}\n'
                    changes_made = True
                    # print(result_str)

            if not changes_made:
                result_str += "변경된 것이 없습니다. 현행을 유지하시죠\n"
                # print(result_str)
        else:
            result_str += "자유로운 영혼의 이 고객을 잡을 수는 없습니다...\n"
            # print(result_str)

        return result_str
    except KeyError as e:
        print(f"KeyError: {e} - modified_input: {modified_input}")
        raise  # 에러를 다시 발생시켜서 원인을 추적할 수 있도록 합니다.

# 각 컬럼들이 가능한 숫자
def get_possible_values(feature):
    if feature == 'PaperlessBilling':
        yield 0
        yield 1
    elif feature == 'InternetService':
        yield 0
        yield 1
        yield 2
    elif feature in ['OnlineSecurity', 'TechSupport']:
        yield 0
        yield 1
    elif feature == 'PaymentMethod':
        yield 0
        yield 1
        yield 2
        yield 3
    return

def get_index(feature):
    feature_to_index = {
        'PaperlessBilling': 13,
        'InternetService': 5,
        'OnlineSecurity': 6,
        'TechSupport': 9,
        'PaymentMethod': 14,
    }
    return feature_to_index[feature]

# TotalCharges & MonthlyCharges 계산 함수
def calculate_mapped_charges(original_input, modified_input):
    mapping = {
        'InternetService': {0: 21, 1: 58, 2: 91},
        'OnlineSecurity': {0: 78, 1: 75},
        'TechSupport': {0: 80, 1: 74}
    }

    # 입력값 매핑
    original_mapped = {
        'InternetService': mapping['InternetService'][original_input[5]],
        'OnlineSecurity': mapping['OnlineSecurity'][original_input[6]],
        'TechSupport': mapping['TechSupport'][original_input[9]]
    }

    modified_mapped = {
        'InternetService': mapping['InternetService'][modified_input[5]],
        'OnlineSecurity': mapping['OnlineSecurity'][modified_input[6]],
        'TechSupport': mapping['TechSupport'][modified_input[9]]
    }

    # 각 서비스별 차이 계산
    internet_service_diff = modified_mapped['InternetService'] - original_mapped['InternetService']
    online_security_diff = modified_mapped['OnlineSecurity'] - original_mapped['OnlineSecurity']
    tech_support_diff = modified_mapped['TechSupport'] - original_mapped['TechSupport']

    # 총 차이
    total_diff = internet_service_diff + online_security_diff + tech_support_diff
    
    # MonthlyCharges
    new_monthly_charge = original_input[15] + total_diff
    if total_diff == 0:
        new_total_charge = original_input[16]
    else:  # TotalCharges = MonthlyCharges * tenure
        new_total_charge = new_monthly_charge * modified_input[3]

    return round(new_monthly_charge, 3), round(new_total_charge, 3)




# 원래 값으로 되돌리는 함수
def revert_mapped_values(input_list):
    revert_mapping = {
        'InternetService': {21: 0, 58: 1, 91: 2},
        'OnlineSecurity': {78: 0, 75: 1},
        'TechSupport': {80: 0, 74: 1}
    }

    input_list[5] = revert_mapping['InternetService'].get(input_list[5], input_list[5])
    input_list[6] = revert_mapping['OnlineSecurity'].get(input_list[6], input_list[6])
    input_list[9] = revert_mapping['TechSupport'].get(input_list[9], input_list[9])

    return input_list

# 값 매핑을 처리하는 함수
def map_feature_value(feature, value):
    mappings = {
        'InternetService': {0: 'No', 1: 'DSL', 2: 'Fiber optic'},
        'OnlineSecurity': {0: 'No', 1: 'Yes'},
        'TechSupport': {0: 'No', 1: 'Yes'},
        'PaymentMethod': {
            0: 'Credit card (automatic)',
            1: 'Bank transfer (automatic)',
            2: 'Mailed check',
            3: 'Electronic check'
        },
        'PaperlessBilling': {0: 'No', 1: 'Yes'}
    }
    
    return mappings.get(feature, {}).get(value, value)