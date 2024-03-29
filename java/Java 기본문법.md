# Java 기본 문법1

## 자바 프로그램 구조

자바 프로그램은 기본적으로 `클래스` 구조에서 시작한다. 클래스는 객체지향 개념에서 객체를 정의하는 틀로서 많은 객체지향 프로그램 언어의 기본 구조이다.



기본적인 자바 프로그램의 구조

```java
// 클래스 선언
public class MyClass {
    // 변수 선언
    int num1;
    Message msg;

    // 메서드
    public void printName(String name) {
        ...
    }

    // 메서드
    public Message getMessage() {
        ...
    }

    // 메인 메서드
    public static void main(String[] args) {
        // 클래스 인스턴스 생성
        MyClass mc = new MyClass();
        ...
    }
}
```



### 클래스(Class)

> 객체지향 프로그램의 기본 구조로 자바에서 모든 프로그램 소스는 클래스 단위로 시작

- 프로그램 소스는 `.java` 파일이고 컴파일된 결과는 `.class` 가 됨
- 일반적으로 클래스 이름과 소스파일명은 동일
- 대부분의 경우 프로그램은 여러 클래스로 구성되며 실행을 위해서는 `main()` 메서드가 필요



### 인스턴스(Instance)

> 클래스로부터 생성된 객체로 클래스는 객체를 정의한 틀이고 실제 프로그램은 인스턴스를 통해 동작

- `main()` 메서드는 단지 프로그램을 실행하는 진입점이고 실제 클래스를 사용하려면 `new()` 연산을 통해 인스턴스를 생성해야 함
- `main()`에서 클래스부에 선언된 변수(멤버)를 접근할 수 없으며 인스턴스를 통해 사용해야함(인스턴스 변수)

- 인스턴스에서 변수와 메서드 사용은 "인스턴스명.변수명, "인스턴스명.메서드명" 과 같은 형식으로 사용



### 변수(Variable)

> 일반적인 프로그램언어의 변수와 기본개념은 같음



### 메서드(Method)

> 일반적인 프로그램언어의 함수와 유사. 함수는 단순한 기능을 모듈화한 것이지만 메서드는 객체의 동작(행위)을 정의



### 주석(Comment)

>대부분의 프로그램언어와 같은 주석을 지원하며 JavaDoc과 같은 특수한 목적의 주석이 있음

```java
// 한줄 주석
/*
    여러줄 주석
*/
/**
    JavaDoc 주석
*/
```

- JavaDoc은 자바 프로그램 소스의 JavaDoc 주석을 참고해 클래스의 API문서를 자동으로 생성해 주는 주석임
- https://docs.oracle.com/en/java/javase/11/docs/api/index.html 에서 볼 수 있는 문서형태가 JavaDoc 으로 생성된 주석임.



### 자바 식별자(identi9filer) 규칙

> 변수, 상수, 메서드, 클래스 등을 선언할떄의 일반적인 이름 규칙

- 첫 문자가 문자나 `_`, `$` 의 특수문자로 시작되어야 한다. 숫자로 시작할 수 없다. 

- 첫 문자가 아니라면, 문자나 `_`, `$` 의 특수문자 그리고 숫자로 구성될 수 있다.
- 자바의 예약어는 식별자로 사용할 수 없다.
- 자바의 식별자는 대소문자를 구분한다.
- 식별자 길이는 제한이 없고 공백은 포함할 수 없다.



### 식별자 생성 관례(Coding convention)

> 문법적인 제한사항은 아니지만 일반적으로 따르는 관례

- 클래스/인터페이스 이름에 대문자 카멜표기법 적용 (ex. AccessToken)
- 메서드 이름은 소문자 카멜표기법 (ex. toString())
- 변수는 소문자 카멜표기법 (ex. accessToken)
- 상수는 대문자와 언더스코어로 구성 (ex. POSTAL_CODE_EXPRESSION)