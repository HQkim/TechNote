# 03_OOP_기초



## OOP(객체지향 프로그래밍)

### 정의

- Object Oriented Programming

- 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 프로그래밍 패러다임의 하나
- 절차지향 프로그래밍과 보통 비교된다.



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

#### self

- 인스턴스 자기자신
- 파이선에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계

#### 생성자(constructor)

- 인스턴스 객체가 생성될 때 호출되는 메서드

``` python
class Person:
    def __init__(self, name):
        print(f'{name}을 가진 인스턴스 객체 생성')

person1 = Person('HQ')
```

#### 소멸자(destructor)

- 인스턴스 객체가 소멸되기 직전에 호출되는 메서드

```python
class Person:
    def __del__(self):
        print('인스턴스 객체가 소멸됩니다.')
        
person1 = Person()
del person1
```

#### 매직 메서드

- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 혹은 매직 메서드라고 함

- 예시

  ```
  __str__(self) : 객체의 출력 형태 지정
  __gt__(self, other) : 부동호 연산자(>, greater than)에 대한 연산처리
  
  __len__(self), __repr__(self), __lt__(self, other), __le__(self, other), 
  __eq__(self, other) __ge__(self, other), __ne__(self, other)
  
  
  ```

### 클래스와 인스턴스

#### 인스턴스 변수와 클래스 변수

``` python
class Person:
    number_of_person = 0		# 클래스 변수 정의
    def __init__(self, name):
        self.name = name		# 인스턴스 변수 정의
        Person.number_of_person += 1
        
john = Person('john')
jin = Person('Jin')
jin.name = 'Jin Kim' # 인스턴스 변수 접근 및 할당
print(Person.number_of_person) # 클래스 변수 접근
```

#### 인스턴스와 클래스 간의 이름공간(namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 - 



### 메서드 종류

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



## 상속

### 개요

- 클래스는 상속이 가능하다.
  - 모든 파이썬 클래스는 object 클래스를 상속 받음
- 상속을 통해 객체 간의 관계를 구축
- 부모 클래스의 속성, 메서드가 자식 클래스에 상속되므로 코드 재사용성이 높아짐



### 상속 check

- isinstance(object, classinfo)
  - classinfo의 instance거나 subclass인 경우 True
- issubclass(class, classinfo)
  - class가 classinfo의 subclass면 True
  - classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사



#### super()

- 자식클래스에서 부모클래스를 사용하고 싶은 경우

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email    
        self.student_id = student_id
```

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # Person 클래스
        super().__init__(name, age, number, email)
        self.student_id = student_id
```



#### 메서드 오버라이딩(method overriding)

- 상속 받은 메서드를 재정의
  - 상속받은 클래스에서 같은 이름의 메서드로 덮어씀
  - 부모 클래스의 메서드를 실행시키고 싶은 경우 super를 활용

``` python
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
# 자식 클래스 - Professor
class Professor(Person):
    def talk(self):
        print(f'{self.name}일세.')
        
# 자식 클래스 - Student
class Student(Person):
    super().talk()
    print(f'저는 학생입니다.')
    
p1 = Professor('김교수')
p1.talk()

s1 = Student('김학생')
s1.talk()
```

#### 상속 정리

- 파이썬의 모든 클래스는 object로부터 상속
- 부모 클래스의 모든 요소(속성, 메서드)가 상속
- super()를 통해 부모 클래스의 요소를 호출할 수 있음
- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능(메서드 오버로딩은 파이썬에 없음)

- 상속관계에서의 이름 공간은 인스턴스, 자식클래스, 부모클래스 순으로 탐색





## 추가적으로 정리할 것

다중상속 추상화 캡슐화 다형성

Solid

python MRO (class.__mro__)

