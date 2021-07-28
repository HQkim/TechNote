# 03_OOP_기초

Object Oriented Programming



## 객체와 클래스

### 클래스

- 무언가(객체)를 계속해서 만들어 낼 수 있는 설계 도면
- 속성과 메서드가 있다.
- 클래스의 정의와 객체의 정의 속에 서로를 이용해서 정의하는데 계속 써봐야 익숙해질것 같다.

### 객체

#### 정의

- 객체(object)는 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미.

- 변수, 자료구조, 함수 또는 메소드를 포함할 수 있다.

- 파이썬은 모두 객체(object)로 이뤄져있다.

- 객체는 특정 클래스의 인스턴스(instance) 이다.

#### 특징

- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

#### isinstance 함수

- isinstance(object, classinfo)
  - classinfo의 instance거나 subclass인 경우 True
  - classinfo가 tuple인 경우(type으로 구성된) 하나라도 일치하면 True
  - classinfo가 type으로 구성되지 않은 경우 TypeError

```python
isinstance(10, int)
isinstance(0, (bool, int, complex))
```



## OOP(객체지향 프로그래밍)

### 정의

- 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 프로그래밍 패러다임의 하나

- 절차지향 프로그래밍과 보통 비교된다.



#### 인스턴스 메서드

- 인스턴스가 사용하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨. 동일한 객체에 정의된 속성 및 다른 메서드에 자유롭게 접근 가능
- 뿐만 아니라 클래스 자체에도 접근할 수 있음
  - 즉, 인스턴스 메서드가 클래스 상태를 수정할 수도 있지만 하지 않는다.

```python
class MyClass:
    def instance_method(self, arg1, ...):

my_instance = MyClass()
my_instance.instance_method(...)
```

#### 클래스 메서드

- 클래스가 사용하는 메서드 (인스턴스도 접근 가능하긴함)
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 클래스(cls)가 전달됨. 따라서 객체 인스턴스 상태를 수정할 수 없음

```python
class MyClass:
    
    @classmethod
    def class_method(cls, arg1, ...):
        
MyClass.class_method(...)
```

#### 스태틱 메서드

- 클래스가 사용하는 메서드 (인스턴스도 접근 가능하긴함)
- @staticmethod 데코레이터를 사용하여 정의
- 호출 시, self나 cls가 전달되지 않음 -> 클래스 정보에 접근 및 수정 불가
- 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속됨

```python
class Myclass:
    @staticmethod
    def static_method(arg1, ...):
MyClass.static_method(...)
```

#### 메서드 정리

- 메서드는 해당 함수에서 어떤 값을 활용하고 변경하는지에 따라 정의할 것
  - 인스턴스는 모든 메서드를 호출할 수 있음
    - 하지만, 인스턴스의 동작은 반드시 인스턴스 메서드로 정의
  - 클래스는 클래스 속성 접근 여부에 따라 클래스 메서드, 정적 메서드로 정의



#### 매직 메서드





## 상속

상속 캡슐화 다형성

Solid