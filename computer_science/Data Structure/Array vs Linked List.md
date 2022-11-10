# Array vs Linked List

## Array(배열)

### Array란?

> **고정된 크기**를 갖는 **같은 자료형**의 원소들이 **연속적**인 형태로 구성된 자료구조

![image-20221110172144652](Array%20vs%20Linked%20List.assets/image-20221110172144652.png)

- 배열 안의 데이터들은 **같은 자료형**으로 나열되어 있음
- 데이터가 **연속된 메모리** 공간에 **순차적**으로 저장
- 따라서 배열의 **논리적 순서(인덱스)**와 원소값의 **물리적인 순서(메모리 주소)가 동일**함

### 장점

- **인덱스**를 가지고 있기 때문에, **탐색**이 빈번한 경우 효율적
- **연속된 메모리 공간**에 존재하기 때문에 관리가 수월

### 단점

- **삽입/삭제가 어렵다**
  - 삽입/삭제는 해당 위치에서 작업 후, 해당 원소 뒤의 모든 원소들을 이동(shift)시켜야 하기 때문

- 배열은 처음 생성할 때 크기를 선언하면, **그 크기를 변경할 수 없음**

### 시간 복잡도

```
삽입/삭제
- 배열의 맨 앞에 삽입/삭제: O(n)
- 배열의 맨 뒤에 삽입/삭제: O(1)
- 배열의 중간에 삽입/삭제: O(n)

탐색 및 수정: O(1)
```





<br/>

## Linked List

### 링크드 리스트란?

> **노드를 연결**해 데이터를 적재하는 자료구조

- 배열의 문제점을 해결하기 위한 자료구조
- **인덱스가 없음**
- **불연속적인 메모리 공간**에 **원소와 다음 노드의 주소**를 가진 노드가 계속해서 이어져 있어 선형의 형태를 유지



![image-20221110172259730](Array%20vs%20Linked%20List.assets/image-20221110172259730.png)

![image-20221110172309892](Array%20vs%20Linked%20List.assets/image-20221110172309892.png)

### 장점

- **삽입/삭제** 시 전후 노드의 **참조관계만 수정**하면 되기 때문에 **효율적**
- **크기가 가변적**
- **메모리 낭비가 적다**
  - 연속적으로 메모리를 할당할 필요가 없어서 메모리 낭비가 적음
  - 메모리 재사용 가능 (삭제 시 해당 노드의 참조가 사라져 GC에 의해 가용 메모리로 전환)

### 단점

- **구현이 상대적으로 복잡**하다
- 인덱스 탐색이 안되기에 **탐색이 비효율적**이다 (처음부터 순차적으로 검색해야함)
- 다음 노드의 주소를 저장하는 **메모리 추가적으로 필요**

### 시간 복잡도

```
삽입
- 리스트의 맨 앞에 삽입: O(1)
- 리스트의 중간에서 삽입: O(n)

삭제
- 리스트의 맨 뒤에 삽입/삭제: O(1)
- 리스트의 중간에서 삭제: O(n)

탐색: O(n)
```

### 리스트의 다양한 종류

- 단일 연결 리스트(Single Linked List)

  ![image-20221110173456548](Array%20vs%20Linked%20List.assets/image-20221110173456548.png)

- 이중 연결 리스트(Double Linked List)

  ![image-20221110173503961](Array%20vs%20Linked%20List.assets/image-20221110173503961.png)
- 원형 연결 리스트(Circular Linked List)

  ![image-20221110173510209](Array%20vs%20Linked%20List.assets/image-20221110173510209.png)
- 순환 이중 연결 리스트(Dobuly Circular Linked LIst)

  ![image-20221110173518585](Array%20vs%20Linked%20List.assets/image-20221110173518585.png)

<br/>

### 참고

[[자료구조] 배열과 리스트(Array & List)](https://bigsong.tistory.com/31)

[[ 자료구조 ] 배열(Array) vs 리스트(List) - 특징, 차이](https://jy-tblog.tistory.com/38)

[Linked List vs Array](https://www.geeksforgeeks.org/linked-list-vs-array/)

[What is a Linked List? Linked List vs Array](https://medium.com/@yk392/what-is-a-linked-list-linked-list-vs-array-92f0db4015cc)

[배열과 리스트의 차이](https://bb-dochi.tistory.com/9)
