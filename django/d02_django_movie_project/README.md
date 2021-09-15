# README



## 프로젝트 개요

장고, bootstrap을 활용한 영화 목록 CRUD 사이트 구현하기



## 0. 프로젝트 시작

다음과 같은 순서로 프로젝트를 시작했다.

- 프로젝트 폴더 생성
- 가상환경 설치 및 실행
- 가상환경에 django와 django-extensions 설치
- django-admin startproject {프로젝트명} .
- python manage.py startapp {앱이름}
- settings.py에서 앱등록, 언어, 시간 설정



## 1. url 설정 및 base.html

#### url 설정

`pjt04/urls.py` 파일에서 

- `{local주소}/movies` 로 접근이 오면 movies앱 디렉토리의 `urls.py` 파일에서 mapping 되도록 했다.

#### base.html

프로젝트 디렉터리와 같은 레벨에 `templates/` 디렉터리를 만들고 그 안에 `base.html` 파일을 생성한다. `pjt04/settings.py`에서 TEMPLATES에서 'DIRS' 부분을 [BASE_DIR / 'templates']로 설정해 준다. 이는 `base.html`을 `movies/templates/movies`의 html파일에서 재사용하기 위한 것으로 알고 있다. 공식 문서를 보니 overriding templates의 키워드가 보이는데 읽어봐도 원리가 정확히는 이해가 잘 안간다. 추후에 다시 보면 알게 되겠지?.. 라고 하면서 일단 넘어가본다.

base.html 안에서 bootstrap을 활용해 다음과 같이 설정했다.

- Navbar의 Movies로고나 INDEX 항목을 클릭하면 `{local주소}/`로 이동하게 했다.
- Navbar의 CREATE항목을 클릭하면 `{local주소}/movies/new/`로 이동하게 했다.
- block을 만들어 추후에 base.html을 확장해서 앱 template에서 활용하도록 했다.

  

## 2. Model

 `moveis/models.py`파일에서 다음과 같이 클래스를 구성했다.

- title : max_length가 100인 django.db.models.CharField
- overview : django.db.models.TextField
- poster_path : max_length가 500인 django.db.models.CharField
- created_at : django.db.models.DateTimeField(auto_now_add=True) -> 생성시 자동 설정
- updated_at: django.db.models.DateTimeField(auto_now=True) -> 수정시 자동 설정

그리고 makemigrations와 migrate를 해주었다.

- makemigrations는 movies/migrations 폴더에 model을 변경했다는 것을 저장하고
- migrate는 db에 실제로 model을 구현하는 것이다.



## 3. Url 설정

`movies/urls.py` 파일에서 다음과 같이 view에 매핑되도록 했다.

- `{local주소}/` 로 HttpRequest가 오면 movies.views.index 함수에서 처리
- `{local주소}/movies/new/` 는 views.new에서 처리
- `{local주소}/movies/create` 는 views.create에서 처리

- `{local주소}/movies/<int:pk>`은 views.detail에서 처리

- `{local주소}/movies/<int:pk>/edit/`은 views.edit에서 처리

- `{local주소}/movies/<int:pk>/update`은 views.update에서 처리

- `{local주소}/movies/<int:pk>/delete`은 views.delete에서 처리



## 4. Views

`movies/views.py`에서 다음과 같이 설정했다.

- index함수
  -  db의 모든 레코드를 쿼리셋에 담아서 이를 `movies/index.html` 전달한다. 그리고 `index.html`파일로 요청에 응답한다.
- new함수
  -  `movies/new.html`로 요청에 응답한다.
- create함수
  - 요청에 담긴 title, overview, poster_path정보를 통해서 새로운 Movie객체를 만들고 이를 db에 저장한 후에 `{local주소}/`로 요청을 돌린다.
- detail 함수
  - url에 담긴 pk 정보를 통해서 이와 같은 pk값을 가지는 레코드를 가져와서 Movie객체에 담는다. 이 객체를 `movies/detail.html`에 전달하며 `detail.html`파일로 요청에 응답한다.
- edit 함수
  - url에 담긴 pk 정보를 통해서 이와 같은 pk값을 가지는 레코드를 가져와서 Movie객체에 담는다. 이 객체를 `movies/edit.html`에 전달하며 `edit.html`파일로 요청에 응답한다.

- update 함수

  - url에 담긴 pk 정보를 통해서 이와 같은 pk값을 가지는 레코드를 가져와서 Movie객체에 담는다. 만약 요청의 메소드라 POST라면 요청에 담긴 'title'키의 값, 'overview'키의 값, 'poster_path'키의 값을 Movie객체의 인스턴스변수에 담은 후에 이를 db에 저장한다. 그리고 `{local주소}/movies/<int:pk>`로 요청을 돌린다.

- delete 함수

  - url에 담긴 pk 정보를 통해서 이와 같은 pk값을 가지는 레코드를 가져와서 Movie객체에 담는다. 만약 요청의 메서드라 POST라면 db에서 해당 레코드를 삭제하는 메서드를 실행한 후에 `{local주소}/`로 요청을 돌린다. 메서드가 POST가 아니라면 `{local주소}/movies/<int:pk>`로 요청을 돌린다.

  

## 5. Templates

Template의 충돌을 막기 위해 Template 디렉터리를`movies/templates/movies/`로 설정해준다. 그 안의 파일들이 보여주는 내용은 다음과 같다.

- index.html
  - view에서 가져온 쿼리셋에 있는 영화들의 제목을 나열하고 제목을 클릭하면 `{local주소}/movies/<int:pk>`로 이동하도록 한다.
- new.html
  - form을 작성하여 action은 `{local주소}/movies/create`로 method는 "POST"로 설정했다. 메서드가 "POST"이기 때문에 csrf_token을 꼭 넣어줘야 한다.
- detail.html
  - view에서 가져온 객체의 정보를 나타내도록 하였고 EDIT, DELETE 버튼을 추가했다. bootstrap의 card를 사용해서 꾸몄다. 
  - EDIT 버튼을 누르면 form을 통해 `{local주소}/movies/<int:pk>/edit/`로 이동하고 DELETE버튼을 누르면 form을 통해 `{local주소}/movies/<int:pk>/delete/` url로 이동하게 하였다.
- edit.html
  - view에서 가져온 객체의 정보를 나타내었고 수정 버튼을 만들었다.



## 소감

이 토이프로젝트는 페어로 진행해 보았다. 네비게이터와 드라이버의 역할을 바꿔보면서 진행했다. 그 과정에서 가상환경과 db를 삭제한 후에 전달하면 다시 가상환경을 설치하고 requirements.txt를 통해 패키지를 설치했다. 서로 더 알고 있는 부분들을 공유해 가면서 프로젝트를 해나갔다. 대체적으로 디테일한 기술적인 부분은 팀원이 알고 계신 것이 더 많았고 나는 전반적인 작동원리를 더 알아서 서로 알게된 점들이 많았던것 같다.

