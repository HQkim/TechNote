# Git Intro



## 정의

- (분산형) 버전 관리 프로그램
  - 코드의 Histroy를 관리하는 도구
  - 개발된 과정의 역사를 볼 수 있으며,
  - 프로젝트의 이전 버전을 복원하고 변경사항을 비교, 분석 및 병합도 가능

- DVCS(Distributed Version Control System)

- <-> 중앙형 : 중앙에 절대적인 데이터 저장소가 있음
- 분산형은 여러 컴퓨터에 데이터를 저장

## Git 초기 설정

#### 커밋 작성자(author) 설정

```
$ git config --global user.email "메일주소"
$ git config --global user.name "유저네임"
```

- 커밋을 작성하는 사람이 누구인지 알아야하기 때문

#### 지정된 설정 확인

```
$ git config --global -l
# $ git config --global --list
```

#### 커밋 편집기 변경

```
$ git config --global core.editor "code --wait"
```

- 해당 명령어는 반드시 vscode가 설치되어 있어야 함

> 기본 텍스트 편집기 vim을 vscode로 대체하는 것

## Repository와 Commit

#### Repository

- .git 디렉토리를 말한다. 버전정보를 담고 있다.
- cf) 워킹디렉토리는 작업하고 있는 사항
- 따라서, .git 디렉토리를 지우면 버전정보가 다 날아간다.
- 버전별 프로젝트 모습과 버전별 변경 사항에 대한 설명(Commit Message)

#### Commit

- 커밋을 통해 하나의 버전으로 기록된다.
- 커밋 메세지는 현재 변경사항들을 잘 나타낼 수 있도록 작성하는 것을 권장
- 커밋은 고유한 아이디인 해시 값을 가짐
  - SHA-1 알고리즘에 의해 생성
- 커밋 목록은 `git log`를 통해서 확인할 수 있음

```bash
$ git log --oneline # 커밋 목록 한 줄로 보기
c02659f (HEAD -> master) first commit
```



## Git 작업흐름 및 파일상태

#### 작업흐름

1. Working directory

   - 여기서 작업을 수행(코딩)

2. git add 

   - Staging area에 변경된 버전사항을 올린다.

   - INDEX

3. git commit

   - 버전사항을 기록하는 개념. 

   - HEAD

4. git push

   - github나 gitlab과 같은 원격 저장소에 commit된 git 파일을 올린다.

#### 파일 라이프사이클

- Working directory의 모든 파일은 특정 상태를 가지며, git 명령어를 통해 변경된다.
- Tracked
  - unmodified - 수정되지 않은 상태
  - modified - 수정된 상태
  - staged - 무대에 있는 상태
- Untracked - 한번도 stage에 올라가지 않은 상태



## Git Basic

#### 로컬 저장소 설정

```
$ git init

Initialized empty Git repository in C:/Users/student/Desktop/git_class

student@M172 MINGW64 ~/Desktop/git_class (master)
```

- 폴더에 git 저장소를 초기화하면,
  - `.git` 숨김 폴더가 생기고
  - bash에는 `(master)`라고 표기 된다.

> 주의사항git 저장소 내에 또다른 git 저장소를 만들면 안됨 !!git init 명령어를 입력할 때, (master)가 있으면 절대! 입력하지 말 것!

### **add**

> staging area / INDEX

```
$ git add 파일명
$ git add . # 현재 디렉토리(하위 디렉토리)
$ git add a.txt # 특정 파일
$ git add my_folder/ # 특정 폴더
```

- `working directory` 상태의 파일을 `staging area`상태로 변경
- 커밋을 위한 파일 및 폴더들을 추가하는 명령어

```
$ touch a.txt b.txt

$ git status
On branch master

No commits yet

Untracked files: # 트래킹 되고 있지 않는 파일 목록
  (use "git add <file>..." to include in what will be committed)
        a.txt
        b.txt

nothing added to commit but untracked files present (use "git add" to track)
$ git add a.txt
$ git status

On branch master

No commits yet

Changes to be committed: # 커밋 예정인 변경사항(staging area)
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt

Untracked files: # 트래킹 되고 있지 않은 파일
  (use "git add <file>..." to include in what will be committed)
        b.txt
```

> 모든 정보는 git status 에 있다.

### **commit**

```
$ git commit -m "first commit"
[master (root-commit) c02659f] first commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
$ git log
commit c02659fc917b40f1ab6106a1727703a7884df12e (HEAD -> master)
Author: edujunho <edujunho.hphk@gmail.com>
Date:   Mon Jun 7 15:29:54 2021 +0900

    first commit
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        b.txt

nothing added to commit but untracked files present (use "git add" to track)
```

- 커밋을 통해 하나의 버전으로 기록 됨
- 커밋 메세지는 현재 변경사항들을 잘 나타낼 수 있도록 작성하는 것을 권장
- 커밋은 고유한 아이디인 해시 값을 가짐
  - SHA-1 알고리즘에 의해 생성
- 커밋 목록은 `git log`를 통해서 확인할 수 있음

```
$ git log --oneline # 커밋 목록 한 줄로 보기
c02659f (HEAD -> master) first commit
```

------

### **status**

- working directory, staging area 공간의 파일 상태를 확인할 수 있다.

```
$ git status
```

### **git log**

- 커밋이 완료 되면, 잘 기록되었는지 확인!

  ```
  $ git log
  $ git log -1 # 최근 몇개까지 보여주는 옵션
  $ git log --oneline # 한줄로 보여주는 옵션
  ```

------

### **추가 커밋 쌓기**

- a.txt 내용 수정

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        b.txt

no changes added to commit (use "git add" and/or "git commit -a")
$ git add a.txt

$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   a.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        b.txt
$ git commit -m "second commit"

[master 4cac5c6] second commit
 1 file changed, 1 insertion(+)
$ git log --oneline
4cac5c6 (HEAD -> master) second commit
c02659f first commit
```

- b.txt 커밋 만들기

```
$ git add b.txt

$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   b.txt

$ git commit -m "add b.txt"
[master 6fe9152] add b.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 b.txt
$ git log --oneline
6fe9152 (HEAD -> master) add b.txt
4cac5c6 second commit
c02659f first commit
```

### **git show**

- 현재 커밋의 변경 기록 확인하기

### **git diff 커밋아이디1 커밋아이디2**

커밋들 사이에 변경 사항을 확인할 수 있음

```
git diff 9b15 539d
```



### 기타 

- Git은 파일만 관리한다. -> 빈 폴더는 추적하지 않는다.



## Git과 GitHub

- Git은 로컬 저장소에 버전사항(생성, 수정, 삭제)을 기록한다.
- Git으로 로컬 저장소에 Commit한 것을 GitHub라는 클라우드에 저장한다.
  - 따라서, 아무것도 없는 로컬에서 GitHub를 통해 버전사항을 받아올 수 있다.