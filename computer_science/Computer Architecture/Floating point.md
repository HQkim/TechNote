# 부동소수점(Floating point)

### 고정 소수점

![고정 소수점 방식](Floating%20point.assets/img_c_fixed_point.png)

- 정수를 표현하는 비트 수와 소수를 표현하는 비트 수를 **미리 정해 놓고**, 해당 비트 만큼만 사용해서 숫자를 표현하는 방식

- ex) 실수 표현에 4bye(32bit)를 사용하고 부호 1bit, 정수 15bit, 소수 16bit를 사용한다고 해보자.

  263.3을 표현하면 (0)000000100000111.0100110011001100이 된다.

- 정수를 표현하는 bit를 늘리면 큰 숫자를 표현할 수 있지만, **정밀한 숫자를 표현하기 힘들다**. 그래서 소수를 표현하는 bit를 늘리면 정밀한 숫자를 표현할 수 있지만 **큰 숫자를 표현하지 못한다**.



### 부동 소수점

![32비트 부동 소수점](Floating%20point.assets/img_c_floating_point_32.png)

- 다양한 방식이 있지만, 일반적으로 **IEEE 754**에서 표준화한 방식을 사용
- **부호 비트(1bit), 지수 비트(8bit), 가수 비트(23bit)**
- ex) 263.3을 2진수로 표현했을 때 **100000111.010011001100110..**가 되는데 1 바로 뒤로 소수점을 옮겨서 표현하면 **1.00000111010011001100110... * 2^8**가 된다. (263.3을 2진수로 나타내는 방법은 이 [유투브 영상](https://www.youtube.com/watch?v=8afbTaA-gOQ)을 보면 이해하기 좋다.)  
  - 부호 비트(1 bit) : 0 (양수)
  - 지수 비트(8 bit) : 10000111 (127 + 8 = 135)
  - 가수 비트(23 bit) : 00000111010011001100110
- 64비트 double형 실수는 다음과 같다

![64비트 부동 소수점](Floating%20point.assets/img_c_floating_point_64.png)

- 지수 비트에서 127을 bias로 두는 이유는 다음과 같이 음의 지수를 두기 위함이다.

  - 0000 0000 : -127

  - 0000 0001 : -126

    ...

  - 0111 1111 : 0

  - 1111 1110: 127

  - 1111 1111: 가수부의 비트가 모두 1인 경우 inf(무한)을 나타내고, 모두 1이 아닌 경우는 nan(미정값)을 나타낸다.

### 부동 소수점의 오류

- 앞서서 263.3에서 0.3을 2진수로 나타내보면 0.0**100110011001**10..과 같이 소수점 아래로 무한히 반복되고 이를 부동 소수점 방식에서는 23bit(혹은 52비트)에서 끊어서 저장하게 된다. 따라서 저장된 값은 엄밀히 말하면 263.3과 동일하지 않다.

- 따라서, 0.3을 10번 더하면 3이 나와야 할 것 같지만 실제로는 2.9999999999999996과 같은 근사치가 나오게 된다.

  ```python
  answer = 0
  for i in range(10):
      answer += 0.3
  print(answer)	# 2.9999999999999996
  ```

- 따라서 두 실수가 같은지 판단할 때는 등호 연산(==)을 사용하면 안된다. 이 때는, 연산한 값과 비교할 값의 차이를 구한 뒤 오차범위 내에 있는지로 확인한다. 파이썬에서는 `sys.float_info.epsilon`과 같은 값이나, `math.isclose()`메소드를 이용할 수도 있다.

  ```python
  import math, sys
  
  answer = 0
  for i in range(10):
      answer += 0.3
  
  if math.fabs(answer - 3) <= sys.float_info.epsilon:
      print("3과 같음")
  else:
      print("3과 다름") 				# 출력됨
      
  print(sys.float_info.epsilon)	  # 2.220446049250313e-16
  print(math.isclose(answer, 3))	  # True
  ```

  - [Python math.isclose() Method](https://www.w3schools.com/python/ref_math_isclose.asp)

    

### 참고

http://www.tcpschool.com/cpp/cpp_datatype_floatingPointNumber

[부동 소수점(Floating Point)란 무엇인가?](https://steemit.com/kr/@modolee/floating-point)

[Decimal to IEEE 754 Floating Point Representation](https://www.youtube.com/watch?v=8afbTaA-gOQ)

[실수 값의 오차(파이썬)](https://dojang.io/mod/page/view.php?id=2466)

[부동소수점에 대한 이해](https://thrillfighter.tistory.com/349)