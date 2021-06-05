# 1월
## SQLite 취약점 발견
#### SQLite는 MySQL이나 PostgreSQL과 같은 데이터베이스 관리 시스템이지만, 서버가 아니라 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다. 
#### 마젤란(Magellan)이라는 SQLite 취약점은 원격지의 공격자가 영향을 받는 기기에서 임의 또는 악성 코드를 실행하고, 프로그램 메모리를 누출시키거나 응용 프로그램을 중단시키도록 허용 가능하다. 

* 참고: <https://ko.wikipedia.org/wiki/SQLite> , <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=30151&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

----------------------------------------------------------------------

## 아나토바(Anatova) 랜섬웨어
#### 랜섬웨어(ransomware) 몸값(ransom)과 소프트웨어(software)가 합쳐진 단어로 파일 등을 암호화한 뒤 몸값을 요구하는 범죄를 말한다. 보통 토르(Tor) 네트워크 등을 통한 암호화폐를 몸값으로 요구하므로 추적이 힘들며, 몸값을 보내도 암호화를 해제할 거라는 보장이 없다.
#### 아나토바는 게임이나 앱의 아이콘으로 위장한다. 샌드박스 환경(동적 분석을 하기 위한 환경)에서 실행되는 것을 막기 위해 가상 기계 탐지 절차를 수행한 후 특정 몇 개 국가(시리아, 이라크 등)에서 피해를 일으키지 않도록 국가 설정 내용을 확인한다. 마지막으로 1MB 이하의 파일들과 네트워크 공유 자원을 찾아 암호화하는 방식으로 동작한다. 아나토바는 랜섬웨어 샘플마다 고유한 키를 가지고 있기 때문에 마스터키가 존재하지 않는다고 한다. 그래서 한 번 감염되면 직접 키를 구해서 복호화하긴 힘들어 보인다.

* 참고: <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=30152&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

----------------------------------------------------------------------

## 로그 설정 권고(윈도우)
1. 이벤트 로그 감사 설정
#### 제어판을 이용하여 설정. gpedit.msc > 컴퓨터 구성 > Windows 설정 > 보안 설정 > ... >계정 로그온, 계정 관리, 세부 추적, 로그온/로그오프 , 개체 액세서, 시스템 등의 감사 정책 설정

2. 이벤트 로그 크기 설정
#### 되나?

* 참고: <https://krcert.or.kr/data/guideList.do?page=2&sort_code=&sort_code_name=&search_sort=title_name&search_word=>

----------------------------------------------------------------------

# 2월
## 클롭(Clop) 랜섬웨어
#### 클롭 랜섬웨어 감염 증상으로는 파일 암호화를 위해 특정 프로세스 종료, 피해 시스템의 주요파일 암호화 및 확장자 변경, 암호화된 폴더에 복호화 방법이 기술된 랜섬노트 생성 등이 있다. clearsystem-10-1.bat란 파일을 생성함으로써 시스템을 복구할 수 없도록 볼륨쉐도우 파일을 삭제하기도 한다. 또한 아나토바처럼 감염 시스템의 키보드레이아웃 정보를 확인하고 나열된 국가 및 러시아 문자셋을 사용하는 시스템 감염 대상에서 제외시킨다. 

* 참고: <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=34963&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

----------------------------------------------------------------------

# 5월
## 소디노키비(sodinokibi) 랜섬웨어
#### WebLogic Server 취약점(CVE-2019-2725)을 악용한 랜섬웨어이다. WebLogic Server 취약점은 2017, 2020 OWASP TOP10에 속하는 안전하지 않은 역직렬화(Insecure Deserializaion), 그로 인해 발생하는 인증 우회 및 원격코드 실행 취약점이다.

* 참고: <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=35035&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

----------------------------------------------------------------------

# 6월
## Vim, Neovim OS 명령어 실행 취약점(CVE-2019-12735)
#### Vim과 Neovim은 리눅스 시스템에서 커맨드라인 텍스트 편집 도구이다. cat, more 등을 통해 읽을 수 있는 파일들은 Vim 등으로도 읽을 수 있다고 생각하면 된다.
#### 이 취약점은 modeline를 처리하는 과정에서 발생한다. modeline은 특정 파일에서 다른 옵션들을 적용할 때 사용되는 기능으로, 문서의 시작과 마지막 라인 근처에 파일의 제작자가 언급한 커스텀 설정 세트를 자동으로 찾아 적용하는 기능으로 기본으로 활성화되어 있다.
#### 해결 방안으로는 modelines 기능 비활성화, modelines의 수식을 비활성화 하기 위한 “modelineexpr” 비활성화, Vim modelines의 대한인 “securemodelines plugin” 사용 등이 있다.

* 참고: <https://vim.fandom.com/wiki/Modeline_magic> , <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=35049>

</br>
