# 트랜잭션 격리 수준 (Transaction Isolation Level)

### 트랜잭션 격리 수준?

동시에 여러 트랜잭션이 처리될 때 Locking을 통해 다른 트랜잭션이 관여하지 못하도록 막는데, `트랜잭션 격리 수준`은 이 Locking의 범위를 말한다. 트랜잭션 격리 수준은 다음 현상들을 막을 수 있는지 없는지에 따라서 정의된다.

- Dirty Read
  - 트랜잭션이 다른 트랜잭션에서 아직 커밋되지 않은 데이터를 읽을 때 발생한다.
  - 트랜잭션 1이 하나의 행을 업데이트 한다고 해보자. 이 때, 트랜잭션 2가 트랜잭션 1이 업데이트를 커밋하기 전에 업데이트된 행을 읽는다. 트랜잭션 1이 변경 내용을 롤백하는 경우 트랜잭션 2에는 존재하지 않는 데이터가 읽히고 사용될 수 있다.

- Non-Repeatable Read

  - 트랜잭션이 동일한 행을 두 번 읽지만 매번 다른 데이터를 가져오는 경우에 발생한다.
  - 트랜잭션 1이 하나의 행을 읽는다고 해보자. 이 때, 트랜잭션 2는 해당 행을 업데이트 하거나 삭제하고 이를 커밋한다. 트랜잭션 1이 행을 다시 읽는 경우 다른 행 값을 얻거나 행이 삭제되었다고 나온다.
  - 1. B 트랜잭션에서 10번 사원의 나이를 조회
    2. 27세가 조회됨
    3. A 트랜잭션에서 10번 사원의 나이를 27세에서 28세로 바꾸고 커밋
    4. B 트랜잭션에서 10번 사원의 나이를 다시 조회
    5. 28세가 조회됨
  - 하나의 트랜잭션 내에서 똑같은 SELECT를 수행했을 경우 항상 같은 결과를 반환해야 한다는 Repeatable Read 정합성에 어긋남

- Phantom Read

  - 검색 조건과 일치하지만 처음에는 표시되지 않는 행이다.

  - 트랜잭션 1이 어떤 검색 조건에 의해서 검색하여 행들을 읽었다고 해보자. 트랜잭션 2는 트랜잭션 1의 검색 조건과 일치하는 새 행(업데이트 또는 삽입을 통해)을 생성한다. 트랜잭션 1이 행을 읽는 문을 다시 실행하면 이전과 다른 행들의 집합을 읽게 된다.

  - 1. A 트랜잭션에서 Member테이블을 조회했을 때 0건이 조회됨
    2. A 트랜잭션의 조회 이후에, B 트랜잭션에서 Member 테이블에 id가 1번인 1개의 행을 삽입
    3. A트랜잭션에서 id가 1번인 행을 업데이트
    4. A트랜잭션에서 Member테이블을 조회하면 1건이 조회됨

    ```sql
    START TRANSACTION; -- transaction id : 1 
    SELECT * FROM Member; -- 0건 조회
    
        START TRANSACTION; -- transaction id : 2
        INSERT INTO MEMBER VALUES(1,'joont',28);
        COMMIT;
    
    SELECT * FROM Member; -- 여전히 0건 조회 
    UPDATE Member SET name = 'zion.t' WHERE id = 1; -- 1 row(s) affected
    SELECT * FROM Member; -- 1건 조회 
    COMMIT;
    ```

    

### READ UNCOMMITTED (lv.0)

- Dirty Read, Non-Repeatable Read, Phantom Read 모두 발생
- 트랜잭션의 변경내용이 COMMIT이나 ROLLBACK과 **상관없이** 다른 트랜잭션에서 보여짐
- 데이터 정합성에 문제가 많아 잘 사용되지 않음



### READ COMMITED (lv.1)

- Non-Repeatable Read, Phantom Read 발생 (Dirty Read 발생 X)

- 어떤 트랜잭션의 변경 내용이 **COMMIT** 되어야만 다른 트랜잭션에서 조회할 수 있다.

- 자신의 트랜잭션 번호보다 낮은 트랜잭션 번호에서 변경된(+커밋된) 것만 보게 되는 것

- 오라클 DBMS에서 기본으로 사용하고 있고, 온라인 서비스에서 가장 많이 선택되는 격리수준

  

### REPEATABLE READ (lv.2)

- Phantom Read 발생 (Non-Repeatable Read, Dirty Read 발생 X)
- **트랜잭션이 시작되기 전에 커밋**된 내용에 대해서만 조회할 수 있는 격리수준

- MySQL DBMS에서 기본으로 사용



### SERIALIZABLE (lv.3)

- Dirty Read, Non-Repeatable Read, Phantom Read 모두 발생 X
- 가장 엄격한 격리수준으로, 동시처리 능력이 다른 격리수준보다 떨어지고 성능저하가 발생하게 된다.



### 참고

[[db] 트랜잭션 격리 수준(isolation level)](https://joont92.github.io/db/%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98-%EA%B2%A9%EB%A6%AC-%EC%88%98%EC%A4%80-isolation-level/)

[Transaction Isolation Level (ODBC)](https://learn.microsoft.com/ko-kr/sql/odbc/reference/develop-app/transaction-isolation-levels?view=sql-server-ver16)
