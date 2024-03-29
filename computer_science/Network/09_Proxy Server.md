# Proxy Server

### Proxy Server?

- 프록시 서버는 클라이언트가 자신을 통해서 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해 주는 컴퓨터 시스템이나 응용 프로그램이다.
- 서버와 클라이언트 사이에 중계기로서 대리로 통신을 수행하는 것을 `프록시`라 하고, 그 중계 기능을 하는 것을 `프록시 서버` 라고 부른다.
- 프록시 서버 중 일부는 프록시 서버에 요청된 내용들을 `캐시`를 이용하여 저장해 둔다.
  - 캐시 안에 있는 정보를 요구하는 요청에 대해서는 원격 서버에 접속하여 데이터를 가져올 필요가 없기에, 전송 시간을 절약할 수 있게 됨과 동시에 불필요하게 외부와의 연결을 하지 않아도 된다는 장점이 있음.
  - 또한, 외부와의 트래픽을 줄여 네트워크 병목 현상을 방지

![File:Open proxy h2g2bob.svg](09_Proxy%20Server.assets/400px-Open_proxy_h2g2bob.svg.png)



### Forward Proxy

- 클라이언트가 인터넷에 직접 접근하는게 아니라 포워드 프록시 서버가 요청을 받고 인터넷에 연결하여 결과를 클라이언트에 전달(forward) 해준다.
- 프록시 서버는 Cache를 사용하여 자주 사용하는 데이터라면 요청을 보내지 않고 캐시에서 가져올 수 있기 때문에 성능 향상이 가능하다.
- End Point
  - 클라이언트가 요청하는 End Point가 **실제 서버 도메인**이고 프록시는 둘 사이의 통신을 담당해준다.
- 클라이언트가 감춰진다. 요청 받는 서버는 프록시 서버를 통해서 요청을 받기 때문에 클라이언트의 정보를 알 수 없다.

![img](09_Proxy%20Server.assets/forward-proxy.png)

### Reverse Proxy

- 클라이언트가 인터넷에 데이터를 요청하면 리버스 프록시가 이 요청을 받아 내부 서버에서 데이터를 받은 후 클라이언트에 전달한다.
- 클라이언트는 내부 서버에 대한 정보를 알 필요 없이 **리버스 프록시에만 요청**하면 된다.
- 내부 서버 (WAS)에 직접적으로 접근한다면 DB에 접근이 가능하기 때문에 중간에 리퍼스 프록시를 두고 클라이언트와 내부 서버 사이의 통신을 담당한다.
- 또한 내부 서버에 대한 설정으로 로드 밸런싱(Load Balancing)이나 서버 확장 등에 유리하다.
- End Point
  - 클라이언트가 요청하는 End Point 가 **프록시 서버의 도메인**이고 실제 서버의 정보는 알 수 없다.
- 서버가 감춰진다. 클라이언트는 리버스 프록시 서버에게 요청하기 때문에 실제 서버의 정보를 알 수 없다.

![img](09_Proxy%20Server.assets/reverse-proxy.png)





### Proxy 서버의 목적

1. **캐시**
   - 캐시를 사용하여 리소스로의 접근을 빠르게 하기 위해 사용할 수 있다.
2. **보안**
   - 프록시 서버가 중간에 경유되게 되면 IP를 숨길 수 있다. 또한 프록시 서버를 방화벽으로 사용하기도 한다.(프록시 방화벽)
3. **접속 우회**
   - 한국에서 접속이 제한이 되는 사이트는 IP를 검사해 한국에서의 접속을 감지한다. 이 경우 프록시 서버를 사용하면 접속을 다른나라로 우회할 수 있게 된다. 



### 참고

[프록시 서버(위키백과)](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9D%EC%8B%9C_%EC%84%9C%EB%B2%84)

[Forward Proxy, Reverse Proxy 정의와 차이점](https://bcp0109.tistory.com/194)

[[네트워크] 프록시 서버란? 원리와 사용 목적](https://liveyourit.tistory.com/251)