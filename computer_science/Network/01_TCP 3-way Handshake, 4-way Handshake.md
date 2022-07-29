# 🤝 TCP 3-way Handshake & 4-way Handshake

### TCP

- Transmission Control Protocol

- TCP는 클라이언트와 서버가 연결된 상태에서 데이터를 주고 받는 연결 지향적 프로토콜

- 데이터를 전송하기 전에 3-way handshaking 과정을 통해 연결을 설정하면 통신 선로가 고정되고, 모든 데이터는 고정된 통신 선로를 통해서 전달

- 클라이언트 데이터 전송이 끝나면 4-way handshaking 과정을 통해 데이터가 모두 전달됐는지 확인

- 따라서, TCP는 데이터를 정확하고 안정적으로 전달할 수 있어 높은 신뢰성을 보장

  - 에러 발생시 재전송을 요청하고 에러를 복구

  

### TCP 제어 플래그

- **TCP Header**에는 **Code Bit(Flag bit)**라는 부분이 존재 **(6bit)**
- 6가지로 구성되며 활성화 되는 값을 비트 “1”로 표현

![image-20220729163613052](01_TCP%203-way%20Handshake,%204-way%20Handshake.assets/image-20220729163613052.png)

1. **URG**: 긴급함을 알림, 긴급 데이터로 우선 순위를 높여 먼저 송신
2. **ACK**: 확인, 수신측에서 송신된 패킷을 정상적으로 받았음을 알림 (Acknowledgement)
3. **PSH**: 버퍼링 되지 않고 바로 송신
4. **RST**: 비정상 상황에서 연결을 끊음
5. **SYN**: 연결을 맺기 위해 보내는 패킷 000010 (Synchronize sequence number)
6. **FIN**: 정상종료, 송신측에서 수신측에 연결 종료 요청



### TCP 3-way Handshake

![image-20220729163639158](01_TCP%203-way%20Handshake,%204-way%20Handshake.assets/image-20220729163639158.png)

1. 클라이언트는 서버에 접속을 요청하는 SYN(x)패킷을 보낸다.
2. 서버는 클라이언트의 요청인 SYN(x)를 받고 클라이언트에게 요청을 수락한다는 ACK(x+1)과 SYN(y)가 설정된 패킷을 보낸다.
3. 클라이언트는 서버의 수락 응답인 ACK(x+1)과 SYN(b)패킷을 받고 ACK(y+1)을 서버로 보내면 연결이 성립된다.



### TCP 4-way Handshake

![image-20220729163657199](01_TCP%203-way%20Handshake,%204-way%20Handshake.assets/image-20220729163657199.png)

1. 클라이언트가 서버에 연결을 종료하겠다는 FIN플래그가 설정된 패킷을 보낸다.
2. 서버는 클라이언트의 요청(FIN)을 받고 알겠다는 확인 메세지로 ACK를 보낸다.
   - 그리고 나서는 데이터를 모두 보낼 때까지 잠깐 TIME_OUT이 된다.
3. 서버가 데이터를 모두 보내고 통신이 끝났으면 연결이 종료되었다고 클라이언트에게 FIN 플래그가 설정된 패킷을 보낸다.
4. 클라이언트는 FIN 메시지를 확인했다는 메시지(ACK)를 보낸다.
   - 클라이언트의 ACK메시지를 받은 서버는 소켓 연결을 close한다.
   - 클라이언트는 아직 서버로부터 받지 못한 데이터가 있을 것을 대비 + FIN 메시지가 서버에 잘 도착하는 것을 보장하기 위해 일정 시간 동안 세션을 남겨놓고 잉여 패킷을 기다리는 과정을 거친다.(TIME_WAIT)

→ 연결 종료



### Why 3-way? 2-way로는 안되나?

- 비유를 하자면 클라이언트가 서버에게 자신의 목소리가 들리는지 물어본다`SYN(x)` . 서버는 클라이언트의 목소리가 들린다고 말한다`ACK(x+1)`. 그리고 서버 자신의 목소리가 들리는지 물어본다`ACK(y)`. 클라이언트는 서버의 목소리가 들린다고 말한다`ACK(y+1)`.
- TCP connection은 양방향성(bidirectional) connection 이기에 클라이언트와 서버가 서로의 존재를 알리고 패킷이 잘 온다는 신호를 보내야 하기 때문에 2-way-handshake로는 부족하다.



### Why randomized sequence number?

- 처음 클라이언트에서 SYN패킷을 보낼 때 Sequence Number에는 랜덤한 숫자(x, y)가 담겨진다. 초기 sequence number를 ISN이라고 한다. ISN이 0부터 시작하지 않고 난수를 생성하는 이유는 무엇일까?
- Connection을 맺을 때 사용하는 포트(port)는 유한 범위 내에서 사용하고 시간이 지남에 따라 재사용된다. 따라서 두 통신 호스트가 과거에 사용된 포트 번호 쌍을 사용하는 가능성이 존재한다. 서버 측에서는 패킷의 SYN을 보고 패킷을 구분하게 되는데 난수가 아닌 순차적인 number가 전송된다면 이전의 connection으로부터 오는 패킷으로 인식할 수 있다. 이러한 문제가 발생할 가능성을 줄이기 위해서 난수로 ISN을 설정하는 것이다.



### 참고자료

[TCP & handshake 쉬운 설명](https://asfirstalways.tistory.com/356)

[TCP 3-way Handshake & 4-way Handshake](https://gmlwjd9405.github.io/2018/09/19/tcp-connection.html)

[TCP & handshake](https://steady-coding.tistory.com/505)

[TCP & handshake2](https://seongonion.tistory.com/74)