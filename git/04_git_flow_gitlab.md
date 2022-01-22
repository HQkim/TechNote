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

### 

