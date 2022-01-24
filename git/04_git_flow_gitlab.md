# 04_git_flow_gitlab

담당자: 현규
생성일: 2022년 1월 23일 오후 9:59
속성: 작성중

# ⚒️ 프로젝트 처음 시작(한번만 하면됨!)

### 1. 리모트 레포지토리(Gitlab)를 원하는 폴더에 클론한다.

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled.png)

```bash
git clone https://lab.ssafy.com/s06-webmobile1-sub2/S06P12A503.git .
```

### 2. 리모트 레포지토리의 브랜치를 확인해본다.

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%201.png)

```bash
git branch -a
```

- 22.01.23 현재 master 브랜치와 develop브랜치가 있는 것을 알 수 있다. (이미 리모트에 생성되었음)
- `git branch -a` : 로컬, 리모트 둘다 확인

### 3. develop브랜치를 생성하고 이동한다.

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%202.png)

```bash
git switch -c develop
```

### 4. 리모트 레포지토리의 develop 브랜치로부터 pull을 받는다.

```bash
git pull origin develop
```

- 이 때, master보다 develop는 항상 최신이기에 merge conflict가 일어나지 않는다.

---

# 🔁 각자 feature 브랜치 만들고 작업시(반복)

**주의!! 항상 develop 브랜치에서 시작해야함! (master아님)**

### 1. **develop브랜치**에서 feature 브랜치를 생성한다. (작업은 항상 독립적인 feature branch에서)

```bash
git switch -c {feature브랜치명}
```

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%203.png)

- feature 브랜치명 예시(backend, frontend로 나누어서 **중복 피하기**!)
    - feature/backend/login
    - feature/frontend/login

### 2. feature 브랜치를 리모트 레포지토리에 연결하고 푸시한다

```bash
git push --set-upstream origin {현재 feature브랜치명}
```

- 이렇게 해주면 리모트 레포지토리에 feature 브랜치가 생성되면서 푸시된다.
- 이후에는 git push만 해주면됨

### 3. feature 브랜치에서 작업한후 `git add .` 과 git commit 하기

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%204.png)

### 

4. 리모트 레포지토리에 작업한 내용을 푸시한다.

```bash
git push
```

- 앞서 `—set-upstream`을 통해 리모트 레포지토리에 로컬의 feature 브랜치와 같은 이름으로 생성하면서 연결했기에 git push만 해도됨

### 5. feature 브랜치 작업이 끝나고 develop 브랜치에 merge한다.

- gitlab에 리모트 레포지토리에 들어가서 사이드바의 **Merge requests**로 들어간다

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%205.png)

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%206.png)

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%207.png)

- Merge request를 작성한다. 이 때, Delete source branch~ 가 기본으로 체크되어 있는데 **그대로 진행한다**(Why? merge되면 해당 feature 브랜치는 삭제하는게 원칙)

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%208.png)

- Merge 버튼을 누르면 merge가 완료된다.

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%209.png)

### 6. merge가 끝나면 remote의 feature 브랜치는 삭제된다. local에서도 이를 삭제해주자.

```bash
git switch develop
```

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2010.png)

```bash
git branch -d {삭제할 브랜치명}
```

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2011.png)

- 브랜치 목록을 보면 feature 브랜치가 삭제된 것을 볼 수 있다.

### 7. remote로부터 develop브랜치를 갱신해주자!

```bash
git pull origin develop
```

### 8. 다시 새로운 작업을 할때는 1-7의 과정을 반복한다.

# ❗Merge Conflics 가 발생할 경우 해결법

## 1. Gitlab에서 해결 가능한 merge conflict

- 이거는 git lab에서 solve conflict버튼을 누르시고 들어가서 수정하면 됩니다!!

## 2. 로컬에서 해결해야만 하는 merge conflict

### 1. 현재 리모트 레포지토리 상태가 다음과 같다고 하자

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2012.png)

- feature/frontend/feature1과 feature/frontend/feature2 브랜치에 집중하자! 둘다 아래의 develop 브랜치에서 나왔다

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2013.png)

### 2. feature1 브랜치에서 git-branch-test-2.txt와 git-branch-test.txt 파일이 필요없다고 생각해서 지우고 merge request했다고 해보자

- feature1을 develop에 merge할때는 conflict가 없이 잘된다.

### 3. 그런데 feature2 브랜치에서 git-branch-test-2.txt와 git-branch-test.txt파일을 수정했다고 해보자.

- 그러면 feature2의 commit을 push하면 어떤 일이 일어날까?

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2014.png)

### 4. 그러면 리모트 레포지토리에서는 다음과 같이 로컬에서만 merge할 수 있다고 나온다

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2015.png)

### 5. 그러면 로컬 develop 브랜치로 돌아가서 pull 받는다.

```bash
git switch develop
git pull origin develop
```

### 6. 다시 feature2 브랜치로 가서 develop 브랜치 → feature2로 merge한다.

```bash
// feature2에서 진행!!
git merge develop
```

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2016.png)

- 그러면 위와 같이, CONFLICT가 났다고 뜬다.

### 7. vscode를 열어서(git bash에서 `code.`) merge conflict를 해결한다.

- Merge Changes라는 것이 뜨는데 +버튼을 눌러서 Stage Changes를 하면 아래와 같은 창이 나온다.

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2017.png)

- 현재 상황에서 git-branch-test-2.txt는 Delete File을 누르고, git-branch-test.txt는 Keep Our Version을 해보자. 그러면 아래와 같이 git-branch-text.txt가 살아있는 것을 볼 수 있다.

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2018.png)

- 다시 `git merge develop` 를 해보자.

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2019.png)

- 문제가 없다고 나온다.

### 8. 정말 문제가 없는지 feature2의 커밋을 푸시하고 다시 merge request를 해보자.

- 내가 open한 merge request로 가서 내용을 바꿔주자

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2020.png)

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2021.png)

- 위처럼 Merge 버튼이 활성화 되었다!!

### 9. 어쨋든 merge conflict를 로컬에서 확인했는데 develop브랜치의 history를 가보면 지저분하다..ㅠ

![Untitled](04_git_flow_gitlab%20d5040711c8794a4bb026ca1ab2a9223c/Untitled%2022.png)

- 이 방식이 최선인지는 모르겠지만, 더 좋은 방법을 찾을때 까지는 이렇게 해결하는걸로!