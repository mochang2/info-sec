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
####
* 참고:

## SSRF(Server Side Request Forgery)
###### CSRF가 Client를 거점(proxy)로 사용하는 것이라면 SSRF는 Server를 거점(proxy)로 사용하여 위조된 요청을 보내는 것이다.
#### 보통 웹 서버는 공개적으로 사용자가 접근이 가능하지만, 조직 내부의 서버는 웹 서버나 내부에 있는 컴퓨터를 제외하고는 직접적으로 접근할 수 없다. 이를 우회하고 내부 서버에 직접적으로 악성 행위를 하는 공격이 SSRF이다. SSRF는 취약한 서버(앞단, 웹서버 등)를 이용해 공격자가 내부 서버에 원하는 요청을 보낸다. 내부 서버는 요청이 신뢰하는 서버(즉, 웹 서버)로 부터 온 것이기 때문에 응답을 하고, 응답은 받은 웹 서버는 공격자에게 결과를 전달하게 된다. 
#### SSRF 취약점을 가지고 있는 서버라면, 공격자는 이를 통해 내부 서버들의 주소를 스캔하는 것이 가능하며 API key와 같은 중요 데이터를 유출시킬 수 있다. 또한 임의 코드 실행이나 임의 파일 쓰기 등의 허가받지 않은 행위도 가능하다. 예를 들어 사용자로부터 URI를 입력받고 해당 URI를 검색한 결과를 이미지 태그로 보여주는 사이트가 있다고 하자. 해당 URI를 일반적인 웹 사이트 주소인 https:\//어쩌구 가 아닌 127.0.0.1 등이나 file:\///etc/passwd로 요청하여 내부 서버를 스캔할 수 있는 것이다.
#### SSRF를 예방하기 위한 방법에는 세 가지 정도 있다. 1. 블랙 or 화이트 리스트 기반으로 입력값에 대한 검증을 수행한다. 2. 허용된 도메인과 URL에 대해서만 입력값을 받는다(다만 서비스에 제약이 생길 수 있다). 3. 요청을 처리하는 서버와 중요 정보가 있는 내부망을 분리시킨다.

* 참고: <https://guleum-zone.tistory.com/165> , <https://blog.lgcns.com/2503> , <https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=aepkoreanet&logNo=221567575013> , <https://cosyp.tistory.com/246>

------------------------

# 8월
####
