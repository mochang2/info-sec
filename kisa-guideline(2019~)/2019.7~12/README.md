# 7월
## 망연계 솔루션(SecureGate)
#### 망연계 솔루션은 망분리된 환경에서 인터넷망과 업무망 간, 즉 서로 다른 네트워크망 간 실시간 데이터 연계(스트리밍) 또는 파일 전송 서비스를 보안정책에 따라 안전하게 전송해 줄 수 있는 환경을 제공하는 솔루션을 말한다. 이를 통해 분리된 망 환경의 높은 보안성을 유지하면서 업무 연속성 및 편의성을 제공한다.

* 참고: <http://www.hanssak.co.kr/solution/securegate.html> , <https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=mplsoft&logNo=221129557556> , <http://it.chosun.com/site/data/html_dir/2020/12/16/2020121600391.html>

----------------------------------------------------------------------

# 8월
## ASUS, Toshiba, Intel, NVIDIA 등 20여 개의 주요 공급 업체 드라이버 보안 취약점 발견
#### 하드웨어 드라이버는 특정 유형의 하드웨어 장치를 제어하여 운영체제와 올바르게 통신하는데 도움이 되는 소프트웨어 프로그램이다. 하드웨어 드라이버는 하드웨어와 운영 체제 사이에 있으며 대부분의 경우 운영체제 커널에 대한 액세스 권한이 있어서 공격자가 드라이버 취약점을 이용할 경우 시스템을 손상시킨 후 사이버 공격의 지속성을 유지(백도어 등)하는데 가장 중요한 역할을 한다. 이를 통해 DOS나 랜섬웨어 공격으로 이어질 수 있다.
#### 장치 드라이버 취약점은 LoJax 악성코드처럼 운영체제를 완전히 다시 설치하더라도 운영체제 아래에 아래 있는 펌웨어 링에 접근하여 악성코드를 지속할 수 있어 즉각적 보안패치가 권고된다.

* 참고: <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=35110>

## 메모리 커럽션
#### 
+ 2020.5 XSS(stored, dom based, reflected xss)
+ 2020.5 use after free 취약점
+ 2020.9 DLL 하이재킹
+ 2021.4 path traversal 취약점

----------------------------------------------------------------------

# 9월
## DDOS 대응방안
1. SYN Flood
#### SYN 자체가 공격이 아니다. 짧은 기간 동안 많은 SYN 패킷이 오는 것이 공격이다. 따라서 방화벽 및 프록시 서버와 같은 모든 주변 장치에서 "TCP 연결 유지" 및 "최대 연결" 규칙을 정의한다. 또한 SYN cookie를 사용하여 인증된 사용자만 백로그큐를 사용하게 함으로써 공격의 영향을 완화할 수 있다.
</br>

2. SYN/ACK Flood(TCP SYN DRDOS)
#### TCP는 일정 시간 안에 응답이 없으면 패킷이 정상적으로 전달되지 못한 것으로 판단하여 재전송하기 때문에 공격의 효과가 더 커지게 된다. UDP나 ICMP flood와 같이 방화벽이나 프록시 서버에서 패킷 임계치 기반 차단 설정을 함으로써 방어할 수 있다.
</br>

3. NTP DRDOS(UDP 포트를 이용하는 서비스 중 하나)
#### NTP는 UDP 123번 포트를 이용하여 네트워크로 연결된 컴퓨터의 시간을 동기화하는데 사용된다. monlist 요청은 해당 NTP 서버에 접속한 사용자들을 묻는 요청으로 요청 대비 응답이 매우 큰 요청이다. NTP 서버를 2.4.7이상으로 업그레이드함으로써 monlist 명령을 제거하거나 OpenNTPD와 같이 monlist를 활용하지 않는 NTP 버전을 이용한다. 서버를 업그레이드할 수 없는 경우 npt.conf에서 disable moniter를 추가하고 NTP 데몬을 재기동한다. 또한 다른 공격에 대한 방어와 마찬가지로 방화벽 규칙을 적용한다.
</br>

4. DNS DRDOS(UDP, TCP 53번 포트 사용)
#### DNS의 any 또는 txt 타입의 쿼리를 사용한다. 응답 대비 요청이 상당히 크기 때문이다. DNS 개발사(BIND, MS 등)에서 제공한 지침에 따라 DNS 재귀 기능을 사용하지 않음으로써 (또는 허가된 사용자만, 특히 authoritative server 같은 경우) 어느 정도 방어가 가능하다.
</br>

5. CLDAP(Connection-less Lightweight Directory Access Protocol)
#### 공격자가 공격대상 IP 주소로 도용하고 LDAP 서버로 CLDAP 요청을 보내는 형태의 공격이다. CLDAP은 공유 인터넷 디렉터리를 연결/검색/수정하는데 사용되며 UDP 389 포트를 사용한다. UDP LDAP 프로토콜은 52~70배까지 증폭이 가능하여 공격 효율성이 높다. LDAP 서버를 운영하는 경우 방화벽 규칙을 설정하여 공격에 악용되지 않도록 예방 조치가 필요하다

* 참고: <https://krcert.or.kr/data/guideView.do?bulletin_writing_sequence=35135&queryString=cGFnZT0yJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9>

----------------------------------------------------------------------

# 10월
## 리눅스 Wi-Fi 취약점 발견
#### 리눅스 무선랜 드라이버 중 Realtek WiFi(rtlwifi) 드라이버에서 경계값 체크가 모호한 버퍼 오버플로우가 발생했다. 공격자가 경계값을 넘어서는 길이의 NoA(Notice of Absence, rtlwifi 드라이버에서 구현한 부재 알림 기능에 사용되는 프로토콜로, 자동으로 무선전원을 끄고 에너지를 절약하기 위해 사용됨) 패킷을 전송시 발생한다고 한다. Wi-Fi가 꺼져 있거나 다른 제조업체의 Wi-Fi칩을 사용한 경우 버그의 영향을 받지 않는다고 한다.

* 참고: <https://krcert.or.kr/data/trendView.do?bulletin_writing_sequence=35182> , <https://m.blog.naver.com/cyberpass/221683589107>

----------------------------------------------------------------------

# 11월

----------------------------------------------------------------------

# 12월

</br>
