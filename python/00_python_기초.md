# 00. Python 기초



# 식별자

#### 키워드 / 예약어

- 아래의 예약어는 변수명 등으로 사용하지 않아야 한다.

``` python
# python에서 사용할 수 없는 식별자(예약어)는 (python 3.8.5 기준) 다음과 같습니다.
import keyword

print(keyword.kwlist)



#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



# 데이터 타입

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



## String

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

#### String 전체 선택

```python
a = "abcde"
print(a[::]) # "abcde"가 출력
```

#### String 메소드

``` python
# 1 .find(x)
# x의 첫 번째 위치를 반환. 없으면 -1을 반환
'apple'.find('p') # 1
'apple'.find('x') # -1

# 2 .index(x)
# x의 첫 번째 위치를 반환. 없으면 오류 발생
'apple'.index('p') # 1
'apple'.index('x') # 오류발생

# 3. replace(old, new[,count])
# 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
# count를 지정하면, 해당 개수만큼만 시행 ([,count]는 선택인자 - 베커스-나우르 표기법)

# 4. 
# .title() : '나 공백 이후를 대문자로
# .swapcase()
# 대 <-> 소문자로 변경하여

#6.
# isalpha():알파벳 문자 여부 (유니코드 상 Letter(ex.한국어) 포함)
# isupper()
# islower()
# istitle()


```





## Container

- 여러 개의 값을 저장할 수 있는 객체
- 시퀀스(sequence)형 : 순서가 있는 데이터
  - list, tuple, range, string, binary
- 비시퀀스(non-sequence)형: 순서가 없는 데이터
  - set, dictionary



### dictionary

- key와 value가 쌍으로 이뤄진 자료구조
  - key는 변경 불가능한 데이터(immutable)만 활용 가능
    - string, integer, float, boolean, tuple, range
  - value는 모든 값으로 설정 가능 



### List

#### List Method

``` python
# 1.
# .extend(iterable)
# 리스트에 iterable의 항목을 추가함

# 3
# .insert(i, x)
# 정해진 위치 i에 x를 추가함

```

#### List 복사

``` python
# 1. 동일한 주소를 가르킴
a = [1, 2, 3]
b = a
b[0] = 3
print(a) # [3, 2, 3]

# Shallow copy
# 1
a = [1, 2, 3]
b = a[:]

# 2
a = [1, 2, 3]
b = list(a)
b[0] = 5
print(a, b) # [1, 2, 3] [5, 2, 3]

# 얕은 복사 주의사항
# 복사하는 리스트의 원소가 주소를 참조하는 경우
a = [1, 2, ['a', 'b']]
b = a[:]
b[2][0] = 0
print(a, b) # a[2][0]도 변경됨

# Deep copy
import copy
a = [1, 2, ['a', 'b']]
b = copy.deepcopy(a)
b[2][0] = 0
print(a, b) # b만 변함
```

#### List comprehension과 map

```python
# 1
numbers = [1, 2, 3]
a = ''.join([str(num) for num in numbers])
b = ''.join(map(str, numbers))

print(a)
print(b)

# 2 구문
# [<expression> for <변수> in <iterable> if <조건식>]

```



### Set

#### Set 메소드

```python
# .add(elem) : 세트에 값을 추가
a = {'a', 'b'}
a.add('c')
print(a) # 순서없이 출력됨

# .update(*others) : 세트에 여러 값을 추가
a = {'a', 'b'}
a.update(['c', 'd'])
print(a)

# .remove(elem) : 세트에서 삭제하고, 없으면 KeyError
a = {'a', 'b', 'c'}
a.remove('a')
print(a)
a.remove('d')
print(a)

# .discard(elem) : 세트에서 삭제하고 없어도 에러발생 x
a = {'a', 'b', 'c'}
a.discard('a')
print(a)
a.discard('d')
print(a)

# .pop() : 임의의 원소를 제거해 반환


```



### Dictionary

#### Dictionary 메소드

```python
# .get(key[,default])
# key를 통해 value를 가져옴
# KeyError가 발생하지 않으며, default 값을 설정할 수 있음(기본: None)
my_dict = {"apple": "사과", "banana" : '바나나'}
my_dict['pineapple']

print(my_dict.get('pineapple', 0))

# .pop(key[,default])
# key가 딕셔너리에 있으면 제거하고 해당 값을 반환
# 그렇지 않으면 default를 반환
# default값이 없으면 KeyError
my_dict = {"apple": "사과", "banana" : '바나나'}
data = my_dict.pop('apple')
print(data, my_dict)
data = my_dict.pop('pineapple')
print(data, my_dict)
data = my_dict.pop('pineapple', 0)
print(data, my_dict)

# .update()
# 값을 제공하는 key,value로 덮어씁니다.
my_dict = {'apple': "사", 'banana': '바나나'}
my_dict.update(apple="사과")
print(my_dict)

```



#### Dictionary comprehension

``` python
dusts = {'서울': 72, '대전': 81, '구미' : 28, '광주': 34}

{key: value for key, value in dusts.items() if value > 70}
```



# 제어문

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



# 함수

#### Built-in Functions(내장 함수)

- 파이썬 자체에 내장되어 있는 함수들이다.

```
# 써본 함수
abs(), set(), dict(), min(), ascii(), id(), sorted(), enumerate(), input(), int(),
open(), str(), isinstance(), ord(), sum(), filter(), pow(), float(), print(), tuple(),
format(), len(), type(), chr(), list(), range(), zip(), map(), max(), round()

# 안써본 함수
delattr(),hash(),memoryview(),all(), help(), setattr(), any(), dir(), hex(), next(), slice(), divmod(), object(), bin(), oct(), staticmethod(), bool(), eval(), breakpoint(), exec(), bytearray(), issubclass(), super(), bytes(), iter(), callable(), property(), frozenset(), vars(), classmethod(), getattr(),locals(), repr(), compile(), globals(), reversed(), __import__(), complex(), hasattr()
```

- 예시

```python
# 1
# filter(function, iterable)
# 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고,
# 그 결과가 True인 것들을 filter object로 반환
def odd(n):
    return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result))
print(list(result))

# 2 
# zip(*iterables)
# 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
a = ['a', 'b']
b = ['c', 'd']
pair = zip(a, b)
print(pair, type(pair))
print(list(pair))
```





#### 함수의 리턴 규칙

- 함수 리턴은 무조건 하나. "," 로 구분해도 tuple의 type으로 하나의 객체만 리턴된다.



#### parameter와 argument

``` python
def func1(num1, num2): # num1, num2가 parameter(매개변수)
    return num1 + num2

result = func1(10, 20) # 10, 20이 argument(인수)
```

-> def 옆에 있는게 parameter.. 데파..데파.. 대파!?



#### *args, **kwargs

```python
def func1(*args, **kwargs): 
    for i in args:
        print(i)
    for k, v in kwargs.items():
        print(f'{k}: {v}')


func1(1, 2, 3, a=1, b=2)
```

- *args는 가변인자리스트(Arbitrary Argument Lists)

  **kwargs 가변 키워드 인자(Arbitrary Keyword Argument)



#### 위치 인자와 키워드 인자의 순서

- 기본 인자값(Default Argument Value)을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없다.

```python
# 에러상황 1 
def greeting(key1 = 'abc', par1):
	return
# SyntaxError: non-default argument follows default argument

# 에러상황 2
def func1(par1, key1 = "a"):
    return
func1(par1='1', key2)
# SyntaxError: positional argument follows keyword argument

```



#### 꼬리재귀 (tail call recursion)

``` python
def yes_tail(n, ans):
  if n == 1:
    return 1
  return yes_tail(n-1, ans + n)

def no_tail(n):
  if n == 1:
    return 1
  return n + no_tail(n-1)

# 출처: http://melonicedlatte.com/2021/05/10/001900.html
```

- 재귀함수가 메모리를 많이 잡아먹고 성능이 떨어지는 것을 해결하는 방법. 컴파일러에서 가능.



- 고차함수

- 클로저

- 리터럴
  - https://wikidocs.net/20562



# 예외

- 모든 내장된 예외는 Exception Class를 상속받아 이루어져 있음

- 예외처리는 순차적으로 수행되므로 예외는 작은 범주부터 써야 한다.



- try-except-else-finally

  ```python
  try:
      f = open('file.txt')
  except FileNotFoundError:
      print('파일 없음')
  else:
      print('파일 읽기 시작')
      print(f.read())
      print('파일 다 읽었음')
      f.close()
  finally:
      print('파일 읽기 종료')
  ```



- try-except-finally 예시 (finally)

  ```python
  def my_func(a):
      try:
          result = int(a)
          return result
      except:
          return False
      finally:
          print(a)
  
  
  print(my_func('3.5'))
  # 3.5 (string) 
  # False 
  
  
  def my_func2(a):
      try:
          result = int(a)
          return result
      except:
          return False
      print(a)
  
  
  print(my_func2('3.5'))
  # False
  ```

  



#### raise 

- 강제로 예외를 발생



#### assert

- 디버깅 시에 사용
- TDD (Test Driven Developement) 에서 테스트 할 때 사용된다. Django.



# 파이썬



## 파이썬 원칙

#### "Simple is better than complex"

- 특별한 이유 없이 복잡하고 교묘한 코드를 작성하는 것은 좋지 않을 수 있다.

- 중첩이 깊은 경우 억지로 줄이는 것이 코드를 더 이해하기 어렵게 만든다.

- 코드의 가독성은 코드의 간결함보다 훨씬 더 중요한 목표다.

- "프로그래밍은 우리의 프로그램이 어떻게 그 목적을 명확하게 전달하는지에 대한 것"

  

#### EAFP, LBYL 

https://itholic.github.io/python-eafp-lbyl/ 참고

- EAFP
  - "It's Easier to Ask Forgiveness than Permission"
  - try - except 스타일
  - 파이썬에서 권장하는 스타일 https://www.python.org/dev/peps/pep-0463/
  - 파이썬 코드가 문제 없이 실행될 것을 전제로 코드를 실행
- LBYL
  - "Look Before You Leap"
  - if문 스타일
  - 어떤 것이 실행하기 전에 에러가 날만한 요소들을 조건문으로 검사를 하고 실행

-> if문이 try 문에 비해 빠르다.(try는 두번 일하는 꼴. except ㅇ)



## 일반적인 Tip

- 프로그래밍 언어는 크게 정보(변수 등)와 행동(함수 등)으로 이루어진다. 둘을 합친 것이 클래스이다.

- Markdown에서 수학식 표현할 때 LaTex http://pad.haroopress.com/page.html?f=mathematics-expression
