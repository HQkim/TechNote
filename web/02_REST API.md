# REST API

### REST API의 탄생

REST는 Representational State Transfer의 약자로 2000년도에 로이 필딩 (Roy Fielding)의 박사학위 논문에서 최초로 소개했다. 로이 필딩은 HTTP의 주요 저자 중 한 사람으로 그 당시 웹(HTTP) 설계의 우수성에 비해 제대로 사용되어지지 못하는 모습에 안타까워하며 웹의 장점을 최대한 활용할 수 있는 아키텍처로서 REST를 발표했다고 한다.



### **REST 구성 요소**

REST는 다음과 같은 3가지로 구성이 되어있다. 

- **자원 (Resource)** : HTTP URI

- **행위 (Verb)** : HTTP Method

- **표현 (Representations)** 



### REST의 특징

1. Uniform Interface (인터페이스 일관성)
   - Uniform Interface는 URI로 지정한 리소스에 대한 조작을 통일되고 한정적인 인터페이스로 수행하는 아키텍처 스타일을 말한다.
2. Stateless (무상태성)
   - REST는 작업을 위한 상태정보를 따로 저장하고 관리하지 않는다. 세션 정보나 쿠키정보를 별도로 저장하고 관리하지 않기 때문에 API 서버는 들어오는 요청만을 단순히 처리하면 된다. 때문에 서비스의 자유도가 높아지고 서버에서 불필요한 정보를 관리하지 않음으로서 구현이 단순해진다.
3. Cacheable (캐시 기능)
   - REST의 가장 큰 특징 중 하나는 HTTP라는 기존 웹표준을 그대로 사용하기 때문에, 웹에서 사용하는 기존 인프라를 그대로 활용이 가능하다. 따라서 HTTP가 가진 캐싱 기능이 적용 가능하다. HTTP 프로토콜 표준에서 사용하는 Last-Modified 태그나 E-Tag를 이용하면 캐싱 구현이 가능하다.
4. Self-descriptiveness (자체 표현 구조)
   - REST API 메시지만 보고도 이를 쉽게 이해할 수 있는 자체 표현 구조로 되어 있다.
5. Client - Server 구조
   - REST 서버는 API 제공, 클라이언트는 사용자 인증이나 컨텍스트(세션, 로그인 정보)등을 직접 관리하는 구조로 각각의 역할이 확실히 구분되기 때문에 클라이언트와 서버에서 개발해야할 내용이 명확해지고 서로간 의존성이 줄어들게 된다.
6. 계층형 구조
   - REST 서버는 다중 계층으로 구성될 수 있으며 보안, 로드밸런싱, 암호화 계층을 추가해 구조상의 유연성을 둘 수 있고 PROXY, 게이트웨이 같은 네트워크 기반의 중간매체를 사용할 수 있게 한다.



### REST API 디자인 가이드

가장 중요한 항목은 다음의 2가지로 요약할 수 있다.

1. URI는 정보의 자원을 표현해야 한다.
2. 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다.

| METHOD |                             역할                             |
| :----: | :----------------------------------------------------------: |
|  POST  |        POST를 통해 해당 URI를 요청하면 리소스를 생성         |
|  GET   | GET를 통해 해당 리소스를 조회. 리소스를 조회하고 해당 도큐먼트에 대한 자세한 정보를 가져온다. |
|  PUT   |                PUT를 통해 해당 리소스를 수정                 |
| DELETE |                 DELETE를 통해 리소스를 삭제                  |



### 참고

[REST API 제대로 알고 사용하기](https://meetup.toast.com/posts/92)

[REST API란? REST, RESTful이란?](https://khj93.tistory.com/entry/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-REST-API%EB%9E%80-REST-RESTful%EC%9D%B4%EB%9E%80)

[REST API 기반에서 리소스를 업데이트 할때는 POST, PUT, PATCH 어떤걸 써야 하나요?](https://repo.yona.io/doortts/blog/issue/12) 