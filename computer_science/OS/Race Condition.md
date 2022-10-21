# Race Condition (경쟁 상태)

> 공유 자원에 대해 여러 프로세스(스레드)가 동시에 접근을 시도할 때, 실행되는 순서나 시간 등에 따라 결과가 영향을 받게 되는 상황



### Race Condition이 발생하는 경우

1. **커널 작업을 수행하는 중에 인터럽트 발생**
   - 발생: 커널 모드에서 데이터를 로드하여 작업을 하던 도중 인터럽트가 발생하여 같은 데이터를 조작하는 경우
   - 해결: 커널모드에서 작업을 수행하는 동안 인터럽트를 diable시켜 인터럽트가 CPU제어권을 가져가지 못하도록 하여 해결
2. **프로세스가 시스템 콜을 통해 커널모드로 진입해서 작업을 수행하는 도중에 컨텍스트 스위칭이 발생할 경우**
   - 발생: 프로세스1이 커널모드에서 데이터를 조작하던 도중 시간이 초과되어 CPU제어권이 프로세스2로 넘어가 같은 데이터를 조작하는 경우
   - 해결: 프로세스가 커널모드에서 작업을 하는 경우에는 시간이 초과되더라도 CPU제어권이 다른 프로세스에게 넘어가지 않도록 함
3. **멀티 프로세서에서 공유 메모리 내의 커널 데이터에 접근할 경우**
   - 발생: 멀티프로세스 환경에서 2개의 CPU가 동시에 커널 내부의 공유 데이터에 접근하여 조작하는 경우
   - 해결: 커널 내부에 있는 각 공유 데이터에 접근할 때마다 그 데이터에 대해 lock/unlock함으로써 해결



### 코드로 살펴보는 Race Condition

```java
class Counter {
  int count=0;
  Counter() {
    Thread thread1 = new Thread(new Runnable() {
      @Override
      public void run() {
        count();
      }      
    });
    Thread thread2 = new Thread(new Runnable() {
      @Override
      public void run() {
        count();
      }      
    });
    thread1.start();
    thread2.start();
  }

  void count() {
    for(int i=0; i<100000; i++) {
      count++;
    }
  }
}
```

- 위에서처럼 두개의 스레드 thread1과 thread2가 돌아가면, count가 예상한 20만이 아니라 109012, 107496 등 10만에 가까운 값이 실행할 때마다 결과가 다르게 나온다.

- 자세한 과정을 살펴보면
  1. 스레드 1이 count의 값 0을 받아온다.
  2. 스레드 1이 0에 1을 더한다.
  3. 컨텍스트 스위칭(작업하는 스레드를 바꿈)을 한다.
  4. 스레드 2가 count의 값 0을 받아온다.
  5. 스레드 2가 0에 1을 더한다.
  6. 컨텍스트 스위칭을 한다.
  7. 스레드 1이 더한 값 1을 count에 쓴다.
  8. **스레드 2가 더한 값 1을 count에 쓴다.**

- 이런 경우, lock/unlock을 통해 문제를 해결할 수 있다.



### 참고 자료

[[운영체제] 경쟁 상태 (Race Condition)](https://velog.io/@klloo/%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C-%EA%B2%BD%EC%9F%81-%EC%83%81%ED%83%9C-Race-Condition)

[경쟁 상태(Race Condition)](https://gyoogle.dev/blog/computer-science/operating-system/Race%20Condition.html#%E1%84%80%E1%85%A7%E1%86%BC%E1%84%8C%E1%85%A2%E1%86%BC-%E1%84%89%E1%85%A1%E1%86%BC%E1%84%90%E1%85%A2-race-condition)

[경쟁 상태](https://namu.wiki/w/%EA%B2%BD%EC%9F%81%20%EC%83%81%ED%83%9C)