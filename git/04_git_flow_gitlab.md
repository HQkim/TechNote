# 04_git_flow_gitlab

## ⚒️프로젝트 처음 시작(한번만 하면됨!)

### 1. 리모트 레포지토리(Gitlab)를 원하는 폴더에 클론한다.

```bash
git clone {리모트 레포지토리 경로} .
```

### 2. 리모트 레포지토리의 브랜치를 확인해본다.

```bash
git branch -a
```

- 현재 master 브랜치와 develop브랜치가 있다고 가정
- `git branch -a` : 로컬, 리모트 둘다 확인

### 3. develop브랜치를 생성하고 이동한다.

```bash
git switch -c develop
```

### 4. 리모트 레포지토리의 develop 브랜치로부터 pull을 받는다.

```bash
git pull origin develop
```

- 이 때, master보다 develop는 항상 최신이기에 merge conflict가 일어나지 않는다.

<br/>

## 🔁각자 feature 브랜치 만들고 작업시(반복)

**주의!! 항상 develop 브랜치에서 시작해야함! (master아님)**

### 1. **develop브랜치**에서 feature 브랜치를 생성한다. (작업은 항상 독립적인 feature branch에서)

```bash
git switch -c {feature브랜치명}
```

- feature 브랜치명 예시(backend, frontend로 나누어서 

  중복 피하기

  !)

  - feature/backend/login
  - feature/frontend/login

### 2. feature 브랜치를 리모트 레포지토리에 연결하고 푸시한다

```bash
git push --set-upstream origin {현재 feature브랜치명}
```

- 이렇게 해주면 리모트 레포지토리에 feature 브랜치가 생성되면서 푸시된다.
- 이후에는 git push만 해주면됨

### 3. feature 브랜치에서 작업한후 `git add .` 과 git commit 하기

- 리모트 레포지토리에 작업한 내용을 푸시한다.

```bash
git push
```

- 앞서 `—set-upstream`을 통해 리모트 레포지토리에 로컬의 feature 브랜치와 같은 이름으로 생성하면서 연결했기에 git push만 해도됨

### 5. feature 브랜치 작업이 끝나고 develop 브랜치에 merge한다.

- gitlab에 리모트 레포지토리에 들어가서 사이드바의 **Merge requests**로 들어간다

- **New merge request 버튼 클릭!**

- Source branch는 “내 feature 브랜치”, **Target branch는 “develop 브랜치”** 로 설정한다.

- Merge request를 작성한다. 이 때, Delete source branch~ 가 기본으로 체크되어 있는데 **그대로 진행한다**(Why? merge되면 해당 feature 브랜치는 삭제하는게 원칙)

- Merge 버튼을 누르면 merge가 완료된다.

### 6. merge가 끝나면 remote의 feature 브랜치는 삭제된다. local에서도 이를 삭제해주자.

```bash
git switch develop
```

```bash
git branch -d {삭제할 브랜치명}
```

- 브랜치 목록을 보면 feature 브랜치가 삭제된 것을 볼 수 있다.

### 7. remote로부터 develop브랜치를 갱신해주자!

```bash
git pull origin develop
```

### 8. 다시 새로운 작업을 할때는 1-7의 과정을 반복한다.

<br/>

## ❗Merge Conflics 가 발생할 경우 해결법

### 1. Gitlab에서 해결 가능한 merge conflict

### 2. 로컬에서 해결해야만 하는 merge conflict

