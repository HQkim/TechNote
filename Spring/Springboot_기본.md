# Springboot_기본

### EntityManager

- JPA에서 

  ```
  @PersistenceContext
  ```

   어노테이션으로 EntityManager불러와 쓸 수 있음

  - 순수하게 JPA를 쓰면 `@PersistenceUnit` 어노테이션을 써서 내가 만든 EntityManagerFactory를 불러와서 써야함.

### JPQL

- SQL과 문법 거의 비슷하지만 쿼리문의 대상이 `Table`이 아니라 `Entity`

### @Transactional

- JPA에서 DB를 변경하고 하는 로직은 Transactional 어노테이션을 붙여줘야함
- spring에서 제공하는 것과 javax에서 제공하는 것이 있는데 우리는 spring을 쓰고 있기때문에 spring걸로 쓰자.
- 클래스 전체에 줄 수도 있지만, 메소드에서 `@Transactional(readOnly = true` 와 같이 쓰면 더 성능이 좋다.

### validateDuplicateMember

- 만약 동시에 같은 member 이름으로 가입을 하는 경우 (멀티스레드)를 방지하기 위해 DB에 unique 옵션을 걸어줘야한다.

### Test시 insert문이 실행되지 않는 이유

- Rollback을 시켜버리기 때문, @RollBack(false)를 하면 rollback하지 않음. 어차피 DB에는 변동이 없기때문에 Insert 시키지도 않음
- em.flush()를 해주면 쿼리문도 보고, rollback도 시킬 수 있음

