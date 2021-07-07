# 7월
## fileless malware
#### 파일리스(fileless)란 단어가 의미하듯이 실행 파일과 다르게 희생자의 컴퓨터의 저장장치에 악성 파일을 저장하지 않는다는 의미이다. 그 대신 (powershell과 같은)정상적인 프로그램을 이용하여 바로 메모리(RAM)에 상주시킴으로써 컴퓨터를 감염시킨다. 따라서 일반적인 파일 스캔하는 방식으로는 악성코드를 찾아낼 수 없고, 동작 기반 탐지 도구를 사용하여 다계층 방어(공격 전, 중, 후)를 사용해야 한다고 한다.  과거에는 시스템 전원이 꺼지면(또는 재부팅 되면) 사라지는 일시적인 malware였다면, 최근에는 시스템 전원이 꺼져도 지속되는 persistent fileless malware이다.
#### 해커가 사용하는 기술에는 1. Reflective DLL injection 2. Memory exploits 3. Script-based techniques 4. WMI(Windows Management Instrumentation) persistence 등이 있다.
![Figure 1. Example of a fileless attack kill chain.](https://www.mcafee.com/enterprise/en-us/img/diagrams/fileless-attack-kill-chain.png)

* 참고: <https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=aepkoreanet&logNo=220934328454> , <https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=aepkoreanet&logNo=221583196950> , <>

------------------------

## 제로데이(zero-day) vs 원데이(one-day) vs 올데이(olday)
#### 제로데이는 알려지지 않은 취약점이 공개되어 그 취약점을 이용한 공격을 당했지만, 현재 이에 대한 대응 방안이나 보안패치가 없는 상태를 말한다. 가장 까다로운 상태의 공격이고 APT 공격이 주로 감행된다.
#### 원데이는 취약점에 대한 패치가 발표되었지만 검증 및 여러 가지 이유 때문에 패치가 적용되지 않은 상태를 말한다. 패치가 발표되더라도 현실적인 이유로 바로 취약점 패치가 이루어지지 않기 때문에 발생하는 상태이다.
#### 올데이는 취약점 분석도 끝나고 오래전에 발표된 패치도 있으나, 패치가 아직 적용되지 않은 상태이다. 보안 담당자의 부재 및 보안 인식 부족으로 인해 주로 발생한다.

* 참고: <https://kimjs6873.tistory.com/8> , <https://whitehole.tistory.com/59>

------------------------

## RTL(return to libc)
###### libc는 모든 C standard library들을 말한다. 따라서 RTL을 return to library와 혼용되어 쓰인다.
#### RTL을 알기 위해선 DEP 또는 NX bit를 먼저 알아야 한다. 공격자들이 RTL를 활용하여 우회하려는 방어기법들을 인텔에서는 XD(eXecute Disable) bit, AMD에서는 EVP(Enhanced Virus Protection), 윈도우에서는 DEP(Data Execution Prevention)이라 한다. 정확히 들여다보자면, DEP란 데이터 영역에서 코드가 실행되는 것을 막는 기법이다. 공격자가 힙 또는 스택 영역에 쉘 코드를 저장해서 실행하기 위해 해당 영역에 실행권한이 있어야 하지만 DEP를 적용된 경우 실행권한이 없어 쉘 코드가 실행되지 않고 프로그램에 예외가 발생하여 종료가 된다. NX bit는 메모리에서 데이터 영역을 실행하는 것을 방지해주는 CPU 기능이다. NX 특성으로 지정된 모든 메모리 구역에서 데이터 저장만 가능하며 프로세서 명령어가 그곳에 상주하지 않음으로써 실행되지 않도록 만들어준다.
#### RTL 정의 + 방어법 등

## return to work program
