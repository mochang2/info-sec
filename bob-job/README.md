## 210905
2013년: APT 대두. 국정원이 국가적 보안 전쟁에서 최고의 지위를 갖도록 확고히 됨.  
DDoS가 성공한 이유? 네트워크 계층 특성상 정상 사용자와 비정상 사용자를 구분하기가 힘들어서. 그렇다면 1980년대에 유행했던 DDoS 공격이 지금에도 유효할까? Yes. 그 당시에 쓰던 TCP/IP 프로토콜 스택과 현재 쓰는 TCP/IP 프로토콜 스택이 근본적으로 바뀌지 않았기 때문.  
  
wormization: 다수의 시스템 해킹 가능. 다양한 형태의 시스템 제어 용이. 정보 유출 및 신뢰하는 호스트로 위장 용이. 근원지 추적 불가. 위치 추적 불가. 자유로운 업데이트. APT 공격 연계의 용이성.  
  
(역추적 기술)패킷을 보낼 때 s.ip가 항상 일정한 것은 아님. 국가별 프록시 서버를 지나면 그 프록시 서버 주소로 바뀜. 역추적 기술은 패킷 앞에 새로운 헤더를 붙여서 원본 s.ip를 추적하는 기술.

-----------------------------------------------------------------------------------------------

## 210912
샌드박스에서 동적 분석을 할 때, 호출하는 시스템 함수 등의 패턴을 이용(각각의 행위에 점수를 두고, 점수가 몇 점 이상인 경우)해서 악성코드인지 구분함. 하지만 time 함수(스케쥴링)에 되게 약함. 요새는 sleep 등의 함수를 다 뛰어넘게 함.  
  
네트워크 구조(PMS 포함)  
Internet - Anti DDoS - Firewall - IPS - WAF - AV - PMS(내부에서 외부 업데이트 서버에 연결해서, 업데이트 내용을 받아오고 실행함. 실행한 결과가 올바르면 내부 서버에 반영. 내부에서 외부로 가는 패킷에 대한 검증을 제대로 하지 않으면 바로 문제가 생길 수 있음)

-----------------------------------------------------------------------------------------------

## 210919
IDS 차단 기능의 문제점  
IDS 차단 기능: RST 패킷을 보냄.  
외부 네트워크 \-------- TAP 장비 \----------- switch \-------- 여러 개의 내부 서버(2.2.2.0/24 대역)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IDS(NIC 2개 이상. switch와 연결된 MAC: AA-AA-AA-AA-AA-AA)  
IDS는 또 다른 NIC 카드와 IP 주소를 달고 내부 switch와 연결됨(IDS가 TAP 장비와 연결된 부분에 있는 NIC는 promiscuous로 동작하기 때문에 bridge base이고, 이 때문에 IP 주소를 가질 수 없음.). 외부 네트워크는 외부 네트워크 + 라우터 + 또 다른 switch 이런 구조를 가질 수 있음.  
  
IDS는 미러링 장비이기 때문에 문제가 생겼다고 감지했을 때는 이미 내부 서버에 악성 패킷이 침투했을 수 있음. 이를 감지하고 당장에 RST 패킷을 보내서 연결을 끊으려 시도. 내부 switch와 연결된 NIC에서 패킷을 생성하여 보냄.  
하지만 여기서 문제가 발생함. TCP 연결을 끊으려 RST를 보내기 위해서는 내부 서버의 IP처럼 위장하여 보내야 됨. 이 때 switch 내부의 CAM table의 무결성이 깨짐. 즉 하나의 MAC에 대해서 하나의 IP만 매칭된다는 규칙이 깨지면서 fail-open이 됨(AA-AA-AA-AA-AA-AA는 3.3.3.3의 주소를 가지고 있다고 기록했었는데, 2.2.2.2로 바뀜. 이제 해커가 공격 대상을 2.2.2.3으로 바꾸면 IDS는 똑같은 패킷을 보낼 것이고, switch CAM table에 AA-AA-AA-AA-AA-AA MAC 주소에 대해 또 다른 IP 주소를 기록. 그리고 이 과정이 계속 반복되면서 flooding이 일어남). 오히려 스니핑에 취약하게 되어버리고, switch가 정상작동하지 못함.    
![11](https://user-images.githubusercontent.com/63287638/135787362-f659967f-f730-49a6-882b-055abc99d8a8.jpg){: width="100" height="100"}
![22](https://user-images.githubusercontent.com/63287638/135787365-421f33de-66f3-4af2-a7ae-81a3b0e01521.jpg){: width="100" height="100"}
  
  
보강1) TAP(2계층)은 NW를 분석하기 위한 물리적인 케이블. TAP은 송신만 가능하고 수신은 불가능한 기기(mirroring).  
반대로 패킷을 전달받는 분석기기는 수신만 가능하기에 ARP request를 줘도 응답을 못 함. 만약 송신이 가능하다고 하면, 하나의 물리적인 회선에 MAC 주소가 3개(external NW, internal NW, analysis tool)가 되므로 node to node라는 원칙이 깨짐. 따라서 주변 기기들이 이 분석 기기의 MAC을 알 수가 없게 됨. 이를 Ghost 장비(Transparent하다)라고도 함. 
  
보강2) out of path에서 패킷 차단은 PBR 등의 라우팅 프로토콜을 사용함으로써 스위치 장비가 내부로 패킷을 전달하지 않고 블랙홀 인터페이스 등으로 패킷을 보내게끔 만듦으로써 가능. 라우팅 프로토콜이므로 3계층 이상이어야 함.  
  
보강3) FOD: failover device. 컴퓨터 서버, 시스템, 네트워크 등에 이상이 생겼을 때 예비 시스템으로 자동 전환되는 기능.

---------------------------------------------------------------------------------------------------

## 210926
Application F/W 권고 사항: Fail Close.  
(외부)Router -- S/W(200MB/s -> 100MB/s) -- FW1(100MB/s) | FW2(100MB/s) -- IPS1 | IPS2 -- S/W(내부)  
이러한 네트워크 구성일 때, fail close를 사용한다면 문제가 생길 수 있음. 외부 쪽에 있는 스위치 장비가 로드 밸런싱 기능이 있다면, FW1 방향 쪽에 에러가 발생하여 fail close 상태라고 가정. 원래 FW1, FW2가 모두 active로 동작했다면(그리고 각각의 bandwidth가 100MB/s라고 가정) 이 네트워크는 200MB/s의 패킷을 감당할 수 있었음. 하지만 FW1이 고장남으로써 모든 트래픽이 FW2로 전송되고, 장기간 이 상황이 지속된다면 FW2도 고장나거나 패킷이 유실될 수 있음. 따라서 이와 같이 fail close 정책을 사용하고, 로드 밸런싱 기능이 있다면 active / active 구조가 아닌 active / standby 상태를 가져가야 함.  
다만, 보통 LB 앞에 Anti-DDoS 장비를 가져감으로써 active / active 정책을 취함.  
  
로드 밸런서의 종류 : FLB(Firewall Load Balancer), SLB(Server Load Balancer)  
FLB 등을 쓰면 세션 관리에서 문제가 생길 수 있음. symmetric은 패킷이 들어오는 길과 나가는 길이 일치하는 것을 얘기하면, asymmetric은 패킷이 들어오는 길과 나가는 길이 일치하지 않을 수 있음을 의미. 만약 asymmetric 구조라면 syn패킷이 들어오는 길과 syn+ack 패킷이 나가는 길이 다를 수 있다는 의미. 이러한 세션을 관리하기 위해 HA link라고 불리는 것을 통해 여러 장비가 세션 정보와 탐지 정보를 공유함. HA(High Availability) link가 상당한 자원을 잡아먹기 때문에 만약 이러한 HA link를 제공하지 않는다면 symmetric을 위한 알고리즘이 필요한데 그게 바로 해시 알고리즘(정확한 원리는 아직 설명하지 않음)  

---------------------------------------------------------------------------------------------------

## 211003
1) 패킷(3계층)  
* 네트워크 망을 통해 전송하기 쉽도록 자른 데이터의 전송 단위.  
* (5 tuple)데이터를 보내는 시작 주소와 시작 포트, 데이터를 수신할 목적지 주소, 목적지 포트, 그리고 응용 계층이 사용하는 프로토콜 정보 등을 포함  
  
2) 플로우(4계층)   
* 동일한 5 tuple 정보를 가진 패킷들의 집합. 액티브 타임아웃, 인액티브 타임아웃으로 처리됨.  
* 액티브 타임아웃은 동일한 5 tuple을 갖는 패킷들이 일정 시간동안 연속될 경우 여러 개의 패킷을 묶어 하나의 플로우로 저장하게 함.  
* 인액티브 타임아웃은 동일한 5 tuple을 갖는 패킷들이 일정 시간동안 송수신되지 않을 경우 그 때까지의 저장된 패킷을 묶어 하나의 플로우로 저장하게 함.  
* 플로우의 시작시간, 종료시간 정보와 전체 크기(byte 단위) 정보를 갖고 있음.  
* 플로우가 포함하는 패킷의 개수 정보를 포함하고 있음.  
  
3) 세션(7계층)
* 통신의 시작, 중간, 끝 사이에 포함되는 동일한 5 tuple 정보를 가진 플로우의 집합.  
* TCP flag와 인액티브 타임아웃으로 처리됨.  
* 세션의 시작시간, 종료시간 정보와 전체 크기(byte 단위) 정보를 갖고 있음.  
* 세션이 포함하는 플로우 및 패킷의 개수 정보를 포함하고 있음.  
  
Packet Level Protection(Static Filtering). 3계층 장비. 세션 기반보다 비효율적. 세션 기반은 하나의 세션이 악성이라고 판단하면 모든 패킷을 다 분석할 필요가 없기 때문에.  
* 일반적으로 라우터의 ACL이나 Stateless 형태의 방화벽 등이 가지고 있는 방법 기법.  
* Two way communication에 절대적으로 약점을 가짐. 일반적으로 단방향으로 방어를 구현하기 때문에 내부에서 외부로 출발한 네트워크 흐름을 판단하지 못함(포트 범위가 너무 다양하기 때문에 패킷 별로 5 tuple을 다 검사해야 함).  
* Packet Filtering 장비들은 일반적으로 다양한 프로토콜을 지원하지 못함. 이는 C/S 간의 데이터 전송을 위한 랜덤 포트를 교환하는 일에 대해 Flow를 판단하지 못함.  

---------------------------------------------------------------------------------------------------

## 211010
Session Level Protection(SPI Stateful Packet Inspection). 체크포인트사가 최초로 사용한 용어
* 패킷 필터링 방식과 어플리케이션 게이트웨이 방식의 완벽한 방화벽 기능을 수행하지 못하고, 속도가 저하되는 등의 여러 가지 단점을 극복하고 장점만을 구현한 새로운 개념의 방화벽 방식.
* 패킷 필터링의 경우 내부 서버에 대한 허용을 위해 들어오는 방향에 대한 접근 규칙을 설정하였다면 되돌아 나가는 응답에 대해서도 별도의 접근 규칙이 필요. 하지만 상태추적에서는 서비스에 대한 특성 및 통신 상태를 관리할 수 있기 때문에 돌아나가는 패킷에 대해서는 동적으로 접근 규칙을 자동 생성함.
* SIP, Sport, DIP, Dport, Protocol, Session 총 6 tuple 정보를 가짐.
* 세션 계층까지도 동작함.

Application Level Protection
* NW flow를 통제할 수 있으며, 여러 시스템들의 session 상태정보 추적과 드롭된 패킷의 정보를 파악할 수 있음.
* Protocol Attack, Buffer Overflow, Null Operation Code 등과 같이 application을 공격하는 패턴들을 방어할 수 있음.
* Application Level 장비들은 일반적으로 Protocol Analysis, Traffic stream을 reassemble 함으로써 worm이나 virus 또는 콘텐츠의 헤더 부분까지 분석이 가능하나 근래의 콘텐츠 위주의(첨부파일 웜) File Level Protection은 불가능.
생각할 점) application level firewall들이 실상 수백만 개가 넘는 어플리케이션에 대한 분석을 어떻게 할까? 모든 어플리케이션 파싱 정보를 가지고 있을까? 그건 당장에 슈퍼컴퓨터를 써도 감당하기 힘든 용량이다. 그래서 ‘80번 포트는 웹 어플리케이션으로 구분한다’ 와 같은 것처럼 일부 시그니처만 보고 단정지어서 오탐이 많다고 한다.

File Level Protection
* 네트워크 트래픽에서 파일을 추출하여 메일이나 네트워크를 통해 전파되는 웜, 바이러스 트로이목마 등의 멀웨어의 본체를 정밀하게 검사하여 방어할 수 있음.
* 해킹이나 바이러스, 웜 등이 가지는 시그니처를 분석하여 HTTP Traffic, E-mail Traffic에 포함된 파일들의 해킹 진위와 감염여부를 파악할 수 있음.
* File Level 장비들은 일반적으로 IPS 또는 Gateway anti-virus 시스템 등이 해당되며 Packet reassemble, File inspection 함으로써 웜이나 바이러스 또는 콘텐츠의 완벽한 검증 및 방어가 가능.

DPI(Deep Packet Inspection)
* 기존의 Stateful Inspection에서 탐지 또는 방어하지 못하는 데이터 영역을 추출해낼 수 있는 최신의 기법
* Protocol, Port, IP address 등의 헤더 정보와 페이로드를 분석하여 탐지 패턴과의 해킹 진위여부를 분석할 수 있는 기능.
* DPI는 DoS, BOF, NOP attack, contents filtering에 대한 방어 기능을 제공하여 유해 트래픽이 대상 네트워크나 시스템에 접근하기 전에 패킷을 드롭시키는 Active Blocking 메커니즘을 가짐.
* Single Packet에서의 웜 방어 기능이 가능하나(decapsulation 기능이 없어서 패킷 one by one으로 검사 즉, 패킷을 쪼개서 보내면 감지하지 못함, DPI v1의 경우) 최근의 파일 단위의 웜은 방어가 불가능.
* DPI는 고속으로 패킷을 처리하는데 적합하나 해킹이나 웜 코드가 단편화되어 전송되는 것은 탐지 및 방어가 불가능.
* DPI는 Packet reassemble 기능을 가지고 있지 않으므로, 특정한 Evasion 공격에 대한 탐지 및 방어가 불가능.

ALSI(Application Level Stateful Inspection)
* DPI를 전처리한 후 Application의 응답을 체크하여 탐지 및 차단하는 시스템. 즉 통신 프로토콜을 트래킹할 수 있다는 의미.
* Packet reassemble, Normalization 기능을 가지고 small packet으로 공격되는 일련의 모든 공격에 대한 탐지 및 방어기능을 제공.
* ALSI는 DoS, BOF, NOP attack, contents filtering에 대한 방어 기능을 제공하여 유해 트래픽이 대상 네트워크나 시스템에 접근하기 전에 패킷을 드롭시키는 Active Blocking 메커니즘을 가짐.
* ALSI는 file, document, program같은 application-level의 객체 안의 페이로드를 reassemble하여 정확한 탐지 및 방어기능을 제공하며, 콘텐츠 기반 공격을 방어할 수 있는 기능을 제공.
* ALSI는 웜, 바이러스, 트로이 목마, XSS, injection 등 Fragment되어진 정보를 정확하게 탐지 및 방어 가능.

----------------------------------------------
  
## 211017
Single host에서 IP spoofing을 써서 가용성을 저해하는 패킷(ex. SYN flooding)을 계속 날리는 것을 DoS라고 해야 하나, DDoS라고 해야 하나? 피해자의 로컬 구간을 보고서만 판단해야 함. 즉, DDoS라고 생각할 수밖에 없음.  
  
IPS 구조. 캡처 엔진이 패킷을 캡처하면 IDS 엔진으로도, IPS 엔진으로도 캡처된 패킷을 보냄.  
 ![ㅇㅇ](https://user-images.githubusercontent.com/63287638/137671251-a8d3997d-9515-4384-a365-af47fb9be763.png)  
  
위 사진은 옛날 구조. 현재는 대부분의 회사의 제품에서 엔진이 사용자 레벨에 존재함(캡처 엔진이 패킷을 캡처하면 사용자 레벨로 패킷을 올림) 오버헤드가 너무 크기 때문이라고 함.  
  
Access Control  
1. 방화벽 기반의 해킹 방어. 단순한 포트 기반에서의 방어 방법으로서 일반적으로 열린 포트에 대해서는 Trust Traffic으로 간주하여 무조건 통과시키는 방식. Stateful Inspection 기능으로 업그레이드되었으나 실제 해킹의 진위를 판단할 수 없음.  
3가지 Action이 존재. Accept, Deny, Reject.  
  
2. 침입 탐지 시스템 기반의 해킹 방어. 침입 탐지 시스템이 방화벽을 통과하여 시도되는 해킹 공격들을 정밀하게 탐지하였으나 근본적인 방어기능의 부재로 방어 불가능. 침입 탐지 시스템의 Tunning의 어려움으로 인한 기본 설정값 사용. 이로 인해 오탐율 증대 및 방어 불가능이라는 결과가 나타날 수 있음.  
  
3. 방화벽 + 침입 탐지 시스템(interoperability). 방화벽과 침입탐지 시스템의 연동 방어 기능으로 방어시스템으로서의 큰 역할을 수행하였으나 one-way 공격(BOF, NOP)은 근본적으로 방어 불가능.  
  
4. IPS  
  
5. NPU(Network Process Unit). 기존의 범용 마이크로 프로세서가 특정한 응용 어플리케이션에서 더욱 나은 성능을 얻기 위해 특화된 구조. 네트워크 망의 고용량 대역폭과 유연성을 처리하기 위해 고속의 패킷 처리를 위하여 최적화된 마이크로 프로세서를 지칭. multi-processing, multi-threading 기법을 구현하여 wire-bandwidth를 지원하고 프로그램이 가능하도록 유연성과 확장성을 지원함으로 인해 방화벽, VPN, IPS 등의 보안제품 엔진으로 장착될 수 있는 특징을 가짐. header parsing, pattern matching, bit field manipulation, table look up packer ordering management, packet modification 등의 기능을 수행 가능.  

----------------------------------------------
  
## 211024
Generic 포괄적 진단: 악성 코드 파일들의 공통된 코드 영역을 진단하는 기법.
- 소스 코드 상에서 사용자 코드의 변화가 없거나 약간의 수정만 가하여 컴파일만 새롭게 한 악성 코드 변형들에 대해 탐지가 가능.
- 유사한 형태의 악성 코드 변형들이 지속적으로 제작되더라도 시그니처 업데이트 없이 탐지가 가능하다는 장점이 있음.

Heuristic(Suspicious Detection) 의심적 판단: 검사 대상 파일이 휴리스틱 시그니처와 비교를 통해 일반적으로 알려진 악성 코드와 얼마나 높은 유사도를 가지고 있는지를 판단하여 알려지지 않은 새로운 악성 코드를 탐지하는 기법.
- 일반적인 악성 코드가 가지고 있는, 특정 폴더에 파일 쓰기와 특정 레지스트리 부분에 키 생성과 같은 명령어들을 스캐닝 엔진에서 시그니처화하여 파일을 검사할 때 사용됨.
