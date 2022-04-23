# Django Database

### 1. 공식문서에서 명시

> [참고자료](https://docs.djangoproject.com/ko/4.0/ref/databases/)

#### django에서 공식적으로 지원하는 DB

- [PostgreSQL](https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes)
- [MariaDB](https://docs.djangoproject.com/en/4.0/ref/databases/#mariadb-notes)
- [MySQL](https://docs.djangoproject.com/en/4.0/ref/databases/#mysql-notes)
- [Oracle](https://docs.djangoproject.com/en/4.0/ref/databases/#oracle-notes)
- [SQLite](https://docs.djangoproject.com/en/4.0/ref/databases/#sqlite-notes)

#### 3rd-party 로 제공되는DB

- [CockroachDB](https://pypi.org/project/django-cockroachdb/)
- [Firebird](https://pypi.org/project/django-firebird/)
- [Google Cloud Spanner](https://pypi.org/project/django-google-spanner/)
- [Microsoft SQL Server](https://pypi.org/project/mssql-django/)

<br/>

### 2. PostgreSQL과 MySQL 비교 (사용성)

> [참고자료](https://www.qu3vipon.com/postgresql-vs-mysql) (2021.05 작성)

Django와 잘 어울리는 DB는 보통 PostgreSQL이라고 함. 그 이유는 **사용성 측면**에서 다음과 같다고 함

#### PostgreSQL 장점

**1. DISTINCT ON**

- Queryset의 distinct()를 이용하면 중복된 값 제거 가능
- PostgreSQL을 사용하면 **특정 필드에 대해서만** 비교를 진행할 수 있음

**2. UUIDField**

- `UUIDField`를 사용하면 DB에 `uuid`타입으로 저장됨
- DB를 export하여 사용할때 편리함

**3. Data Type Cast**

- SQL로 데이터를 가공할 때 PostgreSQL의 `Data Type Casting` 문법이 상대적으로 간편

4. **Full Text Search**

- FTS를 통해 훨씬 빠르고 효율적인 문자열 검색이 가능
- 하지만 지금 진행하는 프로젝트에서는 FTS를 사용할 일이 크게 없을것 같음.

<br/>

#### MySQL 단점

**1. Migration Rollback**

- [여기](https://www.qu3vipon.com/django-migrations#80f642cf2e834834bcfca34c9f1f4e26)를 읽어보면 MySQL은 schema 변경과 관련된 transaction의 rollback을 지원하지 않는다고 나온다. 

  (위의 링크에 migrations에 대한 전반적인 내용도 있음)

- 개발을 하다보면 migration 파일을 수정하거나 RunPython을 사용하여 새로운 테이블에 초기값을 설정하는 등의 작업이 빈번

- MySQL은 위의 작업을 위해 DB 테이블을 **직접 조작**해야함

  - 혹은 초심자들은 보통 migration이 꼬였을 때 초보자들은 흔히 데이터베이스를 전부 날리고 모든 테이블을 새로 생성
  - 테이블을 삭제하면 데이터도 다 함께 삭제 (운영 중인 서비스에서는 이런 방식으로 문제 해결x)

**2. UUID**

- `UUIDField`를 사용하면 DB에 `varcahr(32)`타입으로 저장됨

- `-`가 제거된 `string`형태로 저장되어 있어서 DB export하여 사용할때 매번 가공해줘야할 수 있음

<br/>

### 3. PostgreSQL과 MySQL 비교 (성능 및 커뮤니티)

- OLTP 환경에서 MySQL의 속도가 더 좋음 ([OLTP참고](https://hyowong.tistory.com/196))

- UPDATE가 빈번한 서비스의 경우 MySQL이 더 우수한 성능
- PostgreSQL은 ACID와 같은 DB 안정성에 더 무게를 둠 ([ACID참고](https://chrisjune-13837.medium.com/db-transaction-%EA%B3%BC-acid%EB%9E%80-45a785403f9e))
- MySQL 사용자 **커뮤니티가 더 크기** 때문에 문제발생시 필요한 자료를 얻기 쉬움
  - 단순하게, google에서 "django mysql"을 검색했을때 "django postgresql"을 검색할때보다 **약 3배** 이상의 자료가 나옴



### 현업자들의 말

- 7만개 데이터 정도면 성능면에서는 크게 고민안해도 된다.
  - 이미지도 백만장 넘어야 성능고려
  - sqlite로도 상관은 없는데 db io가 많은거라면 sqlite는 지양
