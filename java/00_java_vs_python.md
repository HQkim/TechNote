# Java vs Python

### 1. Java는 정적타이핑, Python은 동적 타이핑

Java에서는 변수를 선언할 때 개발자가 데이터 타입을 명시해 주어야 한다. 이를 정적 타이핑이라고 한다.

```java
public class Main {
    public static void main(String[] args) {
        int x = 1, y = 2;
        int result = x + y;
        System.out.println("x + y = " + result);
    }
}
```

반면에 Python은 동적타이핑 언어로서 런타임에서 데이터 타입이 해석된다.

```python
x = 1
y = 2
print('x + y = ', x + y)
```



Python에서 동적 타이핑은 개발자를 편리하게 만들어주는 요소 중 하나이다. 하지만 주석을 잘 작성하지 않는 등의 이유로 인해서 실행 과정에서 타입에러로 이어질 수 있다. 반면에 정적 타이핑은 개발 과정에서는 일일히 타입을 지정해야 하는 수고가 있지만 컴파일 단계에서 에러를 잡아줘서 실행 단계에서 에러에 들어가는 리소스를 줄일 수 있다.



### 2. 문법의 차이

- 간결성
  - Python은 위의 예시에서 알 수 있듯이 문법 간결해서 초보자가 배우기에도 좋다. 반면, Java는 익숙해지면 상관 없겠지만 정적 타이핑 등으로 인하여 처음 접했을 때는 코드의 양도 길어 어려움을 느낄 수 있다.
- 세미콜론
  - Java는 문장(statement)의 마지막에 세미콜론`;` 을 붙여 주지 않으면 컴파일 에러가 난다. 파이썬의 경우에는 붙여주지 않는다.
- camelCase vs snake_case
  - 함수와 변수명에 Java는 camelCase를 쓰고 Python은 snake_case를 사용한다.



### 3. 컴파일 vs 인터프리터

Java는 `컴파일 언어`로 실행 전에 코드를 기계어로 컴파일 하는 과정이 필요하다. 그래서 실행 전에 컴파일 시간이 다소 걸릴 수 있다. 하지만 컴파일이 되면 실행 속도가 빠르다. 반면에 Python은 `인터프리터 언어`로  코드의 변경사항이 발생했을 때 긴 컴파일 단계를 거치지 않고 바로 실행할 수 있다. 하지만 컴파일 과정이 없기 때문에 실행시 속도가 느릴 수 있다.



### 4. 오픈소스

Java는 Oracle이 메인으로 개발하고 유지보수하는 언어이다. 물론 Open JDK도 있다. Python은 오픈소스이다. 





### 참고자료

- https://pearlluck.tistory.com/632

- https://dingrr.com/blog/post/%EC%9E%85%EB%AC%B8%EC%9E%90%EC%97%90%EA%B2%8C-java%EB%83%90-python%EC%9D%B4%EB%83%90-%EA%B7%B8%EA%B2%83%EC%9D%B4-%EB%AC%B8%EC%A0%9C%EB%A1%9C%EB%8B%A4

- http://primaryholic.kr/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B3%BC-%EC%9E%90%EB%B0%94-%EB%B0%B0%EC%9A%B0%EA%B8%B0-%EC%A0%84%EC%97%90-%EC%B0%A8%EC%9D%B4%EC%A0%90%EC%9D%80-%EA%B3%BC%EC%97%B0-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C/