# JPA-영속성관리

## JPA에서 가장 중요한 2가지

- 객체와 관계형 DB의 매핑
- 실제 jpa의 동작 → 영속성 컨텍스트

## 영속성 컨텍스트

> 엔티티를 영구 저장하는 환경

```java
EntityManager.persist(entity);
```

- EntityManager에서 persist를 호출하여 entity를 집어 넣음
  - 단순 객체 db에 저장이 아님!!
- persist메서드는 db에 저장하는게 아닌 entity를 영속성 컨텍스트에 저장하는 것

[영속성 컨텍스트]

- 엔티티 매니저를 통해서 영속성 컨텍스트에 접근

엔티티의 생명 주기

```java
						/* 비영속 상태 */
            Member member = new Member();
            member.setId(100L);
            member.setName("HelloB");

            // 영속 -> EntityManager를 통해서 관리 되는 상태
            System.out.println("====Before====");
            em.persist(member);
            // 영속성 context 에서 삭제(준영속)
//            em.detach(member);
						
						// 객체삭제 
						// em.remove(member);
            System.out.println("====After====");

            // 실제 query가 날라가는 시점
            tx.commit();
```

### 영속성 컨텍스트의 이점

1. 엔티티 조회, 1차 캐시
   - `em.persist(member)`를 하면  내부에 1차 캐시를 들고 있다.

**db 저장 + 조회**

```java
try {
            /* 비영속 상태 */
            Member member = new Member();
            member.setId(101L);
            member.setName("HelloJPA1");

            // 영속 -> EntityManager를 통해서 관리 되는 상태
            System.out.println("====Before====");
            em.persist(member);
            System.out.println("====After====");

            Member findMember = em.find(Member.class, 101L);
            System.out.println("fineMember.id = " + findMember.getId());
            System.out.println("fineMember.name = " + findMember.getName());

            // 실제 query가 날라가는 시점
            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            // 사용 후에 꼭 닫아줘야 한다.
            em.close();
        }
// 출력된 query문

/* insert hellojpa.Member
        */ insert 
        into
            Member
            (name, id) 
        values
            (?, ?)
```

- select문이 날아가지 않았다. → 1차 캐시에서 조회해왔기 때문!

**[db에서 2번 조회]**

```java
try {
            // 영속
            Member findMember = em.find(Member.class, 101L);
            Member findMember2 = em.find(Member.class, 101L);
            System.out.println("fineMember.id = " + findMember.getName());
            System.out.println("fineMember.name = " + findMember2.getName());

            // 실제 query가 날라가는 시점
            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            // 사용 후에 꼭 닫아줘야 한다.
            em.close();
        }
// query 출력 

Hibernate: 
    select
        member0_.id as id1_0_0_,
        member0_.name as name2_0_0_ 
    from
        Member member0_ 
    where
        member0_.id=?
fineMember.id = HelloJPA1
fineMember.name = HelloJPA1
```

- 맨 처음 조회할 때 JPA가 db에서 조회해서 영속성 컨텍스트에 올려놓음
- 2번째 조회 시점에 영속성 컨텍스트 안에 있는 1차 캐시를 뒤져서 있으면 반환하기 때문에 select 문이 1번만 호출되는 것
- 또한 동일성도 보장해줌 (같은 transcation안에서 조회할 경우)
  - `System.out.println("fineMember.name = " + findMember2.getName());`
  - `result = true`
