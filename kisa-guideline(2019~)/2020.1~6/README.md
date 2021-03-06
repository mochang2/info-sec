# 1월
## 
#### 

* 참고: <>

----------------------------------------------------------------------

## 
#### 

* 참고: <>
----------------------------------------------------------------------

# 2월
## 

* 참고: <>

----------------------------------------------------------------------

# 3월
## 정보보호 최고책임자(CISO)의 업무
#### 전자금융거래법에 따른 CISO의 업무는 1. 전자금융거래의 안정성 확보 및 이용자 보호를 위한 전략 및 계획을 수립. 2. 정보기술부문 보호. 3. 정보기술부문의 보안에 필요한 인력관리 및 예산 편성. 4. 전자금융거래의 사고 예방 및 조치.
#### 정보통신망법에 따른 CISO의 업무는 1. 정보보호 관리체계의 수립 및 관리, 운영 2. 정보보호 취약점 분석, 평가 및 개선 3. 침해사고의 예방 및 대응 4. 사전 정보보호 대책 마련 및 보안조치 설계, 구현 등 5. 정보보호 사전 보안성 검토 6. 중요 정보의 암호화 및 보안서버 적합성 검토 7. 그밖에 이 법 또는 관계 법령에 따라 정보보호를 위하여 필요한 조치의 이행
#### CISO의 책임과 역할. 보호정책 및 전략 의사결정(정보보호 정책/지침 총괄, 정보보호/개인정보보호 관련 법률의 이해, 연간정보보호 추진을 위한 자원 확보, 전사보호 이슈 대응/해결, 정보보호 인식제고 및 정보보호 문화 확산), 전사 보안조직 총괄(정보보호조직/R&R 관리, 실무 협의회 운영/관리, 이해관계부서 간 이슈 및 갈등 조정, 정보보호 관련 변화관리), 정보보호 침해사고 대응총괄(보안사고 대응 총괄, 보안사고 대응 훈련 계획 수립 및 총괄 관리, 침해사고 대응조직 구성 관리, 개인정보 유출사고 시 대외기관 신고), 정보보호 투자계획 심의/결정(정보보호 중장기 추진 전략 검토/승인, 중장기 정보보호 투자 계획 심의, 연간 정보보호 투자 계획 수립)
#### 정보보호에 관한 규정. 규정의 종류와 내용을 정의한 기준은 별도로 없으며 조직의 특성을 고려하여 수립한다. 보통 정보보호 관리지침, 서버운영 보안지침, 네트워크운영 보안지침, 보안장비운영 보안지침, DB운영 보안지침, 임직원 보안지침, 어플리케이션 개발/운영 보안지침, 재해복구 관리지침, 물리보안지침, 침해사고 대응지침, 정보자산관리지침, 개인정보보호 지침 등으로 나뉜다.

* 참고: <https://krcert.or.kr/data/guideView.do?bulletin_writing_sequence=35296&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

----------------------------------------------------------------------

# 4월
## path traversal(directory traversal, dot-dot-slash, directory climbing, backtracking)
#### path traversal은 웹 루트 디렉토리 외부에 저장된 파일 및 디렉터리에 접근하는 기법이다. 경로 탐색 취약점이라고도 불리며 절대경로(../)를 참조하는 변수를 조작해 허가되지 않은 파일 및 디렉터리에 접근할 수 있다. path traversal 공격 시 가장 많이 탐지되는 로그 패턴에는 '../../../Windows/system.ini', '..%5C..%5c..%5cWindows%5Csysem.ini', '%2F..%2F..etc%2Fpasswd' 등이 있다.
#### 설명만 들었을 때는 file inclusion 취약점과 같은 것 아닌가라는 착각이 들을 수 있다. 두 취약점에는 명확한 차이가 존재하는데 path traversal은 공격자가 파일을 읽는 것만 가능하지만 LFI, RFI는 악성 코드를 직접 실행할 수 있다는 것이다.
#### path traversal을 예방하는 방법에는 1. 사용자 입력을 기반으로 동적으로 파일을 읽지 않는다. 2. 파일 화이트리스트를 유지하여 입력에 대한 유효성 검사를 해야 한다. 공격자가 특수 문자나 문자 시퀀스를 사용하여 필터를 조작할 수 있으므로 파일 경로 요소, 파일 확장명 등을 기반으로 필터링하는 일반적인 웹 애플리케이션 보안 메커니즘은 비효율적이다. 3. chrooted jail 이나 접근 제어를 활용하여 파일을 가져오거나 저장할 수 있는 위치를 제한한다.

* 참고 : <https://www.acunetix.com/blog/articles/path-traversal/> , <https://owasp.org/www-community/attacks/Path_Traversal> , <https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=6yujin6&logNo=221730643367> , <https://rjswn0315.tistory.com/108>

----------------------------------------------------------------------

# 5월
## 산업제어시스템(ICS, Industrial Control System)
#### ICS란 산업생산에서 사용되는 감시 제어 및 데이터 수집(SCADA, Supervisory Control And Data Acquision), 분산제어시스템(DCS, Distributed Control System), 프로그래머블 로직 컨트롤러(Programmable Logic Controller)와 Field Device 같은 시스템을 포함한 여러 종류의 제어시스템을 말한다. ICS는 하나의 산업 목표(제조, 운송 등)를 달성하기 위해 함께 작동하는 제어 구성요소(전기, 기계, 유압, 공압)의 조합들로 구성된다.
#### 그 중 SCADA는 발전소, 철도, 항만과 같은 사회기반시설이나 산업체의 공장을 감시, 제어하고 운영 관련 데이터를 수집, 기록하는 역할을 한다. SCADA는 DCS와 자주 비교된다. SCADA는 공정을 조직화하여 감시하는 장치이지만 DCS는 실시간으로 공정을 제어하는 시스템이다. 또한 SCADA는 지리적으로 넓게 분산되는 형태의 응용에 적합하고 DCS는 하나의 지엽적인 현장에서 발생하는 작업들을 처리하는데 주로 사용된다.
#### PLC는 산업 플랜트의 유지관리 및 자동 제어 및 모니터링에 사용하는 (기계)제어 장치이다. PLC는 입력을 프로그램에 의해 순차적으로 논리 처리하고 그 출력 결과를 이용해 연결된 외부장치를 제어한다. 순차제어(sequential control)에 사용되는 대표적 장치이다. PLC는 단독으로 쓰일 수도 있고, SCADA 등의 시스템과 함께 사용되기도 한다.
<img src="https://www.securicon.com/wp-content/uploads/2019/05/image001.png" width="200px" height="auto" />

* 참고: <https://krcert.or.kr/data/guideView.do?bulletin_writing_sequence=35433&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9> , <https://www.securicon.com/whats-the-difference-between-ot-ics-scada-and-dcs/> , <https://ko.wikipedia.org/wiki/%EC%8A%A4%EC%B9%B4%EB%8B%A4> , <https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EB%B8%94_%EB%A1%9C%EC%A7%81_%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC>
</br>

## 딥링크(Deeplink)
#### 딥링크란 모바일 웹상에 있는 링크나 그림을 클릭할 경우 기기 내 관련 앱이나 사전에 정의된 특정 웹페이자 실행되는 모바일 기술을 말한다. 웹(WWW) 어플리케이션이 http:// 나 https:// 프로토콜을 가지고 있는 것처럼, 모바일 어플레케이션도 각자의 프로토콜을 가지고 있다. 예를 들면, 유튜브는 youtube://, 멜론(아이폰)은 meloniphone://, 벅스는 bugs3:// 프로토콜을 가지고 있다. 가끔씩 모바일로 웹 서핑을 하다가, 어떤 버튼을 눌렀는데 네이티브 앱으로 바로 이동하는 경험을 해본 경험이 있을 것이다. 그것이 바로 '모바일 딥링크'를 이용하여, 특정 앱 페이지로 들어가는 것이다.
#### 이 딥링크에 취약점이 있다. 모바일 어플리케이션마다 개별적으로 생성한 딥링크의 검증이 없을 경우, 관련 앱 자바 스크립트가 권한인증 없이 자동으로 실행되어 의도치 않은 악성 URL에 접속하고 어플리케이션 내 민감 정보가 공격자에게 노출된다.
#### 딥링크 취약점과 관련하여 다음과 같은 조치방안을 참고하여 패치 및 개발이 권고된다. 첫째는 딥링크 URI 파싱시 취약한 함수 사용 금지하기이다. URI 파싱 시 getHost, substring, split과 함수 보다는 getQueryParmaeter 등의 함수를 활용하여 필터링이 가능하도록 한다. 둘째는 인가된 URI에만 자바인터페이스 권한을 부여한다. 외부 사이트에서 접속 시 검증 없이 자바인터페이스 권한을 줄 때 이를 악용하여 개인정보가 유출되기 때문이다. 셋째는 도메인 검증을 이용한 우회를 방지한다. 하드코딩된 일부 string 구문 비교를 통해 파싱할 경우 취약점을 유발할 수 있으므로 검증된 도메인에서 함수 호출, 정보 반환, 웹뷰를 출력하도록 검증된 도메인 리스트 설정을 하거나, 서브 도메인 악용을 막기 위해 슬래쉬(/)로 끝나도록 명확한 검증 도메인명을 작성한다. 넷째로 URI.parse 함수 사용 시 특정 기능을 수행하는 특수문자들을 필터링한다.

* 참고: <https://blog.ab180.co/posts/deeplinkga-mweojyo> , <https://krcert.or.kr/data/guideView.do?bulletin_writing_sequence=35434&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

## use after free(UAF) 취약점
#### UAF는 힙(heap)에서 메모리를 할당한 공간을 free 한 후에 재사용할 때 일어날 수 있는 취약점이다. 힙이란 프로그래머의 필요에 의해서 메모리 공간이 동적으로 할당 및 소멸되는 영역을 말한다. 힙은 런타임 시 할당되는 영역이넫 바이너리가 실행되고 죽기 전까지 힙에 데이터가 남아이쎅 된다. 이와 반대로 같은 메모리 공간을 공유하지만 정적으로 할당되기 때문에 컴파일 시 미리 공간이 할당되어 있는 곳을 스택이라고 한다. 스택은 생성될 때 배열 사이즈가 상수로 고정될 수밖에 없게 된다.
#### 힙은 메모리를 효율적으로 사용하기 위해 반환된 힙 영역의 크기를 기억해놨다가 같은 크기의 할당 요청이 들어오면 이전 영역을 재사용한다. c/c++에서 사용되는 malloc 함수에는 캐싱 기능이 있는데 할당했던 공간을 다시 할당함으로써 병합하거나 분할하는 시간을 절약하고자 사용되는 기능이다. 이로 인해 메모리를 효율적으로 사용할 수 있지만, 원하지 않는 값을 참조하게 될 수 있다. 특히 할당됐던 공간에 비밀번호나 개인정보 등을 저장하게 되면 더 큰 문제가 발생할 수 있다.

    #include <stdio.h>
    #include <stdlib.h>
  
    int main(){
        int* one = malloc(100);
        *one = 20;
        printf("before free, one address: %p\n", one);
        printf("before free, one value: %d\n", one);
    
        free(one);
    
        int* two = malloc(100);
        printf("after free, two address: %p\n", one);
        printf("after free, two value: %d\n", one);
    
        return 0;
    }
    
#### 위는 간단한 UAF 예제 코드이다. 보안 업데이트가 되어 있지 않는 곳에서 위 코드를 실행하면 one과 two의 주소와 값(20으로)이 같게 된다. 보안 업데이트가 되어 있는 곳에서도 위 코드를 실행하면 병합 지연(Deferred Coalescing)으로 인해 one과 two가 같은 주소를 공유할 수도 있다. 하지만 two의 값은 초기화된 상태로 할당된다.
#### 이처럼 UAF 취약점을 막기 위해서는 보안 업데이트를 하거나, 새로 할당 받은 변수의 값을 초기화해줄 필요가 있다.

* 참고: <https://nroses-taek.tistory.com/156> , <https://woosunbi.tistory.com/95> , <https://encyclopedia.kaspersky.com/glossary/use-after-free/> , <https://shayete.tistory.com/entry/7-Use-After-Free> , <https://www.youtube.com/watch?v=RAGar9rRnEM>

## XSS(CSS, Cross Site Script)
#### XSS는 OWASP TOP 10에 2014년과 2017년, 2020년에 연속해서 3번이나~~(사실 그 전에도 뽑혔을 수 있으나 확인은 안 해 봤다)~~ 뽑힐 정도로 악명 높은 취약점이다. XSS는 애플리케이션에서 브라우저로 전송하는 페이지에서 사용자가 입력하는 데이터를 검증하지 않거나, 출력시 위험 데이터를 무효화시키지 않을 때 발생한다. XSS는 일반적으로 자바스크립트에서 많이 발생하지만 VBScript, Flash, ActiveX 등 클라이언트 측에서 실행되어 동적 데이터를 생성하는 언어(Client Side Script)에서 발생이 가능하다.
#### XSS 공격의 의한 피해에는 1. 사용자의 쿠키 정보나 세션 ID를 획득 2. 시스템 관리자 권한 획득 3. 악성코드 다운로드 등이 있다.
#### XSS 공격 유형은 크게 3가지로 분류된다. 첫 번째는 Stored XSS(저장 XSS)이다. DB에 저장함으로써(뒤에 두 가지 유형은 DB에 저장하지 않는다) 웹 서버에 스크립트를 입력시켜 놓으면, 방문자가 악성 스크립트가 삽입되어 있는 페이지를 읽는 순간 공격이 발생한다. 가장 일반적인 방법은 게시판과 같은 곳에 HTML 문서에 _\<script>_ 를 이용하여 이 태그 안에 악성 코드를 저장한다. 간단하게

    <script>alert(document.cookie)</script>

#### 를 통해서 사용자가 이 스크립트가 삽입된 페이지를 읽을 경우 공격자는 사용자의 쿠키를 탈취할 수 있다. alert 대신 다른 공격 코드들도 삽입이 가능하다.
#### 두 번째는 Reflected XSS(반사 XSS)이다. 악성 스크립트가 포함된 URL을 사용자가 클릭하도록 유도(이메일 등을 통해)하여 URL을 클릭하면 공격이 발생한다. Reflected XSS는 웹 애플리케이션의 지정된 변수를 이용할 때 발생하는 취약점을 이용하는 것으로, 검색 결과, 에러 메시지 등 서버가 외부에서 값을 입력받아 브라우저에게 응답할 때 전송하는 과정에서 입력되는 변수를 그대로 돌려주면서 발생한다.

    http://www.example.com/search/?q=<script>alert(document.cookie)</script>&x=0
    // 주로 <script> 이하는 이용자가 눈치채기 힘들게 인코딩하여 전달하는 경우가 많다.

#### 일반적으로 서버에 검색 내용을 입력하면, 검색 결과가 있는 경우에는 결과 값을 사용자에게 전달하지만, 위와 같이 요청하여 서버에서 정확한 결과가 없는 경우 서버는 브라우저에 입력한 값을 그대로 HTML 문서에 포함하여 응답한다. 이 경우 악성 스크립트가 브라우저에서 실행이 된다.
#### 세 번째는 DOM Based XSS(DOM 기반 XSS)이다. DOM 환경에서 악성 URL을 통해 사용자의 브라우저를 공격한다. 여기서 DOM(Document Object Model)이란 HTML 코드로 설계된 웹 페이지가 브라우저 안에서 화면에 나타나고 이벤트에 반응하며 값을 입력받는 등 기능들을 수행할 객체들로 실체화된 형태이다. 보다 정확하게 MDN 정의에 따르면 HTML이나 XML 문서를 나타내는 API라고 한다. DOM Based XSS가 실행되는 과정은 1. 공격자가 파라미터에 악성 스크립트를 포함시킨 URL 등을 희생자에게 전달하면 2. 희생자 브라우저는 렌더링 중 HTML을 페이지에 추가하기 위해 innerHTML로 다뤄지는 사용자 입력을 분석하고 페이지를 동적으로 생성한다. 3. 이러한 과정에서 악성 스크립트가 포함된 사용자 입력이 페이지의 HTML 태그에 추가되어 실행된다. DOM Based XSS는 서버 응답 자체에는 악성 스크립트가 포함되지 않지만, 페이지 구성 시 DOM의 _document.write_ 가 실행되며 아성 스크립트가 실행되는 것이다.
#### 이러한 XSS를 예방하기 위한 기술에는 스크립트에서 특수 기능을 사용하게 되는 문자들인 _<, >, &, " 등_ 을 필터링하거나 허용된 태그들만 사용가능하게 설정하는 방식 등이 있다. 또한 보안 라이브러리를 활용하는 것도 좋은 방법이다.
#### XSS와 항상 같이 언급되는 공격인 CSRF(Cross Site Request Forgery)가 있다. 공격 방식 등에 따라 비슷한 점이 매우 많고 XSS 공격 유형에 따라 차이점도 가지각색이지만, 공통적으로 얘기되는 분명한 차이점이 있다. 그것은 XSS는 악성 스크립트가 _client 측에서 작동_ 한다는 것이고, CSRF는 위조된 요청이 _server 측에서 작동_ 한다는 것이다.

* 참고: <https://twoicefish-secu.tistory.com/126> , <https://www.kisa.or.kr/uploadfile/201312/201312161355109566.pdf> , <https://dongdd.tistory.com/49> , <https://alwaysbeen.tistory.com/57> , <https://www.youtube.com/watch?v=1ojA5mLWts8>

----------------------------------------------------------------------

# 6월
## 비대면 업무환경 보안 가이드
#### 비대면 업무환경에는 업무 수행자가 기업 및 기관 내부의 정해진 사무 공간이 아닌 외부 다른 공간에서 업무를 수행하는 원격근무(회사의 업무처리시스템에 접속하기에 사용자 단말기, 보안 접속 프로그램, 업무처리 시스템으로 구성)와 물리적으로 원격에 있는 사람들이 전용장비/프로그램을 이용하여 회의를 진행하는 영상회의(영상회의 플랫폼에는 기업이 직접 구축하는 방식과 클라우드 SaaS 서비스를 이용하는 방식이 있음)가 있다.
#### 비대면 업무환경에 대해서는 물리적, 인적, 기술적 위협이 존재한다. 특히 원격근무에 대한 기술적 위협에는 사용자 단말기의 취약성, 원격근무에서 사용되는 네트워크 환경의 취약성, 접속 인증절차의 취약성 등이 존재한다. 영상회의에 대한 기술적 위협에는 통신 암호 미흡시 회의 내용 유출 가능성, 화면 탈취, 영상회의 주소가 공개될 경우 디도스 공격 가능성 등이 존재한다.
#### 회의 시 가장 많이 사용되는 Zoom에도 침해사고가 존재했다. 국내 대학 온라인 강의에서 수강생이 아닌 사람들이 강의실에 입장하거나 Zoom Bombing을 발생시켜 회의를 방해, 가짜 영상회의 초대장으로 사용자 계정을 는 공격 등이 발생했다.
###### 원격근무 환경에서 보안을 위해서 원격 근무자는 1. 전용 공간을 확보해야 한다. 2. 허가되지 않은 장비 사용하지 않으며 단말기를 최신 상태로 업데이트 함으로써 단말기 보안을 유지해야 한다. 3. 허가된 프로그램만을 사용하고 보안 업데이트를 최신 상태로 유지하여 프로그램 보안을 유지해야 한다. 4. USB 사용을 자제하고 혹여 필요시 읽기 전용으로만 설정하여 자동실행을 방지해야 한다.  5. 신뢰할 수 없거나 개방형 Wi-Fi는 사용하지 않고 WPA2 이상의 암호화 방식을 사용하는 무선으로 접속해야 한다. 6. 영어 대소문자, 숫자, 특수문자를 조합하여 사용하고 비밀번호 8자 이상 사용이 권장된다. 또한 비밀번호가 노출되지 않도록 브라우저에 암호를 자동 저장 않기 등을 통해 관리해야 한다. 7. 메일 본문에 있는 웹 사이트 링크를 함부로 클릭하거나 첨부파일에 대한 확인 없이 다운로드하지 않아야 한다. 또한 추가 인증을 적용해야 한다.
###### 원격근무 환경 관리자는 1. 계정을 공유할 수 없도록 제한하고 개별 사용자마다 구분된 권한을 부여하여 사용자별 이력 및 행위 추적성을 확보해야 한다. 2. 원격 근무자가 사내 네트워크에 접속시 2FA 등 강력한 인증방안을 사용해야 한다. 3. VPN이나 안전망 등을 통해 허가된 사용자와 단말기만 업무망에 접근하도록 해야 한다. 4. 원격 근무용 단말기의 분실 및 도난, 또는 시스템 이상징후 탐지 시 즉시 대응하는 보안 절차를 운영해야 한다.
###### 영상회의 환경에서 영상회의 개설자는 1. 회의실 입장을 위한 암호를 설정해야 한다. 2. 영상회의실 주소를 고정하여 사용하지 않아야 한다. 3. 초대자와 참석자의 일치 여부를 확인해야 한다. 4. 최신 보안 업데이트 상태로 단말기를 관리해야 한다. 영상회의 참가자는 1. 자동 로그인을 사용하지 않아야 한다. 2. 암호화 통신을 설정하여 진행해야 한다. 3. 회의 내용이 노출되지 않도록 업무 전용 공간을 확보하거나 이어폰을 사용한다.
###### 영상회의 구축형 플랫폼 관리자는 1. 내부 서비스 접근은 기업에서 지정한 단말만 허용하도록 보안 설정해야 한다. 2. 단말기의 보안상태를 점검할 수 있어야 한다(NAC, Network Access Control) 3. 비밀번호 외에도 추가 인증 수단을 마련해야 한다. 4. 로그를 기록하여 사용자 접속 이력 및 행위 추적성을 확보할 수 있게 만들어야 한다. 영상회의 서비스형 플랫폼 관리자는 1. 데이터 암호화 등 데이터 보호 서비스를 적극 활용해야 한다. 2. 보안 취약점 패치를 지속적으로 적용해야 한다. 3. 영상회의 보안 설정을 개설자/사용자에게 문서 형식으로 안내해야 한다.

* 참고: <https://krcert.or.kr/data/guideView.do?bulletin_writing_sequence=35467&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

</br>

##
####
