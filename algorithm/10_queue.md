# 10_큐(Queue)

#### 큐의 특성

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조

  - 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조

- 선입선출구조(FIFO)

  - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입(First In)된 원소는 가장 먼저 삭제(First Out)된다.

  - 머리(Front) - 저장된 원소 중 첫번쨰 원소 (또는 삭제된 위치)
  - 꼬리(Rear) - 저장된 원소 중 마지막 원소

#### 큐의 연산

- 삽입 : enQueue	(# enqueue와 같이 써주면 큐인걸 말하는 것)
- 삭제 : deQueue
- 공백상태 검사 : isEmpty()
- 포화상태 검사 : isFull()
- 공백 상태 큐 생산 : createQueue()
- 큐의 앞쪽(front)에서 원소를 삭제 없이 반환 : Qpeek()



## 선형큐

#### 선형큐

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
- 상태 표현
  - 초기 상태 : front = rear = -1
  - 공백 상태 : front = rear
  - 포화 상태 : rear = n-1 (n: 배열의 크기, n-1 : 배열의 마지막 인덱스)

#### 큐의 구현

1. 삽입: enQueue(item)

- 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
  1. rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
  2. 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장

````
def enQueue(item) :
	global rear
	if isFull() : print("Queue Full")
	else:
		rear <- rear + 1
		Q[rear] <- item
````

2. 삭제 : deQueue()
   - 가장 앞에 있는 원소를 삭제하기 위해
     1. front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
     2. 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능을 함

```
deQueue()
	if(isEmpty()) then Queue_Empty();
	else{
		front <- front + 1
		return Q[front]
	}
```

3. 공백상태 및 포화상태 검사 : isEmpty(), isFull()
   - 공백상태 : front = rear
   - 포화상태 : rear = n-1 (n: 배열의 크기, n-1 : 배열의 마지막 인덱스)

``` 
def isEmpty():
	return front == rear
	
def Full():
	return rear = len(Q) -1
```

4. 검색 : Qpeek()
   - 가장 앞에 있는 원소를 검색하여 반환
   - 현재 front의 한자리 뒤(front+1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환

```
def Qpeek():
	if isEmpty() : print("Queue_Empty")
	else : return Q[front+1]
```



#### 구현 팁

- 위와 같이 인덱스(front, rear)로 접근을 하는 것이 가장 빠르다.
- 리스트의 append()는 새로 만들어서 복사붙여넣기 하는 것.
- 속도 : 인덱스 > deque > 리스트 append, pop(0)



## 원형큐

#### 원형 큐의 구조

![image-20210825101834919](10_queue.assets/image-20210825101834919.png)

- 초기 공백 상태

  - front = rear = 0

- Index의 순환

  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야함
  - 이를 위해 나머지 연산자 mod를 사용

- front 변수

  - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

- 삽입 위치 및 삭제 위치

  선형큐 : 삽입위치 - rear = rear + 1, 삭제 위치- front = front+1

  원형큐 : 삽입위치- rear = (rear+1) mod n, 삭제 위치 - front = front(front+1) mod n

#### 원형 큐의 연산 과정

1. 공백상태 및 포화상태 검사 : isEmpty(), isFull()

   - 공백 상태 : front = rear
   - 포화 상태 : 삽입할 rear의 다음 위치 = 현재 front
     - (rear+1)mod n = front

   ```
   def isEmpty() :
   	return front == rear
   	
   def isFull() :
   	return (rear+1) % len(cQ) == front
   ```

2. 삽입 : enQueue(item)

   - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
     1. rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련함 : rear <- (rear+1) mod n
     2. 그 인덱스에 해당하는 배열원소 cQ[rear]에 item을 저장

   ```
   def enQueue(item):
   	global rear
   	if isFull():
   		print("Queue_Full")
   	else:
   		rear = (rear + 1) % len(cQ)
   		cQ[rear] = item
   ```

3. 삭제 : deQueue(), delete()

   - 가장 앞에 있는 원소를 삭제하기 위해
     1. front 값을 조정하여 삭제할 자리를 준비함
     2. 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능함

   ```
   def deQueue() :
   	global front
   	if isEmpty():
   		print("Queue_Empty")
   	else:
   		front = (front + 1) % len(cQ)
   		return cQ[front]
   
   def delete():
   	global front
   	if isEmpty():
   		print("Queue_Empty")
   	else:
   		front = (front + 1) % len(cQ)
   ```

   

## 연결큐

Linked list

## 우선순위 큐

#### 우선순위 큐

- 우선순위 큐의 특성
  - 우선순위를 가진 항목들을 저장하는 큐
  - FIFO순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.
- 우선순위 큐의 적용 분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제의 테스크 스케쥴링
- 우선순위 큐의 구현
  - 배열 이용
  - 연결리스트 이용
- 우선순위 큐의 기본 연산
  - 삽입: endQueue
  - 삭제: deQueue

#### 배열을 이용한 우선순위 큐

- 배열을 이용하여 우선순위 큐 구현
  - 배열을 이용하여 자료 저장
  - 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
  - 가장 앞에 최고 우선순위의 원소가 위치하게 됨
- 문제점
  - 배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생
  - 이에 소요되는 시간이나 메모리 낭비가 큼



## 큐의 활용 : 버퍼

#### 버퍼(Buffer)

- 버퍼
  - 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역
  - 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미
- 버퍼의 자료 구조
  - 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
  - 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용.



