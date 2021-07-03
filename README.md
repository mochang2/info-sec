# info-sec assignment

* md 사용법: <https://gist.githinsb.com/ihoneymon/652be052a0727ad59601>

###### 7월 3일 교육 내용

## 1. BoB 보안인
by 김영옥(보안컨설팅 멘토)-빅데이터, AI 보안  
1) <ins>내가 중심이 되어 배워 나가자.</ins>
* 어떤 목표를 이루고 싶어서 BoB에 들어왔나? => 각자 생각
* 5년 후에 나의 모습은? => 각자 생각
* 초발심시변정각: 첫 번째 발생한 마음이 변하지 말아야 한다(초심을 잃지 말자)

-----------------------------

## 2. 4차 산업혁명과 보안의 역할
by 김영옥(보안컨설팅 멘토)  
1) <ins>4차 산업혁명이란</ins>
* 자율주행. 사물인터넷(IoT). 빅데이터. 블록체인. 인공지능. AR/VR 등으로 구성 => 4차 산업혁명은 디지털을 통한 사회 전반적인 변화(편리하고 간편하고 쉽고 빠르고 안전한, 즉 자동화)를 총칭.
* 단순 융합(더하기)을 넘어선 화학적 융합(곱하기). 온/오프라인, 생물학적 영역의 경계가 없어짐. 타 산업 분야(도시, 제조, 자동차 의료 등등) * ICT 기술(IoT, 클라우드, 빅데이터, AI ...) => smart 시티/팩토리/카/의료. 이에 대한 근본을 보안이 잡아준다.
* 우리나라는 제조업에 강하고 ICT 응용도 강하다. 하지만 중국, 인도 등과의 경쟁에서 제조업 경쟁력의 한계 / 인구 절벽, 고령화 문제로 인해. 4차 산업에 반드시 뛰어들어야 하는 상황에 직면.
* 3가지 중요한 키워드.
    * 가. 초연결성(IoT 진화). 많은 디바이스들의 연결. ICT를 기반으로 하는 IoT 및 IoE의 진화를 통해 인간-인간, 인간-사물, 사물-사물을 대상으로 한 초연결성이 기하급수적으로 확대. 2020년까지 인터넷 플랫폼 가입자와 스마트 디바이스에 의해 상호 간 네트워킹 될 것으로 전망.
    * 나. 초지능화(AI, 빅데이터). 기계가 지능을 가짐. 강화산업 구조의 초지능화. Google의 알파고, IBM의 왓슨 등 기계학습과 딥러닝 및 빅데이터에 기반한 인공지능은 초지능적 제품 생산과 서비스 제공에 기여할 것으로 전망.
    * 다. 초융합(산업영역과 경계 융합). 기술간, 산업간, 사물-인간 간의 경계가 사라지는 대융합의 시대가 될 것으로 전망. 데이터와 정보, 콘텐츠, 지식의 융합을 통해 산업간, 기술간 융합 완성.  
_cf1) IoT: 사물인터넷은 사람, 사물, 공간, 데이터 등 모든 것이 인터넷으로 서로 연결되어, 정보가 생성/수집/공유/활용되는 초연결 인터넷._  
_cf2) 빅데이터: 업무, 센서, 생활 등에서 발생되는 정형, 비정형 데이터를 수집하여 가치를 도출하는 기술 또는 서비스._
* Platform(ex. kakao) Effect. 4차 산업 혁명을 이끌기 위해선 플랫폼 장악이 우선시되어야 함. 시장을 지배하는 강력한 소수의 플랫폼으로 집중하게 됨. 소비자에게 높은 가치와 합리적이고 저렴한 가격으로 명백한 혜택 제공. 불평등과 불균형으로 인한 사회 갈등, 불안 등 사회 위험 발생. 가치와 힘이 소수에게 집중되는 것을 막기 위해 공동혁신에 대한 개방성과 기회를 보장. 모든 사람에게 기회 제공. 플랫폼의 혜택과 위험성 사이의 균형(독과점 방지, 후진국 산업 보호), 국가내, 국가간 조정기구.

2) <ins>4차 산업혁명 시대에서 보안 패러다임 변화</ins>
* 전통적인 보안의 패러다임 CIA => 새로운 패러다임 CIA + Privacy, Safety, Reliability. 예전에는 데이터 자체에만 신경을 썼다면 데이터가 작동시키는 기계, 그로 인해 영향을 받는 사람, 환경에 대한 것까지 고려되어야 함.
    * 가. Privacy 개인정보를 못 쓰게 관리하자는 것이 아닌 안전하게 활용. 익명/비식별화 등의 방식연구.
    * 나. Safety 사람이 안전하게 설계되어야 함.
    * 다. Reliability 이러한 기술에 대한 의지를 할 수 있어야 함.
* 디지털 보안 전략. Resilient Digital Security를 중심으로 Biz-Aligned Security, People-Centric Security, Data-Driven Security로 이루어져 있음.

-----------------------------

## 3. 정보보안 기본이해 및 방법론
by 한철규
1) <ins>철학/보안/보안철학</ins>
* 자신의 경험에서 얻은 인생관, 세계관, 신조 따위를 이르는 말. 보안에 대해 공부하다가도 어떠한 내용에 대해 다룰지, 어떤 솔루션을 제공할지 등에 대해 철학을 가질 필요가 있음.
* 보안이란 안전을 유지함. 사회의 안녕과 질서를 유지함 등을 의미(정보보안과 정보보호는 크게 구분 짓지 않아도 됨)
* 일체유심조. 모든 것은 오직 마음이 지어냄. 좋은 철학이 좋은 행동을 이끌고 좋은 보안인이 되도록 만듦.

2) <ins>안전?</ins>
* _해커의 수준 분류_(Gilbert Alavendian)
    * 가. _Lamer_(절름발이): 해커는 되고 싶지만 경험도 기술도 없는 이들.
    * 나. _Script kiddies_: 약간의 기술, 알려진 도구 사용, 학생들.
    * 다. _Developed kiddies_: 해킹 기법 잘 알지만 새로운 취약점을 찾아내지 못함.
    * 라. _Semi-elite_: 특정 취약점을 알고 공격, 언론 보도되는 대부분.
    * 마. _Elite_: 취약점 알고 해킹 성공. 공격 흔적을 감춤. APT(Advanced Persistent Threat)의 성향을 띄움.
* 연구에 따르면, 죄의식적 관점에서 일반 범죄와 사이버 범죄를 비교할 때, 사이버 범죄에 대한 죄의식이 더 약함.
* 해킹하는 이유.
    * 가. (획득가치 * 유출용이성: 가치) > (충격 * 발생가능성: 위험) 할 때 기대 이익이 높기 때문에. 따라서 획득가치와 유출용이성을 낮추거나 충격과 발생가능성을 높임으로써 해커를 단념시킬 수 있음. 전자의 대책으로는 익명화, 암호화, 후자의 대책으로는 법적 처벌 강화, 양쪽 모두에는 관리적/물리적/기술적 보호대책이 있음.
    * 나. 불쾌감. 불쾌감이 높으면 비도덕적 행위를 합리화하기 쉬움.
    * 다. 작은 부정행위가 큰 부정행위를 초래함으로써, 차츰 더 심한 해킹을 시도함.
    * 라. 다른 사람들이 규칙을 지키지 않으면 본인도 규칙을 지키기 싫어짐.
* 보안 교육의 효과. 프로젝트 시작 직전, 서약서 작성하고 서명, 지속적으로 교육이 있다면, 효과가 크다고 밝혀짐. 사슬의 강함은 가장 취약한 부분의 강인함에 의해 결정됨. 보안에서는 주로 가장 취약한 부분이 사람이기 때문에, 사람에 대한 보안 교육이 필요함.

3) <ins>보안 방법론</ins>
* SW 위기(시스템의 대규모화에 따라 소프트웨어의 신뢰성 저하, 개발비의 증대, 계획의 지연 등의 현상)의 극복 방법론. 한정된 자원으로 고품질의 SW를 일정기간 내에 개발.
    * 가. 공학적 접근: 구조적 방법론, 정보공학 방법론, 객체지향 방법론, CBD 방법론, 프로젝트 관리기법
    * 나. 자동화 도구활용: CASE, 코드 생성/관리기, Repository, 형상관리 도구
    * 다. 표준화: 역공학, 재공학 활용, S/W, DATA의 표준화, Reusability의 체제화
    * 라. 품질보증체제: 품질관리 정착, ISO 품질보증체제 도입, CMM/SPICE 도입, 정보시스템 감리
* 방법론 vs SW life cycle. 방법론: 일하는 방식을 체계화한 것(WBS: 일정관리표, 산출물 등 7가지로 구성됨) . SW life cycle: 소프트웨어 제작부터 폐기까지 일련의 과정.
* SW life cycle의 유형
    * 가. 폭포수(Waterfall) 모델
    ![Waterfall model](https://user-images.githubusercontent.com/63287638/124350075-70db6e80-dc2d-11eb-9db9-e540ca5de7e9.png)  
    * 나. 프로토타입(Prototype) 모델
    ![Prototype model](https://user-images.githubusercontent.com/63287638/124350081-789b1300-dc2d-11eb-9ebb-21dd257c6593.png)  
    * 다. 나선형(Spiral) 모델
    ![Spiral model]](https://user-images.githubusercontent.com/63287638/124350084-7f298a80-dc2d-11eb-92f3-05b436fc6db3.png)  
    * 라. 증분형(Incremental) 모델
    ![Incremental model](https://user-images.githubusercontent.com/63287638/124350090-8cdf1000-dc2d-11eb-85a2-648ad3efb15d.png)  
    * 마. 진화적(Evolutionary) 모델
    ![Evolutionary model](https://user-images.githubusercontent.com/63287638/124350095-923c5a80-dc2d-11eb-97a2-cd24aae609cf.png)  

* 방법론의 발전사. 구조적 방법론(폭포수) -> 정보공학 방법론(나선형) -> 객체지향 방법론(나선형) -> CBD 방법론(나선형). _정보공학 방법론의 중요사항: 관심사의 분리(프로세스와 데이터를 분리하기 시작한 첫 번째 방법론)_
