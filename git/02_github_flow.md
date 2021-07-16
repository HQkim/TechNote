# 02_Github_Flow



## Git Flow

- Git을 활용하여 협업하는 흐름으로 branch를 활용하는 전략.





## Branch

### Branch란?

- 여러명의 작업자가 독립적으로 어떠한 작업을 진행하기 위해 고안된 개념. master(main) branch를 default branch로 설정하고 추가적인 branch로 작업한 후 추후에 master branch에 병합한다. 
- 간단한 예로 로그인 기능을 구현하는 것을 master 브랜치가 아닌 login_branch에서 작업한 후에 이를 추후에 master 브랜치에 병합(merge)하는 경우가 있다. 
- 게임을 패치할 때도 현재 배포되고 있는 branch가 아닌 branch에서 새로운 기능을 구현하거나 해서 잘 돌아가면 이 branch로 배포한다.

### Branch 기본 명령

#### 브랜치 목록

```bash
(master)$git branch
```

#### 새로운 Branch 생성

```bash
(master)$git branch {branch name}
```

#### Branch 이동

```bash
(master)$git checkout {branch name}
```

#### Branch 생성 및 이동

```bash
(master)$git checkout -b {branch name}
```

#### Branch 삭제

```bash
(master)$git branch -d {branch name}
```



### Branch Merge

#### Branch merge

``` bash
(master)$git merge {branch name}
```

- 3가지 상황이 있음

  1. Fast-Forward(버스)

     하나의 branch에서만 작업 수행. merge 할때 아무 문제가 없다.

  2. 나눠서 독립적으로 작업

     merge 할때 아무 문제가 없다. 각자가 최신이기 때문

  3. 섞어서 작업

     git은 항상 최신의 상태로 유지하고 싶어함. 

     그런데 이 경우 merge 할때 뭐가 최신인지 모를 수 있음. -> merge conflict

     이 경우 수동으로 수정을 해줘야함.



### 기타

#### Branch merge --no-ff(심화)

```bash
(master)$git merge -no-ff {branch name}
```

fast forwarding 상황에서도 commit을 발생시키는 옵션. branch 이력을 유지한다는 장점이 있다.

#### Branch 그래프로 보기

```bash
$git log --all --graph --oneline
```

#### Branch rebase

remote repository에 push된 commit에 대해서는 절대 rebase를 진행하면 안된다.

참고: https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-Rebase-%ED%95%98%EA%B8%B0





## Github Flow

### Github Flow 기본 원칙

Github Flow는 Github에서 제안하는 Branch 전략으로 다음과 같은 기본 원칙을 가지고 있다.

1. master branch는 반드시 배포 가능한 상태여야 한다.
2. feature branch는 각 기능의 의도를 알 수 있도록 작성한다.
3. Commit message는 매우 중요하며, 명확하게 작성한다.
4. Pull Request를 통해 협업을 진행한다.
5. 변경사항을 반영하고 싶다면 master branch에 병합한다.



### Github Flow models(협업)

#### Shared Repository Model

- 개요

  - 동일한 저장소를 공유하여 활용하는 방식.

  - 팀장 : repository owner (project manager)

    팀원: collaborator (a.k.a) 

- 순서

  1. 팀장이 github에 repository 생성 후 settings>manage access> collaborator에 팀원 등록

  2. 팀원은 이메일을 통한 초대 수락

  3. Clone project(remote) repository

     항상 첫 git add를 하기 전에 .gitignore 파일 작성  (https://www.toptal.com/developers/gitignore)

  4. 팀원이 독립적인 feature branch 생성.

     master branch는 항상 배포 가능한 상태유지. 이에 영향 없도록 독립적 branch 생성

     feature branch는 이름 생성할 때 기능을 명시적으로 나타낼 것

  5. 팀원이 Commit을 통해 작업의 이력을 남긴다.

     Commit message는 매우 중요하며 일관된 형식으로 해당 이력을 쉽게 파악할 수 있도록 작성

  6. 팀원이 원격 저장소에 push

     **master branch에 push 하지 않도록 유의!**

  7. 팀원이 Github에 들어가서 Pull Request를 통해 요청 생성

  8. 팀장이 pull request에서 작성된 코드를 확인 후 병합

     이 때 master branch가 반드시 배포 가능한 상태여야 한다.

  9. 로컬 저장소에서 merge된 branch는 삭제하고 master branch 업데이트.

     이후 앞의 과정을 반복

#### Fork & Pull Model

- 개요
  - Collaborator에 등록하지 않고 Pull request를 통해 협업. Github 기반의 오픈소스 참여과정에서 쓰이는 방식