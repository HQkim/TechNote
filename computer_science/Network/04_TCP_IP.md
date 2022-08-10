# TCP/IP와 4계층

## TCP/IP 란 무엇일까?

- 온라인상의 안전하고 효율적인 데이터 전송의 필수 요건을 정의
- 두 개의 기기 간에 데이터를 전송하는 것을 담당
- TCP/IP 4계층 혹은 5계층으로 구성

## TCP? IP?

- TCP/IP는 수많은 컴퓨터 네트워크 프로토콜을 포함. TCP와 IP는 이러한 프로토콜 중 가장 많이 쓰임

- IP (Internet Protocol)
  - 데이터의 조각(패킷)을 최대한 빨리 대상 IP 주소로 보내는 역할을 표시
  - IP주소 체계를 따르고 IP Routing을 이용해 목적지에 도달
- TCP(Transmission Control Protocol)
  - 한 기기에서 다른 기기로 데이터를 전송하는 것을 담당
  - 데이터의 전달을 보증하고 보낸 순서대로 받음
  - IP 위에서 동작
- 데이터 전송 과정에서 TCP와 IP가 각각 담당하는 작업이 있지만, 결국에는 같은 결과를 목표로 하기 때문에 한 명칭으로 불림



## TCP/IP 4계층

- TCP/IP는 통신 규칙의 모음, 프로토콜 스위트라고 불리기도함
- TCP/IP 4계층은 이러한 규칙이나 프로토콜이 적용되는 특정한 조건을 의미
- TCP/IP모델이 다양한 기기와 앱에서 효율적으로 '통신'하고 데이터를 전송할 수 있도록 하는 방식



### 응용 계층 (Application Layer)

- 앱에 구축되어 사용자가 상호작용하기 가장 쉬운 계층
- 사용자(사람 또는 소프트웨어)가 네트워크에 접근할 수 있도록 함
- 사용자 인터페이스를 제공할 뿐만 아니라 이메일, 원격 파일 접근 및 전송, 공유 데이터베이스 관리 등의 서비스 제공
- 전자우편 표준 통신 규약인 SMPT (Simple Mail Transfer Protocol), 웹서버와 사용자의 인터넷 브라우저 사이에 문서를 전송하기 위해 사용되는 통신 규약인 HTTP(Hyper Text Transfer Protocol)
- 이외에도, 파일 전송 규약(File Transfer Protocol: FTP), 동적 호스트 설정 통신 규약(Dynamic host Configuration protocol: DHCP), 간이 망 관리 프로토콜(Simple Network Management Protocol: SNMP) 등이 있음



### 전송 계층 (Transport Layer)

- 전송을 담당하는 계층
- TCP뿐만 아니라 사용자 데이터그램 통신규약(User Datagram Protocol: UDP)도 있음
- UDP
  - TCP보다 단순하며 다른 데이터에 비해 안전하게 보호되어야 할 필요가 없는 실시간 응용 프로그램에서 흔히 사용
  - TCP보다 신뢰도가 낮고 오류 검출, 흐름 제어 등의 기능을 제공하지 않아 패킷을 빠르게 전송하는 응용 계층에서 이용
- TCP
  - 두 네트워크 사이에 연결을 형성하고 효율적인 작업을 위해 데이터를 작은 패킷으로 나눠서 전송
- TCP는 연결형 서비스지만 UDP는 비연결형 서비스
- TCP는 신뢰도가 높지만 속도가 느리고, UDP는 신뢰도가 낮지만 속도는 빠름
- TCP 패킷 교환 방식은 가상 회선 방식, UDP는 데이터 그램 방식
- TCP에서는 전송 순서 보장, UDP는 전송 순서가 바뀔 수 있음



### 인터넷 계층 (Internet Layer)

- 네트워크 간 데이터 패킷의 전송을 관리

- IP뿐만 아니라 주소 변환 규약 (Address Resolution Protocol: ARP), 인터넷 그룹 관리 프로토콜(Internet Group Management Protocol: IGMP), 인터넷 제어 메시지 프로토콜(Internet Control Message Protocol: ICMP)도 있음.



### 데이터 링크 계층 (Datalink Layer) 

- 네트워크 인터페이스 계층(Network Interface Layer)이라고도 불림
- 데이터가 원하는 IP주소 (즉, 공유기)에 도달할 뿐만 아니라 해당 네트워크 내의 연결된 기기에 연결되어 있는지 확인
- 원하는 기기의 MAC 주소를 확인하고 이더넷 케이블 및 와이파이를 통한 데이터 전송을 관리하는 등의 작업 담당



## TCP IP 주소

- IP 주소는 매우 다양
  - 공개 IP 주소와 비공개 IP 주소, 정적 IP 주소와 동적 IP 주소가 있음
- TCP/IP는 모든 유형의 IP 주소에서 작동
- 구글 검색창에 "Whats my IP address"라고 치면 나옴
  - 네트워크 내 특정 기기의 IP 주소를 알아낼 수 없음
  - 윈도우의 경우 네트워크 속성에서 IPv4를 찾아보면 됨



### 참고

[TCP/IP와 원리](https://nordvpn.com/ko/blog/tcp-ip-protocol/)

[TCP/IP 쉽게 이해하기](https://aws-hyoh.tistory.com/entry/TCPIP-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0)