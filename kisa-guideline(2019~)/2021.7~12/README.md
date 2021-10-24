# 7월
## fileless malware
#### 파일리스(fileless)란 단어가 의미하듯이 실행 파일과 다르게 희생자의 컴퓨터의 저장장치에 악성 파일을 저장하지 않는다는 의미이다. 그 대신 (powershell과 같은)정상적인 프로그램을 이용하여 바로 메모리(RAM)에 상주시킴으로써 컴퓨터를 감염시킨다. 따라서 일반적인 파일 스캔하는 방식으로는 악성코드를 찾아낼 수 없고, 동작 기반 탐지 도구를 사용하여 다계층 방어(공격 전, 중, 후)를 사용해야 한다고 한다.  과거에는 시스템 전원이 꺼지면(또는 재부팅 되면) 사라지는 일시적인 malware였다면, 최근에는 시스템 전원이 꺼져도 지속되는 persistent fileless malware이다.
#### 해커가 사용하는 기술에는 1. Reflective DLL injection 2. Memory exploits 3. Script-based techniques 4. WMI(Windows Management Instrumentation) persistence 등이 있다.
![Figure 1. Example of a fileless attack kill chain.](https://www.mcafee.com/enterprise/en-us/img/diagrams/fileless-attack-kill-chain.png)

* 참고: <https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=aepkoreanet&logNo=220934328454> , <https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=aepkoreanet&logNo=221583196950> , <>

## 제로데이(zero-day) vs 원데이(one-day) vs 올데이(olday)
#### 제로데이는 알려지지 않은 취약점이 공개되어 그 취약점을 이용한 공격을 당했지만, 현재 이에 대한 대응 방안이나 보안패치가 없는 상태를 말한다. 가장 까다로운 상태의 공격이고 APT 공격이 주로 감행된다.
#### 원데이는 취약점에 대한 패치가 발표되었지만 검증 및 여러 가지 이유 때문에 패치가 적용되지 않은 상태를 말한다. 패치가 발표되더라도 현실적인 이유로 바로 취약점 패치가 이루어지지 않기 때문에 발생하는 상태이다.
#### 올데이는 취약점 분석도 끝나고 오래전에 발표된 패치도 있으나, 패치가 아직 적용되지 않은 상태이다. 보안 담당자의 부재 및 보안 인식 부족으로 인해 주로 발생한다.

* 참고: <https://kimjs6873.tistory.com/8> , <https://whitehole.tistory.com/59>

## RTL(return to libc)
###### libc는 모든 C standard library들을 말한다. 따라서 RTL을 return to library와 혼용되어 쓰인다.
#### RTL을 알기 위해선 DEP 또는 NX bit를 먼저 알아야 한다. 공격자들이 RTL를 활용하여 우회하려는 방어기법들을 인텔에서는 XD(eXecute Disable) bit, AMD에서는 EVP(Enhanced Virus Protection), 윈도우에서는 DEP(Data Execution Prevention)이라 한다. 정확히 들여다보자면, DEP란 데이터 영역에서 코드가 실행되는 것을 막는 기법이다. 공격자가 힙 또는 스택 영역에 쉘 코드를 저장해서 실행하기 위해 해당 영역에 실행권한이 있어야 한다. 하지만 DEP를 적용된 경우 실행권한이 없어 스택에 쉘 코드를 삽입하더라도, 쉘 코드가 실행되지 않고 프로그램에 예외가 발생하여 종료가 된다. NX bit는 메모리에서 데이터 영역을 실행하는 것을 방지해주는 CPU 기능이다. NX 특성으로 지정된 모든 메모리 구역에서 데이터 저장만 가능하며 프로세서 명령어가 그곳에 상주하지 않음으로써 실행되지 않도록 만들어준다.
#### RTL은 메모리에 이미 적재되어 있는 공유 라이브러리를 이용해, 바이너리에 원하는 함수가 없어도 공유 라이브러리에서 원하는 함수를 사용하는 공격 기법이다. 위키피디아에 따르면 이러한 공격을 막을 수 있는 방법에는 ASCII armoring과 ASLR(Address Space Layout Randomization)이 있다. 첫 번째 방어법인 ASCII armoring이란 모든 시스템 라이브러리 주소들이 적어도 하나의 NULL 값(0x00)을 갖게 만드는 것이다. 만약 주소가 어느 시점에 null로 끝나는 문자열로 취급된다면, strcpy, strlen, sprintf와 같이 null을 만나면 끝나는 함수들이 libc 주소 끝에서 null을 만나서 처리를 중지하게 된다. 이로 인해 버퍼 오버플로우를 발생시켜도 원하는 동작을 하게끔 만들지는 못한다. 두 번째 방어법인 ASLR은 매 실행시마다 함수들의 메모리 위치가 포함된 데이터 영역을 랜덤화해서 원하는 함수들의 위치를 못 찾게 하는 것이다.

* 참고 : <https://ko.wikipedia.org/wiki/Return-to-libc_%EA%B3%B5%EA%B2%A9> , <https://lactea.kr/entry/bof-Return-to-Libc-RTL-%EA%B3%B5%EA%B2%A9-%EA%B8%B0%EB%B2%95> , <https://d4m0n.tistory.com/79> , <https://rninche01.tistory.com/entry/RTLReturn-To-Libc>

## RTL Chaining
###### 개념만 간단하게
#### RTL Chaining은 RTL의 연장선이다. RTL 기법에서는 하나의 함수만 호출하였다면, RTL Chaining에서는 여러 함수를 연계하여 호출하는 것을 말한다. RTL 기법에서 공격 Payload 중 Return Address가 들어가는 바로 다음 4 Byte에 "pop ret"와 같은 명령어의 주소를 넣어 스택의 포인터를 다음 함수로 위치시킨다. 이로써 Chaining이 가능해진다.

* 참고 : <https://d4m0n.tistory.com/80>

## ROP(Return Oriented Programming)
###### 개념만
#### NX bit와 ASLR 같은 메모리 보호 기법을 우회하기 위한 공격 기법이다. RTL, RTL Chaining, GOT(Global Offset Table) Overwrite기법을 활용하여 취약한 프로그램 내부의 기계어 코드들을 이용해 콜 스택을 제어함으로써 공격한다.

* 참고 : <https://d4m0n.tistory.com/84>

## SOP(Same-Origin Policy)와 CORS(Cross-Origin Resource Sharing)
#### SOP란 동일한 URL끼리만 API 등을 통한 데이터 접근이 가능하도록 하는 것이다. 정확하게 말하면 헤더의 Location에 있는 프로토콜, 호스트명, 포트가 같아야만 상호작용이 가능하게 하는 것이다. 이를 통해 한 출처에서 로드된 문서나 스크립트가 다른 출처의 자원과 상호작용하지 못하도록 제한함으로써 아무나 내 도메인 서버에 와서 자원을 가져갈 수 있는 것을 제한한다.
#### SOP를 통해 보안을 강화할 수는 있지만 프론트엔드와 백엔드 간의 상호작용이 필요한데, 둘의 도메인이 다를 경우 데이터를 주고받지 못하는 불편함이 발생한다. 프론트에서 HTTP 요청을 보냈을 때 따로 설정을 하지 않으면 에러가 나는데, 이를 해결해주는 것이 CORS이다. CORS는 추가 HTTP 헤더를 사용하여 브라우저가 실행중인 웹 애플리케이션(외부 도메인 서버)에 선택된 액세스 권한을 부여하도록 하는 것이다. 서버에서 받은 요청 응답에 특정 헤더 "Access-Control-Allow-Origin: \<url>'을 추가하면 웹 브라우저가 요청이 가능한 사이트로 인식하게 된다.

* 참고: <https://www.youtube.com/watch?v=bW31xiNB8Nc&t=521s> , <https://java119.tistory.com/67> , <https://velog.io/@jesop/SOP%EC%99%80-CORS> , <https://velog.io/@songsong2920/SOP-CORS> , <https://velog.io/@yejinh/CORS-4tk536f0db>

## CSP(Content Security Policy)
#### CSP는 페이지를 로드할 때 리소스를 제어하는데 사용된다. 허용된 인라인 스크립트나 css를 제외하고는 따로 삽입하지 못하게 함으로써 XSS나 CSRF, 클릭재킹 등의 공격을 막을 수 있다. 만약 인라인 스크립트를 사용한다면 nonce를 사용하여 일치하는 것에 대해서만 특정 스크립트 사용을 허용한다. CSP는 HTTP Content-Security-Policy 응답 헤더를 통해 설정할 수 있다.
###### meta tag 설정 방법으로는

    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; ">

###### php header 설정 방법으로는 

    <?php $headerCSP = "Content-Security-Policy:".
                        "default-src 'self';". // 기본은 자기 도메인만 허용
                        "connect-src 'self' ;". // ajax url은 자기 도메인만 허용
                        "script-src 'self' example.com code.jquery.com https://ssl.google-analytics.com ;". // 자기자신, 접근허용 도메인 설정
                        "style-src 'self' 'unsafe-inline';";
                        "report-uri https://example.com/csp_report.php;". // 보안 정책 오류 레포트 URL 지정(meta 태그에선 사용불가)
    header($headerCSP);
    ?>

출처: https://simjaejin.tistory.com/31 [심재진 블로그]

* 참고: <https://simjaejin.tistory.com/31> , <https://ko.wikipedia.org/wiki/%EC%BD%98%ED%85%90%EC%B8%A0_%EB%B3%B4%EC%95%88_%EC%A0%95%EC%B1%85> , <https://w01fgang.tistory.com/147> , <https://m.blog.naver.com/01075970528/221790130199> , <https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Content-Security-Policy>

## SSRF(Server Side Request Forgery)
###### CSRF가 Client를 거점(proxy)로 사용하는 것이라면 SSRF는 Server를 거점(proxy)로 사용하여 위조된 요청을 보내는 것이다.
#### 보통 웹 서버는 공개적으로 사용자가 접근이 가능하지만, 조직 내부의 서버는 웹 서버나 내부에 있는 컴퓨터를 제외하고는 직접적으로 접근할 수 없다. 이를 우회하고 내부 서버에 직접적으로 악성 행위를 하는 공격이 SSRF이다. SSRF는 취약한 서버(앞단, 웹서버 등)를 이용해 공격자가 내부 서버에 원하는 요청을 보낸다. 내부 서버는 요청이 신뢰하는 서버(즉, 웹 서버)로 부터 온 것이기 때문에 응답을 하고, 응답은 받은 웹 서버는 공격자에게 결과를 전달하게 된다. 
#### SSRF 취약점을 가지고 있는 서버라면, 공격자는 이를 통해 내부 서버들의 주소를 스캔하는 것이 가능하며 API key와 같은 중요 데이터를 유출시킬 수 있다. 또한 임의 코드 실행이나 임의 파일 쓰기 등의 허가받지 않은 행위도 가능하다. 예를 들어 사용자로부터 URI를 입력받고 해당 URI를 검색한 결과를 이미지 태그로 보여주는 사이트가 있다고 하자. 해당 URI를 일반적인 웹 사이트 주소인 https:\//어쩌구 가 아닌 127.0.0.1 등이나 file:\///etc/passwd로 요청하여 내부 서버를 스캔할 수 있는 것이다.
#### SSRF를 예방하기 위한 방법에는 세 가지 정도 있다. 1. 블랙 or 화이트 리스트 기반으로 입력값에 대한 검증을 수행한다. 2. 허용된 도메인과 URL에 대해서만 입력값을 받는다(다만 서비스에 제약이 생길 수 있다). 3. 요청을 처리하는 서버와 중요 정보가 있는 내부망을 분리시킨다.

* 참고: <https://guleum-zone.tistory.com/165> , <https://blog.lgcns.com/2503> , <https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=aepkoreanet&logNo=221567575013> , <https://cosyp.tistory.com/246>

## Cyber Threat Intelligence(CTI)
#### CTI 단어를 분석하자면, Threat위협은 동기와 공격 기회, 공격자의 역량이 모두 갖춰져 있는 것을 말한다. Intelligence는 다양한 채널에서 수집된 정보로부터 판단한 결과를 말한다. 여기서 정보는 Network log(Access log, IDS, IPS, SIEM 등에서의 정보), Endpoint log(EDR, 백신 등 단말에 설치되어 있는 에이전트), OSINT(Open Source INTelligence, 인터넷에 공개된 악성 도메인, IP, 침해사고 관련 침해지표 등)을 말한다. 이 정보들을 통해 Intelligence로 C&C 서버와 내부 인프라와의 연결 여부를 확인 가능하고, OSINT 및 MUMINT를 활용해 확보된 정보를 내부에 적용하여 보안 장비를 탐지하지 못하는 위협 식별 가능하고, 또한 공격그룹의 수법 분석이 가능하다.
#### CTI를 결국 한 마디로 표현하자면 사이버 공간의 유해 이벤트를 완화하는데 도움이 되는 위협 및 위협 요소에 대한 정보이다.

* 참고: <https://en.wikipedia.org/wiki/Cyber_threat_intelligence>

## 보조기억장치 HDD vs SSD
#### HDD는 원판을 플래터가 움직여 읽어낸다. 이 플래터가 움직이는 거리가 멀어질수록 정보를 읽고 쓰는 속도가 느려질 수밖에 없다. 반면 SSD는 플래시 메모리로, 물리적 제약이 없고 전자적으로 정보를 저장하기 때문에 어떤 지점의 정보에 접근하더라도 같은 속도를 보인다. 따라서 데이터를 읽고 쓰는 속도는 HDD가 더 느리다. 또한 SSD는 소음도 적고 소비 전력 역시 적으며 물리적 충격에도 강하다.
#### 보안과 관련해서도 HDD와 SSD의 차이가 있다. SSD는 wear leveling, 즉 하나의 cell에 대해 write 횟수가 많아지는 것을 막기 위해 내부적으로 컨트롤러가 알아서 다른 위치로 변경해주는 기능을 제공한다. 또한 over provisiong이라는 실제로 내부에 사용되는 공간을 조금 더 할당하는 기능도 있다. 마지막으로 trim 기능을 제공함으로써 데이터를 항상 삭제한다. 결과적으로 HDD보다 SSD가 데이터를 더 복구하기 힘들게 된다.

* 참고: <https://trendtalk.co.kr/%EC%A0%95%EB%B3%B4/hdd-ssd-%EC%B0%A8%EC%9D%B4-%EB%B0%8F-%EC%9E%A5%EB%8B%A8%EC%A0%90-%EB%B9%84%EA%B5%90/>

## row hammer
#### row hammer는 소프트웨어를 통해 하드웨어의 취약점을 이용할 수 있는 취약점이다. 기술이 발전함에 따라 DRAM의 cell 밀집도가 높아지면서, 한 row에 대해 반복적인 접근을 했을 때 인접한 행들에서 bit flip이 발생하는 취약점이다. 즉, 하나의 row에 반복적인 충격을 주었을 때 결함이 생기는 것이다. bit flip 현상은 다양한 원인으로 발생하는데, 우주선, 방사선, 전압저하뿐만 아니라 JS를 통해서도 가능하다.
#### row hammer를 이용해 다양한 공격이 가능한데, 특히 커널 권한 상승 공격이 가능한 것으로 밝혀졌다. 이를 막기 위해 DDR4 메모리를 제작했으나, 이 또한 변형된 row hammer을 통해 효과적으로 공격할 수 있음이 밝혀졌다고 한다.

* 참고: <https://blog.alyac.co.kr/574> , <https://www.dailysecu.com/news/articleView.html?idxno=9017>

## 헤더와 라이브러리
###### 헤더를 모아놓은 것이 라이브러리가 아니다. 
#### 헤더는 프로그래머가 이해할 수 있고 c/c++ 문법에 맞게 작성되어 있는 선언들의 집합을 말한다. 헤더 파일 내부에는 함수의 선언부가 있고, 라이브러리와 함께 사용되는 데이터 유형 및 삼수도 포함된다. 확장자는 .h이다.
#### 반면 라이브러리는 함수에 대한 정의가 구현되는 부분이다. 링크가 될 수 있도록 보통 컴파일된 형태인 오브젝트 코드(바이너리) 형태로 존재한다. 라이브러리의 확장자는 리눅스의 경우 .a, 윈도우의 경우 .lib이고 그 안에 들어간 오브젝트들의 확장자는 리눅스의 경우 .o, 윈도우의 경우 .obj이다. 라이브러리는 코드 재사용을 위해 전통적으로 사용되어 왔다.

* 참고: <https://coding-chobo.tistory.com/64> , <https://linuxism.ustd.ip.or.kr/344>

## 후킹(Hooking)
#### 후크란 간섭된 함수 호출, 이벤트, 메시지를 처리하는 코드를 말한다. 후킹은 갈고리처럼 특정 함수 코드를 가로채서 원하는 행위를 한 후 원래의 코드를 돌려주는 기법을 뜻한다. 후킹은 디버깅 및 기능 확장을 비롯한 다양한 목적으로 사용된다. 키보드 또는 마우스 이벤트 메시지가 응용 프로그램에 도달하기 전에 인터셉트하거나 운영 체제 호출을 가로채어 응용 프로그램이나 다른 구성 요소의 동작을 모니터하거나 기능을 수정하는 데 사용되기도 한다. 악의적으로는 크래킹 등을 위해 사용되기도 한다.
#### 후킹은 소프트웨어가 이미 실행중일 때 삽입되는게 보통이지만, 실행 전에 사용할 수도 있는 전략이다. 예를 들어 역어셈블러를 사용하여 모듈 내에서 함수의 시작점을 찾고, 로드된 라이브러리 내에서 원하는 함수를 실행하도록 주소를 변경하는 것이다. 이에 대한 대처 방법으로는 래퍼 라이브러리(Wrapper Library) 사용이 있다. 래퍼 라이브러리란 원본 라이브러리와 동일한 기능을 가지지만 함수 호출을 인터셉트하여 악의적인 행위가 수행되지 못하도록 막는 라이브러리를 말한다.

* 참고: <https://power-girl0-0.tistory.com/48> , <https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=on21life&logNo=221446844771>


## RAT(Remote Administration Tool)
#### RAT를 사용하면 원격에서 마치 직접적으로 기기에 접근하여 명령을 입력하거나 사용하는 것처럼 행동할 수 있다. RAT를 선의적인 목적으로 사용하면 원격 수리 기사가 직접 컴퓨터를 치료해주거나 할 수 있지만, 악의적인 목적으로 사용하면 내부 침입자가 직접 기기를 만지는 것처럼 행동할 수 있다. 민감한 정보를 유출하는 건 기본이고 시스템 크래시를 낼 수도 있다.

* 참고: <https://www.mcafee.com/blogs/consumer/what-is-rat/>

------------------------

# 8월
## mariadb vs mysql
#### mysql이 오라클에 인수되면서 기존 개발자가 나와서  호환되게 만든 것이 mariaDB이다. Miria DB는 MySQL의 소스코드를 그대로 가져와 개발한 것이므로 거의 모든 기능이 동일하다. 즉 서로간의 호환성이 보장 된다. 심지어 따로 설정을 변경하지 않는 경우 서비스 포트마저 3306으로 동일하다.
#### 성능면에서 mariadb가 더 낫다는 말이 많다. 다음은 일반적으로 말하는 mariadb의 장점이다.
1. MariaDB 개발이 좀 더 개방적이고 활발함
2. 빠르고 투명한 보안패치 릴리즈
3. 좀 더 다듬어진 기능들
4. 더 많은 스토리지 엔진
5. 나은 성능
6. Galera 액티브-액티브 마스터 클러스터링
7. 오라클 관리하의 불확실성
8. 유명세가 높아지고 있음
9. 호환성과 쉬운 마이그레이션
10. 15년 이후에는 마이그레이션이 어려울 수 있음

* 참고: <https://bongjacy.tistory.com/entry/MariaDB-Mysql-%EB%91%98-%EC%A4%91%EC%97%90-%EB%AC%B4%EC%97%87%EC%9D%84-%EC%84%A4%EC%B9%98%ED%95%98%EC%A7%80> , <https://dololak.tistory.com/766>

## API와 SDK
#### API(Application Programming Interface)는 응용프로그램에서 데이터를 주고 받기 위한 방법이다. 운영체제가 응용프로그램을 위해 제공하는 함수의 집합을 포괄하여 부르는 의미이다. 종류에는 제3자에게 노출되지 않는 private API, 모두에게 공개되는 public API, 기업이 데이터 공유에 동의하는 특정인만 사용 가능한 partnet API가 있다.
#### SKD(Software Development Kit)은 프로그래머들을 위해 제공하는 개발 도구이다. SDK에는 개발 도구 프로그램, 디버깅 프로그램, 문서, API 등이 있다. 원래는 MS에서 제공하는 윈도우용 프로그램 개발킷을 의미했으나 현재는 API와 거의 같은 뜻으로 쓰인다. 종류에는 안드로이드 SDK, JDK, IOS SDK, Windows SDK 등이 있다.

## EL injection(Expression Language)
EL injection을 알아보기 전에 그 공격에서 자주 사용하는 코드가 어떻게 이루어져 있는지 알아본다.  
<https://github.com/mochang2/various-information/blob/main/java%20compile%20setting%20in%20Ubuntu.md> 에 들어가면 실습 세팅을 할 수 있다.

        "".getClass().forName("java.lang.Runtime").getMethods()[6].invoke("".getClass().forName("java.lang.Runtime")).exec("ls")

가 공격 인자로 자주 들어간다. 위 공격을 메소드 단위로 쪼개 보았다. 결과만 먼저 쓰자면 큰 의미 없이 exec 이후가 실행된다는 것만 알면 되겠다.  
![source code](https://user-images.githubusercontent.com/63287638/129444916-bde767fa-06e1-4de8-900b-4372220e27f4.PNG)
를 실행하면 

        class java.lang.String
        class java.lang.Runtime // Class.forName()은 사실 자바 리플렉션 API의 일부. 자바 리플렉션 API란
        // 구체적인 클래스의 타입을 알지 못해도 클래스의 변수 및 메소드 등에 접근하게 해주는 API(동적 바인딩)
        Ljava.lang.reflect.Method;@65b54208
        31
        public static java.lang.Runtime java.lang.Runtime.getRuntime()  // 여기까지가 위 공격에서 invoke 전까지를 의미

라는 결과가 나오고  
![01](https://user-images.githubusercontent.com/63287638/129444917-4af329b5-ab2f-4a3a-8391-2d958e850a6b.PNG)  
위와 같이 현재 디렉터리에 abc.txt가 생성이 된다. 즉 exec에 인자로 들어간 것이 쉘에서 실행되는 것이다.  
  
#### EL은 JSP의 기본 문법을 보완하고 수치 연산, JAVA 클래스, 메소드 호출 기능 등을 제공한다. 또한 static 메소드를 호출할 수도 있는데 JSP에서는 주로 서블릿 보관소(JspContext, ServletRequest, HttpSession, ServletContext)에서 값을 꺼낼 때 사용한다. ${expr}와 같은 형식을 가지고 있다.
#### 서버측 코드(SS code: ASP, JSP, PHP 등) 인젝션은 응용 프로그램이 사용자가 제어할 수 있는 데이터를, 코드 인터프리터에 의해 동적으로 평가되는 문자열에 통합할 때 발생한다. 이때 유효성 검사를 수행하지 않으면 공격자가 서버에서 실행할 임의 코드를 주입할 수 있다. 이러한 공격 중 하나가 EL injection이다. 사용자의 파라미터를 조작함으로써 EL 인터프리터에서 동작할 때 사용자가 원하는 기능을 수행하게끔 한다. https://www.notion.so/5-Nexus-Repo-Manager-CVE-2020-10199-49bc68494bda4b9f9e8d385bb48b05b6 에서 수행해본 공격과 같은 경우 /tmp 디렉터리(world writable dir)에 공격 파일을 심어놓을 수도 있다.
#### EL injection은 현재 Spring JSP 태그를 잘못 사용할 때 자주 발생한다고 한다. CVE-2020-10199 취약점에서는 POST 메소드로 /service/rest/beta/repositories/go/group, /service/rest/beta/repositories/bower/group, or /service/rest/beta/repositories/docker/group 과 같은 URI에 JSON 형식으로 memberNames 파라미터를 조작함으로써 EL injection을 성공시킨다.

## 2 tier vs 3 tier
#### 2 tier 구조는 클라이언트에서 Buiness Logic을 작성하고 데이터베이스에 저장하여 사용하는 형태를 말한다. Client/Server 구조로 사용자를 위한 인터페이스 프로그램이 Client 측에 위치하고 DBMS의 서비스가 서버로서 존재한다. Client는 이러한 인터페이스로 데이터를 입력하고 불러온다.
#### 이러한 구조의 장점이 개발이 편리하고 개발비용이 저렴하다는 데에 있다. 또한 변화에 대한 위헙부담을 최소화한다는 장점도 있다. 단점은 사용자수 증가에 따른 네트워크 트래픽의 병목현상으로 성능이 현저하게 저하한다는 것이다. 확장성이 적으며 유지관리의 어려움도 있다. 또한 Application 로직이 프레젠테이션 로직에 포함되어 있어 재사용이 어려우며 보안에 취약하다.
#### 3 tier 구조는 Client - Middleware - Server와 같은 구조를 가지고 있다. Client는 Middleware로 메시지를 주고 받으면서 데이터베이스에 저장한다. Middleware에 대한 구현은 Transaction Processing Monitor, Message Server, Application Server 등 여러가지 방법으로 구축될 수 있다.
#### 이러한 구조의 장점은 Application의 분산으로 성능 향상이 가능하며, 서버 기종이나 DB에 관계없이 확장성이 용이하다는 것이다. 또한 Application 집중관리로 유지보수와 재사용이 용이하며, 2 Phase commit으로 장애나 공격에 대한 대처가 용이하다. 반면 단점으로는 개발환경이 복잡하고 구현이 어렵다는 것이다. 또한 1계층이 더 추가되었으므로 개발 비용이 늘어난다는 단점이 있다.

* 참고: <http://blog.jserver.kr/go/5201> , <https://mkil.tistory.com/53>

## 딥페이크(deepfake)
#### 인공지능을 기반으로 활용한 인간 이미지 합성 기술. 기존에 있던 인물의 얼굴이나, 특정한 부위를 CG처럼 합성한 영상편집물을 총칭함. 합성하려는 인물의 얼굴이 주로 나오는 고화질의 동영상을 통해 딥러닝하여, 대상이 되는 동영상을 프레임 단위로 합성시키는 것. 병렬연산장치의 성능에 다라 속도와 품질이 결정됨. 다만, 방해물들이 있을 경우 그냥 원본 얼굴만 보여주기도 하거나, 자칫 충분한 딥러닝을 하지 못할 경우에는 불쾌한 골짜기 현상이 일어나기도 함.
#### 유명인들은 온라인에 공개된 리소스의 양이 당연히 많으므로 영상 합성이 용이하기 때문에 딥페이크 포르노의 탄생에 이용됨. 또한 정치적 목적으로 딥페이크 영상을 만들어 정치인의 말조차 가짜로 만들어내어 정치적 공세를 가하는 경우도 존재함.

* 참고: <https://namu.wiki/w/%EB%94%A5%ED%8E%98%EC%9D%B4%ED%81%AC>

------------------------

# 9월
## FIDO(Fast IDentity Online)
###### https://www.notion.so/FIDO-62d6ee5177ba49adac3a233f48dbdefe 여기에 더욱 자세히 정리해놨다.
#### 아이디 / 패스워드 방식이 아닌 지문, 홍채, 얼굴, 목소리 등 생체 정보를 활용한 인증 방식이다. 인증 프로토콜과 인증 수단을 분리하여 보안을 높이고 안정성을 확보했다.
#### 인증 프로토콜로는 UAF(Universal Authentication Framework), U2F(Universal 2nd Factor), CTAP(Client-to-Authenticator Protocol)이 있다. UAF는 사용자 디바이스 인증기법을 온라인 서비스와 연동해서 사용자를 인증하는 기술이다. U2F는 기존 패스워드를 사용하는 온라인 서비스에서 2번째 인증요소로 강한 인증을 사용자 로그인 시에 추가하는 기술이다. CTAP은 외부장치를 이용한 인증방식에 사용한다. 모바일 단말기, USB, NFC, BT와 같은 것을 이용하여 운영체제나 웹 브라우저 등과 인증자 연동을 구성한다.
#### 다음과 같은 것들로 구성되어 있다.
- 서버: 인증장치에 대한 정책을 설정하고 사용자의 공개키를 등록, 관리 및 검증
- 클라이언트: 서버의 정책에 따라 인증자를 필터링하고 ASM과 RP 클라이언트 간의 중계 역할
- ASM: Authenticator Specific Module의 약자로 FIDO 클라이언트의 요청을 인증자로 전달하고 인증자에게 생성된 응답값을 FIDO 클라이언트로 전달하는 중계역할
- 인증자: 생체 인증 등으로 사용자를 사용자 단말에서 로컬 인증하고 서버에서의 원격 인증을 위한 비대칭키 쌍을 생성하고 개인키를 이용해 전자서명을 수행

* 참고: <https://m.blog.naver.com/tmaxhq/221519925930> , <https://pongdang-pooh.tistory.com/7> , <https://www.fsec.or.kr/common/proc/fsec/bbs/42/fileDownLoad/1206.do> , <https://stackframe.tistory.com/42>

## NFC(Near Field Communication)
###### https://www.notion.so/NFC-417ea43a7c03441ebd32b8532f4b361c 여기에 더욱 자세히 정리해놨다.
#### 태깅을 통해 전자기기끼리 근거리 무선 통신을 할 수 있게 하는 기술이다. 양방향 통신이기에 태그(칩)와 리더 역할을 유동적으로 변경시킬 수 있다는 특징이 있다.
#### 동작 모드에는 3가지가 있다. 카드 모드, RFID 리더 모드, P2P 모드이다. 카드 모드는 비접촉식 스마트카드 기술 및 보안으로 교통카드와 할인쿠폰 등 다양한 모바일 결제 방식 제공한다. 외부 NFC 기기가 단말기로 무선 접속할 수 있게 수신 대기 상태로 동작한다. RFID리더모드는 단말 기기 뿐만 아니라 RFID 태그가 부착되어 있는 스마트 포스터 등을 이용한 웹사이트 연결 및 정보 획득한다. P2P모드: 양방향 통신 모드. 스마트폰과 PC 및 가전제품 기기 간 데이터 송수신 및 파일공유한다. NFC 카드 기능을 포함한 읽기/쓰기, 데이터 주고 받기 등의 NFC의 모든 기능을 사용 가능하다.
#### NFC는 RFID에 포함된다고 보면 된다. 하지만 약간의 차이가 있다. RFID는 사용 주파수와 통신 방식에 따라 장거리에서도 사용 가능하지만, NFC는 13.56MHz 주파수로 고정되어 있기 때문에 최대 10cm로 거리가 짧다. 또한 RFID는 리더와 태그가 따로 구성되지만, NFC는 한 NFC 장치가 리더와 태그 기능을 모두 할 수 있다.
#### 다음과 같은 곳에 사용할 수 있다.
- 전자지불 서비스 및 고속도로 통행료 지불
- 박물관의 전시물 안내 서비스
- 도어락 기능과 경보 기능 설정 및 해제
- 핸드폰이 매너모드로 전환하거나, Wi-Fi를 켜거나, 취침 모드로 들어가는 등의 지정한 동작을 수행
- 다른 NFC 장치 간에 정보 전송. 블루투스처럼 데이터 읽기와 쓰기 기능을 모두 사용할 수 있지만 블루투스처럼 기기 간 연결이나 페어링을 필요로 하지는 않음(즉, 초기 인증 과정이 필요 없음)

* 참고: <https://www.kisa.or.kr/uploadfile/201306/201306101747434530.pdf> , <https://www.sony.co.kr/electronics/support/articles/00022001> , <https://m.blog.naver.com/pst8627/221633598688> , <https://blog.naver.com/PostView.nhn?blogId=ndb796&logNo=221087572139> , <https://www.nfcw.com/2020/02/14/365743/st-explains-how-nfc-can-be-combined-with-blockchain-technology-to-deliver-smarter-supply-chains/>

## DID(Decentralized IDentifier)
###### https://www.notion.so/DID-12f9b231ec4e4a34953fbf7cc96d004a 여기에 더욱 자세히 정리해놨다.
#### 개인 블록체인 지갑에 개인정보를 담고 있다가, 필요한 때에 필요한 만큼만 보여줌으로써 나를 증명하는 것. 예를 들면 성인인증을 할 때, 생년월일까지 전부 공개하는 것이 아니라 만 19세가 넘는 것만 증명하는 것을 말한다. 블록체인으로 신원을 증명하기 때문에 서비스 기업이나 기관에 개인정보를 모두 제공할 필요가 없으며 신원 정보 주인이 정보 제공 여부를 통제할 수 있다. 또한 기존 개인정보 관리 방식과는 다르게 개인정보 소유자인 개인이 스스로 정보를 관리(수정)하고 통제할 수 있다. 현재는 금결원에서 사원증, PASS 모바일 운전면허 확인 서비스 등에서 사용되고 있다.
#### 다음과 같은 순서로 동작한다. (1)서비스 제공자가 사용자에게 신원 정보 인증 요청 (2)사용자가 신원정보발행자(인증기관 등)에게 신원 정보 발행 요청 (3)신원정보발행자가 분산 ID저장소에 사용자의 신원 정보를 검증할 수 있는 서명된 ID정보를 등록 (4)신원정보발행자가 사용자에게 신원정보 발행 및 사용자는 신원정보발행자가 서명한 내용에 대해 Counter-sign을 하여 DIDs(Key) — DID Document(Value) 생성 (5)사용자는 서비스 제공자에게 신원 정보를 전달, 이때 신원정보발행자에게 받은 신원 정보 전체중 인증에 필요한 일부만을 선택한 신원 정보를 서비스 제공자에게 전달 (6)서비스 제공자는 DIDs를 통해 분산 ID저장소에 저장된 DID Document를 검증하여 신원 확인을 완료
##### 크게 3가지 정도의 구조가 있다. 첫 번째는 Sovrin이다. Sovrin은 자기주권신원 형태의 분산신원증명 플랫폼으로 서비스 제공자에 의해 인증된 참여자들만 참여 가능한 허가형 블록체인(Permissioned blockchain)상에 구현된 오픈소스 프로젝트이다. 일반 사용자들이 단말 클라이언트를 통해 자신의 신원정보(식별자, 공개키, 메타데이터)를 관리하고 이 정보를 신뢰하는 기관들(은행, 대학, 정부 등)의 합의에 기반하여 블록체인 데이터베이스에 기록한다. 사용자는 여러 키를 사용하여 복수의 식별자-속성 조합의 신원정보를 사용할 수 있다.
##### 두 번째는 uPort이다. uPort는 분산된 신뢰신원 형태의 분산신원증명 프레임워크로 이더리움 블록체인 상에서 스마트 컨트랙트로 구현된 오픈소스 프로젝트이다. 사용자는 컨트롤러(Controller) 컨트랙트로 키를 초기 등록하고 이후 컨트롤러 컨트랙트를 참조하는 프록시(Proxy) 컨트랙트들을 생성해 복수의 식별자-속성 조합의 신원정보를 관리 가능하다.
##### 세 번째는 ShoCard이다. ShoCard는 분산된 신뢰 신원 형태이다. 신뢰 기관이 발급한 신원정보를 암호학적 해시함수형태로 비트코인 블록체인에 저장하여 누구든지 검증 가능한 신원 증명 서비스를 제공한다. 블록체인에 기록되는 신원 정보는 최초에 신뢰하는 제3자인 인증자(Certifier)에 의해 기록되지만 기록된 신원 정보는 누구든지 쉽게 검증 가능하다.

* 참고: <https://www.markany.com/kr/portfolio-posts/did-블록체인-기반-분산-신원증명-기술/> , <https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002660601> , <https://m.blog.naver.com/smartnari/222073016643>

------------------------

# 10월
## RTLO Attack(Right-to-Left-Override)
#### RTLO Attack을 알기 위해선 RTL 인코딩을 알아야 한다. 한국어, 영어, 일본어 등은 왼쪽에서부터 오른쪽으로 읽지만, 아랍어나 히브리어 등은 반대로 읽는다. 기본적으로 윈도우 운영체제 등은 LTR(Left-to-Right)를 지원하지만 "\[U+202e\]"를 쓰면 RTL 인코딩을 한다는 의미이다. 예를 들어 'mytextfile.txt'이란 파일이 있다고 하자. 'mytext\[U+202e\]file.txt' 이렇게 파일 이름을 만들면 유티코드 캐릭터가 반전이 되어서 'mytexttxt.elif'라고 표현된다.
#### RTLO Attack은 이러한 인코딩 방법을 이용한 피싱 공격이다. 사람들은 exe 파일 등은 악성 파일일 수 있다는 인식이 강한 반면 txt 파일은 악성 파일일 수 있다는 가능성을 생각하지 않는 점을 이용한다. 즉, 실제로는 exe 파일을 txt 파일처럼 보이게끔 하는 것이다. 'mytext\[U+202e\]txt.exe' 이런 식으로 사용하면 'mytextexe.txt'라는 이름으로 보여서 사람들은 경계심을 풀게 되고 쉽게 다운받을 수 있게 된다.
#### 안티바이러스를 사용하는 것은 이러한 공격을 막는데 매우 효과적이다. 하지만 안티바이러스 무용론이 제기되듯 언제든지 수많은 악성코드가 공격이 가능한 취약점을 노릴 수 있다. 특히 zip 파일 안에 숨기는 RTLO 악성 파일은 잡기 힘들 수도 있기에 언제든지 주의를 기울일 필요가 있다. 또한 윈도우의 경우 확장자 표시 기능을 이용해서 항상 실제 확장자를 확인할 필요가 있다.

* 참고: <https://cybriant.com/what-is-a-right-to-left-override-attack/> , <https://attack.mitre.org/techniques/T1036/002/>

## MSI 확장자
#### MSI 확장자는 MicroSoft Installer의 약자로 Windows Installer 패키지 파일의 확장자로 쓰인다. 타사 설치 프로그램 도구뿐만 아니라 Windows Update에서 업데이트를 설치할 때 일부 Windows 버전에서 사용된다. 이 파일 형식은 내부에 데이터베이스 테이블로 구성된 설치 지침, 실행할 애플리케이션 파일을 포함하고 있다.
#### 악성코드가 MSI 포맷으로 유포되는 사례가 많다. MSI 확장자를 통해 확장자 검사만 하는 기존 보안제품을 우회할 수 있기 때문이다.

* 참고: <https://ko.eyewated.com/msi-%ED%8C%8C%EC%9D%BC%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9E%85%EB%8B%88%EA%B9%8C/> , <https://zdnet.co.kr/view/?no=20180223222434>

## AMSI(AntiMalware Scan Interface)
#### AMSI는 기본 제공 스크립팅 서비스를 심층적으로 검사할 수 있게 해주는 윈도우 구성 요소로, 응용 프로그램 및 서비스가 컴퓨터에 있는 모든 멀웨어 방지 제품과 통합될 수 있도록 하는 다양한 인터페이스 표준이다. AMSI는 최종 사용자와 해당 데이터, 응용 프로그램 및 워크 로드에 대한 향상된 멀웨어 보호 기능을 제공한다. AMSI와 통합되는 Windows 구성 요소로는 UAC(User Account Control), Powershell, Windows 스크립트 호스트(wscript.exe 등), JS 및 VBScript, Office VBA 매크로 등이 있다.
#### AMSI는 다음 예시와 같이 동작한다. 참고로 다음 예시는 Kaspersky Endpoint Security에 관한 것이다.
![](https://user-images.githubusercontent.com/63287638/135786682-a2c3d988-6fcf-4bfc-94a5-c4e05afad00d.PNG)  
#### AMSI를 우회하는 기법들에는 Powershell 다운그레이드 기법, 시그니처 탐지 우회 기법, hooking, memory patching(AMSI API를 패치해서 항상 정상 프로그램임을 나타내는 값을 리턴), Registry Key Modification 등이 있다.

* 참고: <https://docs.microsoft.com/ko-kr/windows/win32/amsi/antimalware-scan-interface-portal> , <https://support.kaspersky.com/KESWin/11.5.0/ko-KR/173854.htm>

## AVT(Advanced Volatile Threat)
#### APT가 장기간, 천천히 특정 대상을 타겟팅하여 공격해온 형태라면, AVT는 잠시 동안의 공격이다. APT가 대두되기 이전에 행해졌던 사이버 공격들을 APT와 비교하기 위해 이러한 이름을 붙인 것으로 보인다.

* 참고: <https://www.csoonline.com/article/2132995/advanced-volatile-threat--new-name-for-old-malware-technique-.html>

## LotL(Living Off the Land) attack
#### Living off the land는 자연에서 먹이를 찾아다니고, 사냥하고 자라면서 살아남는다는 것을 의미한다. LotL 공격은은 OS 요소나 소프트웨어를 타겟삼아 찾아다니고, 그것들을 이용하여 목표를 달성한다. 즉, 악성 행위를 하기 위해 희생자 측에서 허가된 소프트웨어나 기능을 이용한다는 것이다. LotL이 자주 사용하는 소프트웨어는 powershell, WMI(Windows Management Instrumentation), PsExec, Mimikatz 등이 있다.
#### LotL을 막기 위해서는 동적 분석이 필요하다고 한다. 따라서 이를 막는 도구로는 EDR 솔루션이나 threat hunting 등이 있다고 한다.

* 참고: <https://encyclopedia.kaspersky.com/glossary/lotl-living-off-the-land/>

## stub
#### crypter 또는 packer는 시그니처 기반 탐지를 우회하기 위해 사용된다. 이 때 공격 대상에서 암호화를 해제하거나, 패킹을 해제하기 위해 Anti-Virus에 탐지되지 않는 stub을 함께 악성 파일 안에 위치시킨다. 기본적으로 crypter나 packer는 malware를 evasion시키는 작업을 한 뒤 파일의 맨 아래에 stub을 배치시킨다. 암호화나 패킹 이전에는 entry point가 main 함수였다면, 이후에는 entry point가 stub이 되면서 stub이 가장 먼저 실행된다.
#### crypter는 scantime에 malware가 Anti-Virus의 정적분석으로부터 탐지되지 않도록 만든다. 만약 malware가 실행되면 stub이 malware의 이진 데이터를 복호화하고 메모리에 malware를 올린다. 실행 후(runtime이 지난 후) stub은 다시 malware를 암호화시켜서 저장하게 한다.
#### 참고로 crypter와 packer의 차이는 섹션을 암호화하느냐, 압축하느냐 등에 따라 여러 가지가 있겠지만, stub을 기준으로 볼 때는 용량에서의 차이가 있다. crypter는 stub을 추가함으로써 용량이 증가하지만, packer는 압축을 하므로 stub을 추가해도 기존 파일보다 용량이 더 작다.

* 참고: <https://security.stackexchange.com/questions/42289/what-is-a-stub> , <https://www.trendmicro.com/vinfo/ph/security/definition/Crypter>

## UPX(Ultimate Packer for eXecutables)
#### 여러 OS에서 수많은 파일 포맷을 지원하는 오픈소스 실행 파일 압축 프로그램이다. GNU 라이센스를 가지고 있다. 압축은 UCL이라는 이름의 알고리즘을 사용하며, 압축 해제 시에는 in-place 테크닉, 임시 파일로의 해제, 이렇게 두 개의 메커니즘을 지원한다.
#### UPX는 zip 파일 등과 비교할 때보다 높은 비율의 압축률을 자랑하고, 빠른 특징을 가지고 있다. 또한 in-place 테크닉을 인해 메모리 오버헤드가 적으며 c++ 기반으로 만들어져 portable하며 class layout으로 인해 extendable하다.

* 참고: <https://ko.wikipedia.org/wiki/UPX> , <https://upx.github.io/>

## 코드 가상화
#### 난독화와 더불어 안티 리버싱 기술 중 하나로, Anti-Virus evasion 기술로도 사용된다. 코드 가상화는 가상 CPU를 활용하여 컴파일 과정에서 보통의 PC에 탑재된 intel CPU용 어셈블리가 아닌, 가상화 CPU용 어셈블리로 코드를 바꾼다. 이것은 기존의 역공학 도구로 코드복원이 불가능하다고 한다. 이렇게 가상화된 코드는 원래의 CPU에서는 실행할 수 없고, 가상 CPU에서만 실행이 가능하다. 대신 가상 CPU가 소프트웨어적으로 구현되어, 사용자는 실제 CPU를 통해 가상화 CPU를 실행하고 가상화 CPU를 통해 가상화된 코드를 해석한다.
![가상머신구조](https://user-images.githubusercontent.com/63287638/136730395-4fd75308-b1d8-47dc-92c3-2dbc52983e95.PNG)  
#### 바이트 코드가 실행되는 가상 머신은 일반적으로 위와 같은 구조를 가진다. Initializer는 기존의 레지스터 및 플래그 값을 스택에 저장하고 가상환경에 필요한 스택과 레지스터를 초기화하는 역할을 한다. 또한 가상환경 구동에 사용될 구조체 및 변수를 초기화 한다. Initializer로 전달되는 opcode는 일반적으로 암호화되어 있거나 압축되어 있으므로 이를 복호화하고 압축 해제하는 작업 또한 이 단계에서 이루어진다.
#### Dispatcher 단계에서는 해석된 opcode를 기반으로 각가의 기능을 수행하는 handler로 코드 흐름을 분기하고 각각의 handler에서는 가상의 instruction을 구현한다.

* 참고: <https://blogsabo.ahnlab.com/2158> , <http://www.igloosec.co.kr/ig/BLOG_%EB%82%9C%EB%8F%85%ED%99%94%EC%99%80%20%EC%BD%94%EB%93%9C%20%EA%B0%80%EC%83%81%ED%99%94%20-%20%EC%95%85%EC%84%B1%EC%BD%94%EB%93%9C%EC%97%90%20%EC%82%AC%EC%9A%A9%EB%90%98%EB%8A%94%20%EB%B0%94%EC%9D%B4%EB%84%88%EB%A6%AC%20%EB%B3%B4%ED%98%B8%EA%B8%B0%EB%B2%95%20?searchItem=&searchWord=&bbsCateId=1&gotoPage=1>

## LLVM(Low Level Virtual Machine)
#### 한 마디로 CPU 명령어를 가상화시키는 똑똑한 컴퓨터라고도 할 수 있다. LLVM은 원래 가상 머신을 가리키는 용어였으나 현재는 프로젝트의 이름으로 사용되고 있다. LLVM은 컴파일러의 기반구조로 프로그램을 컴파일 타임, 링크 타임, 런 타임 상황에서 프로그램의 작성 언어에 상관없이 최적화를 쉽게 구현할 수 있도록 구성되어 있다. LLVM은 언어와 구조로부터 독립적이며, 언어 모듈과 시스템을 위한 코드 생성 부의 사이에 위치한다.

* 참고: <https://ko.wikipedia.org/wiki/LLVM> , <https://llvm.org/>

## 프로세스 도플갱잉(process doppleganging)
#### 프로세스 할로잉과 비슷한 방법이다. 정상 프로세스의 새로운 인스턴스를 생성해서 그 인스턴스에서 악성 코드를 수행하도록 하고, 생성을 롤백함으로써 파일을 디스크에 쓰이지 않아도 악성행위가 발생한다(디스크에 실제 변경을 적용하지 않고 실행 파일을 변경시킴). 파일 기반 탐지 백신의 대부분을 우회할 수 있고 NTFS의 Transaction(정보 처리) 기능을 이용한다는 특징이 있다. 참고로 NTFS의 Transaction 기능은 Windows Vista에서 처음 도입되었으며, 파일 작업이 트랜잭션 내에서 수행하게 하는 기능이다. 이를 이용하면 파일 업데이트를 안전하게 처리되어 업데이트 프로세스 중에 오류가 발생하는 경우 파일 무결성이 보장된다.
#### 보안뉴스에서 엔실로라는 사람과의 인터뷰에 따르면 “NTFS에서의 정보 처리(transaction)가 이뤄지는 상황에서 정상 파일을 덮어쓰기 하는 거라고 볼 수 있습니다. 그런 후 조작된 파일로부터 섹션을 하나 생성하고, 거기서부터 프로세스를 또 생성합니다. 현재까지 저희가 확인한 보안 제품 중에서는 처리 과정(transaction) 중 파일을 검사하는 게 가능한 솔루션은 없었습니다." 이러한 공격 기법이라고 한다.

* 참고: <https://www.boannews.com/media/view.asp?idx=58499> , <https://ichi.pro/ko/peuloseseu-dopeulgaeng-ing-114675046643215> , <https://kali-km.tistory.com/entry/Process-Doppelganging-1>

## 프로세스 할로잉(process hollowing) 또는 PE 이미지 스위칭
#### hollow는 속이 비어 있다는 뜻이다. 즉, 정상 프로세스의 속을 비우고 새로운 인스턴스를 생성해 정상 코드를 악성 코드와 바꿔치는 식으로 코드를 주입하는 기법이다(대상 프로세스의 이미지를 언매핑하고 자신의 이미지를 매핑하는 기술). 프로세스를 suspend 상태로 실행하고 injection 완료 시 실행 상태로 변경함으로써 공격이 이루어진다. 악성코드를 정상 프로세스로 속일 수 있으며 fileless 공격으로 응용이 가능한 특징을 가지고 있다. 만약 할로잉된 프로세스를 확인하고자 한다면 외관상으로는 정상적인 프로세스와 동일하기 때문에 메모리를 덤프하여 비교하거나 디버거로 분석해야 한다.

* 참고: <https://whitecherryblossom.tistory.com/36>

## 도메인 생성 알고리즘(Domain Generation Algorithm, DGA)
#### DGA란 다양한 도메인 이름을 주기적으로 그리고 동적으로 생성하는 알고리즘이다. 주로 악성코드에서 C&C IP 등의 특정 도메인에서 명령 등을 받아올 때 해당 도메인을 동적으로 변경해줌으로써 접속 방지 기법을 우회하기 위해 사용된다. DGA를 사용하면 malware가 하루에도 수만 개의 도메인을 생성할 수 있다. 이렇게 생성된 도메인들을 등록된 도메인처럼 가장하는 곳에 사용하어 탐지를 회피하는 것이다. DGA가 감지되면 하나 이상의 시스템이 DGA 기반 malware에 감염되어 봇넷이 됐다고 판단할 수 있다.
#### DGA는 시그니처 기반 탐지 시스템으로는 탐지하기 어렵다. DGA를 탐지하기 위해서는 DPI 엔진을 통해 DNS 애플리케이션 감지를 수행하고 도메인 이름을 추출함으로써 의심되는 도메인의 등록 상태를 확인하고, 네트워크 트래픽 검사와 상호 연결해야 한다.

* 참고: <https://stellarcyber.ai/ko/what-are-dgas/>

## UAC(User Account Control) 권한 상승 판단 조건
#### UAC란 윈도우에서 제공하는 보안 기능으로, 권한이 없는 프로그램이나 악성코드가 바로 실행되지 않도록 사용자에게 실행여부를 묻는 것이다. 권한이 없는 프로그램의 자동 설치를 차단하고 시스템 설정을 실수로 변경하지 않도록 방지한다.  
![winenv-uac-image1](https://user-images.githubusercontent.com/63287638/138598670-2594c827-5505-4742-8011-ecef99b147ca.png)  
출처: <https://docs.microsoft.com/ko-kr/windows/win32/uxguide/winenv-uac>  
#### UAC에서 권한 상승 판단 조건은 크게 3가지가 있다. 첫째는 실행파일에서 \<autoElevate>true\<\/autoElevate> 속성이 있는지 확인하는 것이다. autoElevate는 키의 일종으로 true면 자동 권한 상승 속성이 삽입되어 있다는 뜻이다. 둘째는 전자 서명이 유효한지 확인하는 것이다. 셋째는 신뢰할 수 있는 폴더에서 실행되었는지 확인하는 것이다. 만약 이 세 가지 조건이 만족되지 않는다면 UAC 알람 설정 수준에 따라 사용자에게 권한을 상승할지 알림이 발생한다. 하지만 이는 반대로 공격자가 어떤 방식으로든 이 조건을 우회할 수 있다면 사용자에게 권한 상승 여부를 물어보지 않고도 권한을 상승할 수 있다는 말이다. 

* 참고: <https://tech.somma.kr/UACbypass/#11-autoelevate%EA%B0%80-%EC%84%A4%EC%A0%95%EB%90%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%EA%B3%BC-%ED%8F%B4%EB%8D%94-%EA%B3%B5%EB%B0%B1%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-ais-%EC%B2%B4%ED%81%AC-%EC%9A%B0%ED%9A%8C> , <https://www.boannews.com/media/view.asp?idx=74566>






