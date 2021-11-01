# 02_JavaScript_비동기

> ### AJAX

#### AJAX란?

- Asynchronous JavaScript And XML (비동기식 JavaScript와 XML)
- 서버와 통신하기 위해 XMLHttpRequest 객체를 활용
- JSON, XML, HTML 그리고 일반 텍스트 형식 등을 포함한 다양한 포맷을 주고 받을 수 있음

#### 특징

- 페이지 전체를 reload(새로고침) 하지 않아도 수행되는 "비동기성"

#### XMLHttpRequest 객체

- 서버와 상호작용하기 위해 사용되며 전체페이지의 새로고침 없이 데이터를 받아올 수 있음
- 사용자의 작업을 방해하지 않으면서 페이지 일부를 업데이트 할 수 있음
- 주로 AJAX프로그래밍에 사용되면 XML 뿐만 아니라 모든 종류의 데이터를 받아올 수 있음



> ### Asynchronous JavaScript

#### 동기식과 비동기식

JavaScript의 동기식과 비동기식은 모두 single threaded 구조에서 나온다

single thread이기 때문에 한번에 하나의 작업만 수행할 수 있음

![image-20211101213139735](02_javascript_%EB%B9%84%EB%8F%99%EA%B8%B0.assets/image-20211101213139735.png)

​																																				[사진 출처](https://velog.io/@dorazi/Asynchronous-VS-Synchronous)

- 동기식

  ```javascript
  const = btn = document.querySelector('button')
  
  btn.addEventListner('click', function () {
      alert('Clicked!')
      const pElem = document.createElement('p')
      pElem.innerText = '클릭 다음'
      document.body.appendChild(pElem)
  })
  ```

  - alert 이후 코드는 alert의 처리가 끝날 때까지 실행되지 않음

- 비동기식

  ```javascript
  const request = new XMLHttpRequest()
  const URL = 'https://jsonplaceholder.typicode.com/todos/1/'
  
  request.open('GET', URL)
  request.send()
  
  const todo = request.response
  console.log(`data: ${todo}`)
  ```

  - todo에 응답 데이터가 할당되지 않고 빈 문자열 출력

#### Concurrency model

- Event loop를 기반으로 하는 동시성 모델

1. Call Stack
   - 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack(LIFO)형태의 자료 구조
2. Web API (Browser API)
   - JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API
   - setTimeout(), DOM events, AJAX로 데이터를 가져오는 시간이 소요되는 일들을 처리
3. Task Queue (Event Queue, Message Queue)
   - 비동기 처리된 callback 함수가 대기하는 Queue(FIFO)형태의 자료 구조
   - main thread가 끝난 후 실행되어 후속 JavaScript 코드가 차단되는 것을 방지
4. Event Loop
   - Call Stack이 비어 있는지 확인
   - 비어 있는 경우 Task Queue에서 실행 대기 중인 callback 함수가 있는지 확인
   - Task Queue에 대기 중인 callback 함수가 있다면 가장 앞에 있는 callback 함수를 CallStack으로 push

- eventloop 확인하는 사이트

  http://latentflip.com/loupe/?code=JC5vbignYnV0dG9uJywgJ2NsaWNrJywgZnVuY3Rpb24gb25Db

#### Zero delays

```javascript
console.log('1')

setTimeout(function () {
    console.log('2')
}, 0)

console.log('3')
```

- 위의 실행결과는 1 -> 3 -> 2
- delay는 JavaScript가 요청을 처리하는 데 필요한 최소 시간이기 때문(보장된 시간이 아님)
- setTimeout 함수에 특정 시간제한을 설정했더라도 대기 중인 메시지의 모든 코드가 완료될 때까지 대기해야함



> ### Callback Function

#### Callback function

- 다른 함수에 인자로 전달된 함수
- 외부 함수 내에서 호출되어 일종의 루틴 또는 작업을 완료함
- 동기식, 비동기식 모두 사용됨
  - 보통 비동기 작업이 완료된 후 코드 실행을 계속하는데 주로 사용됨
  - 이를 비동기 콜백(Asynchronous callback)이라고 함

#### 일급객체(First Class Object)

- JavaScript의 함수는 일급객체
- 일급객체의 조건
  1. 인자로 넘길 수 있어야 함
  2. 함수의 반환 값으로 사용할 수 있어야 함
  3. 변수에 할당할 수 있어야 함

#### callback Hell

- 여러 개의 연쇄 비동기 작업을 할 때 마주하는 상황

![img](https://miro.medium.com/max/1400/0*C0iEvjGNPURJcqrI.jpeg)

​																																								[사진 출처](https://medium.com/@kyle_seongwoo_jun/%EC%BD%9C%EB%B0%B1-%ED%97%AC%EC%9D%84-async-await%EB%A1%9C-c-taskcompletionsource-9433dfd61eec)

- 해결하기
  1. Keep your code shallow (코드의 깊이를 얕게 유지)
  2. Modularize (모듈화)
  3. Handle every single error (모든 단일 오류 처리)
  4. Promise callbacks (Promise 콜백 방식 사용)



> ### Promise

#### Promise object

- 비동기 작업의 최종 완료 또는 실패를 나타내는 객체
  - 미래의 완료 또는 실패와 그 결과 값을 나타냄
  - 미래의 어떤 상황에 대한 약속

#### Promise methods

- 성공(이행)에 대한 약속
  - .then(callback)
  - callback 함수는 이전 작업의 성공 결과를 인자로 전달 받음
  - 따라서 성공했을 때의 코드를 callback 함수 안에 작성
- 실패(거절)에 대한 약속
  - .catch(callback)
  - .then이 하나라도 실패하면(거부 되면) 동작 (동기식의 'try - except' 구문과 유사)
  - 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용 가능
- 주의
  - **성공과 실패는 반환 값이 반드시 있어야 함**
- 결과와 상관 없이 무조건 실행
  - .finally(callback)
  - Promise 객체를 반환
  - 어떠한 인자도 전달 받지 않음

#### Promise가 보장하는 것

- Async callback 작성 스타일과 달리 Promise가 보장하는 특징

1. callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
   - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
3. .then()을 여러번 사용하여 여러 개의 callback 함수를 추가할 수 있음(Chaining)
   - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
   - Chaining은 Promise의 가장 뛰어난 장점



> ### Axios

#### Axios

- "Promise based HTTP client for the browser and Node.js"
- 브라우저를 위한 Promise 기반 클라이언트
- 원래는 "XHR"이라는 브라우저 내장 객체를 활용해 AJAX요청을 처리하는데, 이보다 편리하게 AJAX 요청이 가능하도록 도와줌
  - 확장 가능한 인터페이스와 함께 사용이 간편한 라이브러리를 제공

#### 예제 코드

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dog API</title>
  <style>
    img {
      height: 500px;
    }
  </style>
</head>

<body>
  <h1>Dog API</h1>
  <img src="" alt="dog">
  <br>
  <button>Get dog</button>

  <!-- axios CDN을 삽입한다. -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const API_URI = 'https://dog.ceo/api/breeds/image/random'

    function getDog() {
      // axios를 사용하여 API_URI로 GET 요청을 보낸다.
      axios.get(API_URI)
        // .then 메서드를 통해 요청이 성공적인 경우의 콜백함수를 정의한다.
        .then(response => {
          return response.data
        })
        // 응답객체의 데이터에서 이미지에 대한 리소스를 img 요소의 src 속성으로 할당한다.
        .then(data => {
          const imgUrl = data.message
          const imgTag = document.querySelector('img')
          imgTag.src = imgUrl
        })
    }

    const button = document.querySelector('button')
    button.addEventListener('click', getDog)
  </script>
</body>

</html>
```



> ### async & await

- 비동기 코드를 작성하는 새로운 방법
  - ECMAScript 2017(ES8)에서 등장
- 기존 Promise 시스템 위에 구축된 syntatic sugar
  - Promise 구조의 then chaining을 제거
  - 비동기 코드를 조금 더 동기 코드처럼 표현
  - Syntactic sugar
    - 더 쉽게 읽고 표현할 수 있도록 설계된 프로그래밍 언어 내의 구문
    - 즉, 문법적 기능은 그대로 유지하되 사용자가 직관적으로 코드를 읽을 수 있게 만듬

