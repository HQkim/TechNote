# 00. Python 기초



## 식별자

#### 키워드 / 예약어

- 아래의 예약어는 변수명 등으로 사용하지 않아야 한다.

``` python
# python에서 사용할 수 없는 식별자(예약어)는 (python 3.8.5 기준) 다음과 같습니다.
import keyword

print(keyword.kwlist)



#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



## 데이터 타입

#### Floating point rounding error

- 부동소수점(Float)에서 연산 과정에서 생길 수 있다. 따라서 실수 값을 비교할 때는 주의해야 한다.

  ``` python
  a = 0.1*3
  b = 0.3
  
  # 1. 방법 1
  abs(a - b) <= 1e-10
  
  # 2. 방법 2 
  import sys
  
  print(abs(a - b) <= sys.float_info.epsilon)
  print(sys.float_info.epsilon)
  
  # 3. 방법 3
  import math
  math.isclose(a, b)
  ```


#### Strig Interpolation

- 문자열을 변수로 활용하여 만드는 법

  - %-formatting
  - str.format()
  - f-strings: python 3.6+ -> 빠르다. 버전이 맞으면 이걸 사용할 것.

  ``` python
  import datetime
  today = datetime.datetime.now()
  
  print(today)
  print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일')
  
  pi = 3.141592
  print(f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2**2}')
  ```


#### string 뒤집기 (list 도 가능)

``` python
a = "abcde" # a = [1, 2, 3, 4]
print(a[::-1])
```





## Container

- 여러 개의 값을 저장할 수 있는 객체
- 시퀀스(sequence)형 : 순서가 있는 데이터
  - list, tuple, range, string, binary
- 비시퀀스(non-sequence)형: 순서가 없는 데이터
  - set, dictionary

#### dictionary

- key와 value가 쌍으로 이뤄진 자료구조
  - key는 변경 불가능한 데이터(immutable)만 활용 가능
    - string, integer, float, boolean, tuple, range
  - value는 모든 값으로 설정 가능 



## 조건문

#### 조건 표현식(Conditional Expression) == 삼항 연산자(Ternary Operator)

``` python
number = int(input())
answer = 1 if number >= 0 else -number 
# 하지만 짧은 코드가 항상 좋은 코드인 것만은 아니다. 다른 사람과 협업할 때 읽기 좋아야.
```



## 반복문

#### enumerate

``` python
cities = ['서울', '대전', '부산']

print(list(enumerate(cities)))
print(list(enumerate(cities, start= 1)))
```

#### for-else

- for문이 정상적으로 다 돌게 되면 else문 실행 

``` python
for alphabet in "abcd":
    if alphabet == "e":
        print("e")
        break
else:
    print("e가 없습니다.")
    
for alphabet in "abcde":
    if alphabet == "e":
        print("e")
        break
else:
    print("e가 없습니다.")
```



## 기타

### * 사용법

```python
# 1
a = ['h', 'i']
c = ['b', 'y', 'e']
print([*a, 'w', *c])

# 2
lista = list(range(10))
listb = lista[:5]
listc = lista[5:]
print([*listb, *listc])

# 3
numbers = [1, 2, 3, 4, 5, 6]
*a, = numbers
print(*a)

*a, b = numbers
print(*a, '///', b)

a, *b = numbers
print(a, '///', *b)

a, *b, c = numbers
print(a, '/', *b, '/', c)

a, b, *lista, c = numbers

print(a, '/', b, '/', *lista, '/', c)
```





## 일반적인 Tip

- 프로그래밍 언어는 크게 정보(변수 등)와 행동(함수 등)으로 이루어진다. 둘을 합친 것이 클래스이다.

- Markdown에서 수학식 표현할 때 LaTex http://pad.haroopress.com/page.html?f=mathematics-expression
