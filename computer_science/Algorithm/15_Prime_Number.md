# 소수 구하기

### 특정한 수가 소수인지 판별하기

**코드**

```python
import math

def check_prime_number(n):
    # 2부터 n의 제곱근까지
    for i in range(2, int(math.sqrt(n)) + 1):
        # n이 해당 수로 나누어 떨어진다면
        if n % i == 0:
            return False # 소수가 아님
    return True	# 소수가 맞음

print(check_prime_number(7))
```

**설명**

- 소수의 정의는, 1과 자기 자신을 제외하고는 나누어 떨어지지 않는다는 것이다.
- 그런데 이 때, 2부터 n-1까지 모두 나누어 보는 것이 아니라 `n의 제곱근`까지만 체크하면 된다!
  - 왜냐하면 `n = a * b`라고 했을 때, `a > sqrt(n)` 이라면 `b < sqrt(n)`이기 때문이다.
  - 즉, sqrt(n)보다 작은 수까지만 체크하면, 모든 a * b 쌍에 대해서 체크하는 경우와 같다.
- 시간복잡도는 O(`n의 제곱근`)
- 2 ~ 1,000,000 안에 소수들을 **모두** 찾는 방법으로는 비효율적



### 에라토스테네스의 체

![에라토스테네스의 체](15_Prime_Number.assets/Sieve_of_Eratosthenes_animation.gif)

**코드**

```python
import math

N = 1000 
arr = [1 for i in range(N + 1)] 

# 에라토스테니스의 체 알고리즘
for i in range(2, int(math.sqrt(N)) + 1): 
    if arr[i]: 
        j = 2
        while i * j <= N:       # i의 모든 배수 지우기
            arr[i * j] = 0
            j += 1

for i in range(2, N + 1):
    if arr[i]:
        print(i, end=" ")
```



**설명**

- 위와 마찬가지로 2~`n의 제곱근` 까지 순회하면서
- 아직 지워지지 않은 수들에 한해서
  - 범위(2~n) 안에서 자기 자신을 제외하고 각 수의 배수들을 지운다.

- 지워지지 않은 수들이 소수이다.
- 시간복잡도: O(Nlog(logN))
  - N이 1,000,000이라면 Nlog(logN)은 4,000,000정도로 거의 선형적
- 메모리가 많이 필요하기 때문에, 10억이 소수인지 찾기 위해서는 위의 소수판별법을 써야함



### 참고

[[알고리즘] 수학#3 소수판별](https://iamsjy17.github.io/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98_%EC%88%98%ED%95%99/2019/06/03/mathproblem3.html)

[[알고리즘] 소수의 판별 - 에라토스테네스의 체](https://velog.io/@changhee09/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%86%8C%EC%88%98%EC%9D%98-%ED%8C%90%EB%B3%84-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4)

[위키백과](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)