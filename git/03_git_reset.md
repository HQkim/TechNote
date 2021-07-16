# 03.Git_Reset



## 개요

- Git reset은 특정한 버전으로 돌아가는 것을 말한다. (타임머신)



## 3가지 방법

1. --soft

   - working derectory와 staging area 안바뀌고 git status에서 HEAD가 특정 커밋을 가리키는 것만 달라진다.

   - 거의 안쓴다.

2. --mixed

   - git reset만 쳤을 때 기본값으로 --mixed가 들어간다.

   - working directory 안바뀜, staging area가 특정 커밋의 내용과 똑같게 만든다.
   - 보통 이걸 쓴다.

3. --hard

   - working directory를 과거의 특정 커밋의 내용과 똑같게 만든다.
   - 이걸 썼다고 해도 git reflog를 통해 log를 확인후 돌아갈 수 있다.



## Git Stash

- 개요

  - 현지 커밋하지 않은 작업을 스택에 잠시 저장할 수 있도록 하는 명령어이다. 이를 통해 아직 완료하지 않은 일을 커밋하지 않고 나중에 다시 꺼내와 마무리할 수 있다.

  - 혹은 현재 작업하는 내용이 다른 branch의 작업에 해당하는 것을 알았을 때 이를 옮길 수도 있다.

- 방법

  - 새로운 statsh를 스택에 만들어 하던 작업을 임시로 저장

    ```bash
    $git stash
    ```

  - stash 목록 확인

    ``` bash
    $git stash list
    ```

  - stash 적용하기

    ```bash
    $git stash apply // 가장 최근의 statsh를 가져와 적용
    ```

  - statsh 제거하기

    ``` bash
    $git stash drop
    ```

    apply 옵션은 단순히 statsh를 적용하는 것으로 해당 statsh는 스택에 남아있다. 위를 통해 제거할 숭 ㅣㅆ다.



github portfolio -> notion도 괜찮다.

velog



### 참고

- 취업 관련 예

  https://www.notion.so/cb7e7be9d73a41e88be9abedc7ae45c2

- github page를 활용해 portfolio를 만들자. notion도 좋다.

  https://startbootstrap.com/themes/portfolio-resume?showPro=false

  https://pages.github.com/

- velog를 활용한 블로그 관리