# 1월
## SQLite 취약점 발견
#### SQLite는 MySQL이나 PostgreSQL과 같은 데이터베이스 관리 시스템이지만, 서버가 아니라 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다. 
#### 마젤란(Magellan)이라는 SQLite 취약점은 원격지의 공격자가 영향을 받는 기기에서 임의 또는 악성 코드를 실행하고, 프로그램 메모리를 누출시키거나 응용 프로그램을 중단시킬 수 있다.

* 참고: <https://ko.wikipedia.org/wiki/SQLite> , <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=30151&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

</br>

## 아나토바(Anatova) 랜섬웨어
#### 랜섬웨어(ransomware)는 몸값(ransom)과 소프트웨어(software)가 합쳐진 단어로 파일 등을 암호화한 뒤 몸값을 요구하는 범죄를 말한다. 보통 토르(Tor) 네트워크 등을 통한 암호화폐를 몸값으로 요구하므로 추적이 힘들며, 몸값을 보내도 암호화를 해제할 거라는 보장이 없다.
#### 아나토바는 게임이나 앱의 아이콘으로 위장한다. 샌드박스 환경(동적 분석을 하기 위한 환경)에서 실행되는 것을 막기 위해 가상 기계 탐지 절차를 수행한 후 특정 몇 개 국가(시리아, 이라크 등)에서 피해를 일으키지 않도록 국가 설정 내용을 확인한다. 마지막으로 1MB 이하의 파일들과 네트워크 공유 자원을 찾아 암호화하는 방식으로 동작한다. 아나토바는 랜섬웨어 샘플마다 고유한 키를 가지고 있기 때문에 마스터키가 존재하지 않는다고 한다. 그래서 한 번 감염되면 직접 키를 구해서 복호화하긴 힘들어 보인다.

* 참고: <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=30152&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

</br>

## 로그 설정 권고(윈도우)
1. 이벤트 로그 감사 설정
#### 제어판을 이용하여 설정. gpedit.msc > 컴퓨터 구성 > Windows 설정 > 보안 설정 > ... > 계정 로그온, 계정 관리, 세부 추적, 로그온/로그오프 , 개체 액세스, 시스템 등의 감사 정책 설정.
</br>

2. 이벤트 로그 크기 설정
#### 레지스트리를 이용하여 설정. HKLM\SYSTEM\CUrrentControlSet\services\eventlog\...\MaxSize 에서 보안(Security.evtx), 시스템(System.evtx), 애플리케이션(Application.evtx)는 4GB이상, 파워쉘(Windows PowerShell.evtx)는 100MB이상 권장.
</br>

3. 로컬 방화벽 로그 설정
#### 제어판을 이용한 설정. 시작 프로그램, 관리 도구 또는 제어판 > ... > 속성 > 로깅 또는 사용자 지정. 손실된 패킷을 로그에 기록: 활성화, 성공한 연결을 로그에 기록: 활성화, LogFileSize: 100MB 이상 권장.
</br>

4. 프리패치 활성화(프리패치: Windows 운영체제에서 응용프로그램이 사용하는 시스템 자원을 특정 파일에 미리 저장하여, 프로그램 실행을 빠르게 도와주는 파일)
#### 레지스트리를 이용하여 설정. HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters\EnablePrefetcher 에서 0x03 권장(0x00: 비활성화 0x01: 응용프로그램 프리패칭 활성화 0x02: 부트 프리패칭 활성화 0x03: 응용프로그램과 부트 프리패칭 활성화).
</br>

5. 시스템 복원 설정
#### 제어판을 이용한 설정. 시작프로그램, 관리 도구 > ... > 백업 일정 또는 제어판> ... > 복원 설정, 디스크 공간 사용에서 시스템 설정 및 이전 버전 파일 복원 체크 후 디스크 공간 사용을 20GB이상으로 설정 권장.
</br>

* 참고: <https://krcert.or.kr/data/guideList.do?page=2&sort_code=&sort_code_name=&search_sort=title_name&search_word=> , <http://forensic.korea.ac.kr/DFWIKI/index.php/%ED%94%84%EB%A6%AC%ED%8C%A8%EC%B9%98_%EB%B6%84%EC%84%9D_%EB%8F%84%EA%B5%AC>

</br>

## 로그 설정 권고(리눅스)
1. 히스토리 파일명 변경
#### set HISTFILE/HISTFILESIZE/HISTSIZE = xx 로 설정하여 History 로그 관련 파일명과 설정 변경. 공격자가 로그를 지울 수 있기 때문.
</br>

2. 로그 로테이션 설정
#### logrotate 설치 후 logrotate.conf 설정. 필요시 /etc/logrotate.d/ 이하에 각 로그 파일 이름으로 되어 있는 파일을 수정. .conf 권장값은 monthly // rotate 6 // create // compress // include /etc/logrotate.d.
</br>

3. 커널 로그 설정
#### dmesg 로깅 설정. RedHat, CentOS, Debian, Ubuntu 각자 /etc/rsyslog.conf 또는 /etc/rsyslog.d/50-default에서 kern.* /var/log/kern.log 가 동작하도록 추가 또는 주석 해제.
</br>

4. wtmp, btmp 등은 교재에 있는 것과 같음

----------------------------------------------------------------------

# 2월
## 클롭(Clop) 랜섬웨어
#### 클롭 랜섬웨어 감염 증상으로는 파일 암호화를 위해 특정 프로세스 종료, 피해 시스템의 주요파일 암호화 및 확장자 변경, 암호화된 폴더에 복호화 방법이 기술된 랜섬노트 생성 등이 있다. clearsystem-10-1.bat란 파일을 생성함으로써 시스템을 복구할 수 없도록 볼륨쉐도우 파일을 삭제하기도 한다. 또한 아나토바처럼 감염 시스템의 키보드레이아웃 정보를 확인하고 나열된 국가 및 러시아 문자셋을 사용하는 시스템 감염 대상에서 제외시킨다. 

* 참고: <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=34963&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

---------------------------------------------------------------------

# 3월
## 임의 코드 실행(arbitrary code execution)
#### 보안상 허점을 이용해 공격자가 원하는 임의의 코드를 실행시켜 원래대로라면 일어나서는 안되는 일이 일어나게 하거나 권한부여를 받게 만드는 것을 말한다. 이러한 취약점을 악용할 수 있도록 설계된 프로그램을 임의 코드 실행 익스플로잇(exploit)이라고 한다. 이 취약점의 대부분은 기계어와 셸 코드를 실행하고 공격자가 임의로 입력한 셸 코드를 실행, 삽입하도록 허용한다. 이를 통해 공격자가 취약한 프로세스를 완전히 탈취할 수 있게 된다. 임의 코드 실행의 일부인, 다른 기기에서 네트워크를 통해 임의 코드 실행을 하도록 만드는 것을 원격 코드 실행(remote code execution)이라고 한다.
#### 임의 코드 실행은 프로세스가 다음에 실행시켜야 할 명령을 가리키는 프로그램 카운터(PC, Program Counter)를 제어하면서 이루어진다. 임의의 코드가 실행되도록 하기 위해 많은 익스플로잇들은 사용자 입력 버퍼 등의 공간에 코드를 주로 삽입한다. 그 후 취약점을 이용해 프로그램 카운터를 삽입한 코드가 존재하는 곳으로 변경하면 삽입된 코드가 자동적으로 실행된다. 침입자는 이러한 임의 코드 실행을 바탕으로 추가적인 제어를 위해 권한 확대(root, System, Admin 권한) 공격과 같은 추가적인 공격을 시도할 수 있다.

* 참고: <https://ko.wikipedia.org/wiki/%EC%9E%84%EC%9D%98_%EC%BD%94%EB%93%9C_%EC%8B%A4%ED%96%89> , <https://namu.wiki/w/%EC%9E%84%EC%9D%98%20%EC%BD%94%EB%93%9C%20%EC%8B%A4%ED%96%89> , <https://krcert.or.kr/data/secInfoView.do?bulletin_writing_sequence=34982&queryString=cGFnZT03JnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>
</br>

---------------------------------------------------------------------

# 4월
## 오버플로우(overflow)와 언더플로우(underflow)
#### 언어에는 데이터 타입(정수형, 실수형 등)마다 표현할 수 있는 범위가 제한되어 있다. 이 때 최댓값의 범위보다 위로 벗어나는 연산이 이루어지는 경우 오버플로우가 발생하며 최솟값의 범위 아래로 벗어나면 언더플로우가 발생한다. (언어마다, os마다 다르긴 하지만)오버플로우가 발생하면 아주 작은 수로써 연산되거나, 언더플로우가 발생하면 아주 큰 수로써 연산되기도 한다. 이를 통해 프로그램이 예기치 못한 상태로 동작할 수 있다. 특히 반복문, 제어, 메모리 할당 등을 위한 조건으로 사용되는 부분일 경우 문제는 더 심각해진다. 정수형 오버플로우로 인해 버퍼 오버플로우 같은 다른 종류의 버그가 나타날 수 있기 때문이다.
#### 단순 오버플로우나 언더플로우는 프로그래밍 중 쉽게 알아차리기 어렵기 때문에 언어/플랫폼 별 데이터 타입의 범위를 잘 확인하여 사용해야 한다. 또한 외부 입력 값을 동적으로 할당하여 사용하는 경우 변수의 값 범위를 검사하여 적절한 범위 내에 존재하는 값인지 확인할 필요가 있다.

* 참고: <https://edu-coding.tistory.com/4> , <https://m.blog.naver.com/wwwkasa/80180210172> , <https://skogkatt.tistory.com/240>
</br>

---------------------------------------------------------------------

# 5월
## 소디노키비(sodinokibi) 랜섬웨어
#### WebLogic Server 취약점(CVE-2019-2725)을 악용한 랜섬웨어이다. WebLogic Server 취약점은 2017, 2020 OWASP TOP10에 속하는 안전하지 않은 역직렬화(Insecure Deserializaion), 그로 인해 발생하는 인증 우회 및 원격코드 실행 취약점이다.

* 참고: <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=35035&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

----------------------------------------------------------------------

# 6월
## Vim, Neovim OS 명령어 실행 취약점(CVE-2019-12735)
#### Vim과 Neovim은 리눅스 시스템에서 커맨드라인 텍스트 편집 도구이다. cat, more 등을 통해 읽을 수 있는 파일들은 Vim 등으로도 읽을 수 있다고 생각하면 된다.
#### 이 취약점은 modeline를 처리하는 과정에서 발생한다. modeline은 특정 파일에서 다른 옵션들을 적용할 때 사용되는 기능으로, 문서의 시작과 마지막 라인 근처에 파일의 제작자가 언급한 커스텀 설정 세트를 자동으로 찾아 적용하는 기능으로 기본으로 활성화되어 있다.
#### 해결 방안으로는 modelines 기능 비활성화, modelines의 수식을 비활성화 하기 위한 “modelineexpr” 비활성화, Vim modelines의 대안인 “securemodelines plugin” 사용 등이 있다.

* 참고: <https://vim.fandom.com/wiki/Modeline_magic> , <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=35049>

</br>
