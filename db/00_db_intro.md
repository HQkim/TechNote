# 00_DB_Intro



#### 데이터베이스로 얻는 장점들 (**)

#### SQL 분류 (**)

| 분류                   | 개념                     | 예시 |
| ---------------------- | ------------------------ | ---- |
| DDL - 데이터 정의 언어 | 관계형 데이터베이스 구조 |      |
|                        |                          |      |
|                        |                          |      |

#### DML



## 테이블 생성 및 삭제

#### 테이블 생성 및 삭제 statement

- CREATE TABLE (**)
  - 데이터베이스에서 테이블 생성

#### DROP (**)

## CRUD



## READ



## ALTER TABLE

#### 는 실패(**)

주관식 마지막 문제. 에러가 나는 이유와 해결방안.



#### user 레코드 생성 실패 예시1,2,3 - SQL (**)



#### 나이가 30살이거나 성이 김씨인 사람의 인원 수(**)

- Q 사용

#### 나이가 많은 사람순으로 10명 -ORM (**)

#### 성, 이름 내림차순으로 5번째 있는 유저 정보 조회 (**)

- OFFSET 4





---

#### DB 자료형 (**)

- BLOB

#### TIP

SQL을 ORM으로 그 반대로

빈칸뚫고 맞추기

단어하나 바꾸고



#### LIKE operator

- sqlite는 패턴 구성을 위한 2개의 wildcards를 제공 (**)
  - %(percent sign)
    - 0개 이상의 문자 ex) 김%
  - _(underscore)
    - 임의의 단일 문자 ex) 김_



#### 기타

- .tables 는 SQL 문법 X. sqlite 프로그램임

- Primary Key : 각 행의 고유 값 - id가 아니라 pk다. id는 장고에서 쓰는 것.

- > SQL분류- 예시, 쓰는법 쭉 보기

- INSERT 문법의 차이점. LIMIT OFFSET(5번째행), DISTINT(중복제거)

- 삭제 DELETE임. remove X

- AUTOINCREMENT

- UPDATE 쓰는법 (순서)

- > SQLITE functions

  - COUNT, AVG, MAX, MIN 등

- > LIKE operator

  - 패턴
  - 쓰는 법

- > ORDER BY

  - 뭐가 오름차순인지
  - ORM에서 -pk와도 연결

- > GROUP BY

  - 어떻게 쓴다 정도

- > 는 실패

  - Error 실패 이유와 해결방법

- ORM을 SQL로 SQL을 ORM으로 쭉 봐주자

  - filter, values, count 등

- > 나이가 30살이거나 성이 김씨인 사람의 인원 수

  - Or 쓸 때 Q써야함

- Aggregate 쭉 봐주라

