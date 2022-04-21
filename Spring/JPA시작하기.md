# JPA 시작하기

## SQL 중심적인 개발의 문제점

- 객체지향 언어 - 관계형 DB

  객체를 관계형 DB에 저장하여 관리해야함.  → SQL 중심적인(의존적인) 개발로 이어진다.

- 객체와 관계형 데이터 베이스의 차이

  1. 상속

     - 객체는 상속관계 존재

     - 관계형 db 에는 상속관계가 x

  2. 연관관계

     - 객체는 참조를 가지고 연관된 객체를 가져옴
       - ex. get

     - 관계형 db는 pk와 fk로 join을 통해서 필요한 객체를 찾음

  3. 데이터 타입

  4. 데이터 식별 방법

  → 객체의 상속관계과 그나마 유사한 관계가 Table 슈퍼타입 서브타입 관계!

  

## JPA 소개 핵심 정리

- JPA는 항상 EntityManagerFactory를 만들어야 함.
  - 이게 db당 하나씩 묶여서 돌아감
- `hello`라는 것은 설정 파일(`persistence.xml`)의 설정 정보를 읽어와서 만들
- jpasms Entitymanager가 고객의 요청에 따라 db작업이 있을때 이 em을 통해서 작업해야 함
- jpa의 모든 db 변경은 transaction 안에서 이루어짐
  - 단순 조작은 transaction 없어도 동작하긴 함
  - tx.commit()을 꼭 해줘야 적용됨!!!
- 작업 이후엔 꼭 em.close()를 통해서 닫아줘야 db connection이 반환됨.
- emf.close()도 해야함

