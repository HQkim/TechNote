# 주소창에 `www.naver.com`을 치면 일어나는 일

주소창에 www.naver.com을 치면 내부적으로 어떤 동작이 일어나는지 살펴보자.



![img](00_web_%EB%8F%99%EC%9E%91%EC%9B%90%EB%A6%AC.assets/img_webbasic_10.png)

사진 출처: http://tcpschool.com/webbasic/works



**①② 사용자가 웹 브라우저를 통해 찾고 싶은 웹 페이지의 URL 주소를 입력함.**

**③ 사용자가 입력한 URL 주소 중에서 도메인 네임(domain name) 부분을 DNS 서버에서 검색함.**

**④ DNS 서버에서 해당 도메인 네임에 해당하는 IP 주소를 찾아 사용자가 입력한 URL 정보와 함께 전달함.**

 

**⑤⑥ 웹 페이지 URL 정보와 전달받은 IP 주소는 HTTP 프로토콜을 사용하여 HTTP 요청 메시지를 생성함.**

**이렇게 생성된 HTTP 요청 메시지는 TCP 프로토콜을 사용하여 인터넷을 거쳐 해당 IP 주소의 컴퓨터로 전송됨.**

 

**⑦ 이렇게 도착한 HTTP 요청 메시지는 HTTP 프로토콜을 사용하여 웹 페이지 URL 정보로 변환됨.**

**⑧ 웹 서버는 도착한 웹 페이지 URL 정보에 해당하는 데이터를 검색함.**

 

**⑨⑩ 검색된 웹 페이지 데이터는 또다시 HTTP 프로토콜을 사용하여 HTTP 응답 메시지를 생성함.**

**이렇게 생성된 HTTP 응답 메시지는 TCP 프로토콜을 사용하여 인터넷을 거쳐 원래 컴퓨터로 전송됨.**

 

**⑪ 도착한 HTTP 응답 메시지는 HTTP 프로토콜을 사용하여 웹 페이지 데이터로 변환됨.**

**⑫ 변환된 웹 페이지 데이터는 웹 브라우저에 의해 출력되어 사용자가 볼 수 있게 됨**

---



위는 아래 [출처](http://tcpschool.com/webbasic/works) 에서 설명한 내용이다. 이 내용들에 있는 키워드를 정리해보자.



### IP 주소

- `IP 주소(Internet Protocol adress)`는 컴퓨터 네트워크에서 장치들이 서로를 인식하고 통신을 하기 위해서 사용하는 특수한 번호이다. 

- 오늘날 주로 사용하고 있는 IP 주소는 `IP 버전 4(IPv4) 주소 `이지만 이 주소가 부족해지면서 길이를 늘린 `IP 버전 6(IPv6) 주소 ` 가 점점 사용되는 추세이다.



### 도메인 네임(Domain Name)

- IP 주소는 IPv4의 경우에는 192.168.1.0과 같이 숫자로 이루어져 있기 때문에 사람이 외우기 쉽지 않다. 그래서 전화번호부와 같은 역할을 하는 서비스가 필요한데 이를 `DNS(Domain Name System)`  라고 한다. 
- 즉, IP주소와 도메인 네임을 한 쌍으로 저장하고 있는 데이터베이스 서버를 DNS 서버라고 한다. 



### HTTP

- **H**ypter **T**ext **T**ransfer **P**rotocol
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
- 웹에서 이루어지는 모든 데이터 교환의 기초이며, 클라이언트-서버 프로토콜
- TCP/IP 위에서 돌아감
- 자세한 것은 다른 문서에서 다룰 예정



### TCP

- 전송 제어 프로토콜 (**T**ransmission **C**ontrol **P**rotocol)

- 두 개의 호스트를 연결하고 데이터 스트림을 교환하게 해주는 중요한 네트워크 프로토콜
- 데이터와 패킷이 정해진 순서대로 전달하는 것을 보장해줌
- IP와 함께 TCP/IP라는 명칭으로도 널리 불림
- 자세한 것은 다른 문서에서 다룰 예정



### 참고

- http://tcpschool.com/webbasic/works

- https://ko.wikipedia.org/wiki/IP_%EC%A3%BC%EC%86%8C

- https://m.blog.naver.com/adamdoha/222080758916

- https://developer.mozilla.org/ko/docs/Web/HTTP/Overview

- https://developer.mozilla.org/ko/docs/Glossary/TCP