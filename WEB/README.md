<h1>이벤트 데이터 수집 및 모델 선택 웹 애플리케이션</h1>
  
<h2>개요</h2>
<br/>
<h3>이 웹 애플리케이션은 다양한 입력 양식을 통해 고객 데이터를 수집하고, 사용자가 AI 모델을 선택하여 고객 행동을 예측할 수 있도록 설계되었습니다.
  <br/>
주요 목적은 직관적인 인터페이스를 제공하여 고객 데이터를 제출하고, 그 결과를 표시하는 것입니다. 
  <br/>
주요 카테고리로는 인터넷 서비스, 결제 방법, 계약 유형 및 기타 기능이 포함됩니다.
<br/>
또한, 메인페이지는 이탈율 및 잔존율을 보여주는 그래프를 포함합니다.</h3>
<br/>

이 프로젝트는 다음과 같은 기능을 포함합니다:
<br/>
<br/>
사용자 친화적인 프론트엔드 인터페이스: 고객 정보를 수집하기 위한 직관적인 입력 양식과 버튼 제공.
<br/>
<br/>
인터랙티브 버튼 및 토글 요소: 다양한 옵션을 선택할 수 있는 버튼 및 토글 기능.
<br/>
<br/>
AI 모델 선택 인터페이스: 두 가지 모델(A-Model, P-Model) 중 하나를 선택할 수 있음.
<br/>
<br/>
데이터 제출 기능: 수집된 입력 데이터를 로그로 기록하고 처리하는 기능.
<br/>
<br/>
<br/>
기능
주요 기능
모델 선택: 사용자는 A-Model 또는 P-Model 중에서 선택할 수 있습니다. 선택된 모델은 제출된 데이터를 처리하거나 예측하는 데 영향을 미칩니다.
<br/>
동적 데이터 수집: 드롭다운, 버튼, 텍스트 필드 등의 다양한 입력 양식을 사용하여 고객 데이터를 수집합니다.
<br/>
<br/>
토글 기능: 인터넷 서비스와 같은 특정 카테고리에서 "Yes"를 선택하면 추가 입력 양식이 표시되며, "No"를 선택하면 해당 양식이 숨겨집니다.
<br/>
<br/>
데이터 제출: 모든 데이터를 제출하면 콘솔에 JSON 형식으로 출력되며, 향후 분석이나 예측에 사용할 수 있습니다.
<br/>
<br/>
사용자 인터페이스
왼쪽 패널: 고객의 성별, 파트너 여부, 부양가족, 나이, 계약 기간 등을 입력할 수 있는 입력 양식이 있습니다.
<br/>
<br/>
오른쪽 패널: 인터넷 서비스, 결제 방법, 계약 유형, 전화 서비스 등 다양한 옵션을 선택할 수 있는 버튼이 포함된 표가 있습니다.
<br/>
<br/>
제출 버튼: 고객이 입력한 데이터를 서버 또는 콘솔로 제출하는 기능을 제공합니다.
<br/>
<br/>
라벨링된 데이터
고객의 선택사항은 미리 정의된 라벨 값으로 변환됩니다.
Ex) Yes는 1로, No는 0으로 변환.
계약 기간: Month-to-month는 1, One Year는 12, Two Year는 24로 변환.
결제 방법: Electronic Check는 3, Mailed Check는 2 등으로 변환.
<br/>
<br/>
<br/>
기술 스택
HTML5
CSS3
JavaScript
