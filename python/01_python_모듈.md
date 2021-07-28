# 02_Python_모듈



## 모듈과 패키지

### 개요

#### 모듈

- 특정 기능을 파이썬 파일(.py) 단위로 작성한 것

#### 패키지

- 특정 기능과 관련된 여러 모듈의 집합
- 패키지 안에 또 다른 서브 패키지 포함
- 라이브러리와 buzzword관계



### 파이썬 표준 라이브러리

Python Standard Library.PSL

- 파이썬에 기본적으로 설치

- https://docs.python.org/ko/3/library/index.html
- https://github.com/python



### 파이썬 패키지 관리자(pip)

#### pip란?

- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
- pypi.org에서 패키지 확인 가능

#### pip 명령어

- 패키지 설치

  ```bash
  $pip install SomePackage # 최신버전
  $pip install SomePackage==1.0.5 # 특정 버전
  $pip install 'SomePackage>=1.0.4' # 최소 버전
  ```

- 패키지 삭제

  - pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌

  ``` bash
  $pip uninstall SomePackage

- 패키지 목록 및 특정 패키지 정보

  ``` bash
  $pip list # 목록
  $pip show SomePackage # 특정 패키지 정보
  ```

- 패키지 freeze

  - 설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용되는 형식으로 출력
  - 해당하는 목록을 requirements.txt(관습)으로 만들어 관리

  ```bash
  $pip freeze > requirements.txt # 목록 저장
  $pip install -r requirements.txt # 목록 설치
  ```

  

## 가상환경

### 개요

- 외부 패키지(3rd party 패키지)와 모듈을 사용하는 경우 모두 pip를 통해 설치해야함
- 여러 프로젝트를 진행하는 경우 버전이 상이할 수 있음
  - 프로젝트 a - django 버전 2.x
  - 프로젝트 b - django 버전 3.x
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음

### venv

#### venv란

- 가상 환경을 만들고 관리하는데 사용되는 모듈 (Python 버전 3.5부터)
- 특정 디렉토리에 가상환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  - 특정 폴더에 가상 환경이(패키지 집합 폴더 등) 있고
  - 실행 환경(예 - bash)에서 가상환경을 활성화 시켜
  - 해당 폴더에 있는 패키지를 관리 및 사용

#### 가상환경 생성

- 이 때 생성한 폴더는 그 위치에 있어야 한다. 내부 파일에 경로값이 들어가는 경우가 있기 때문. 
  - 다른 폴더로 옮기거나 github에 올리지 않는다.
  - 단 전체 프로젝트 폴더를 옮겨도 된다.

``` bash
$ python -m venv <폴더명> # <폴더명>에 가상환경 생성
```

#### 가상환경 활성화/비활성화

```bash
$ source <폴더명>/bin/activate # 가상환경 활성화 in bash
$ deactivate # 가상환경 비활성화
```

#### 현재 어떤 환경인지 확인

```bash
$ which python # 어떤 경로의 파이썬을 쓰는지 확인
```



## 커스텀 모듈/패키지 만들기

### 패키지 생성

- jupyter notebook 파일트리화면에서 New > Folder
- 다음과 같은 폴더구조 생성

```python
my_package/
    __init__.py
    math/
        __init__.py
        tools.py  
```

> 모듈 이름 `my_package.math`는 `my_package`라는 이름의 패키지에 있는 `math`라는 이름의 하위 패키지를 가리킵니다.

- `__init__.py`

  > python3.3 버전부터는 `__init__.py` 파일이 없어도 패키지로 인식합니다(PEP 420). 하지만 하위 버전 호환 및 일부 프레임워크에서의 올바른 동작을 위해 `__init__.py` 파일을 생성하는 것이 권장됩니다.

### 패키지 만들기 연습

#### [패키지 및 모듈 생성]

```py
my_package/
    __init__.py
    math/
        __init__.py
        tools.py  
    statistics/
        __init__.py
        tools.py
```

```python
# my_package/math/tools.py

pi = 3.14159265358979323846

e = 2.71828182845904523536

def my_max(a, b):
    if a > b:
        return a
    else:
        return b
```

```python
# my_package/statistics/tools.py

def standard_deviation(values):
    mean = sum(values) / len(values)
    sum_var = sum(pow(value - mean, 2) for value in values) / len(values)
    std_dev = math.sqrt(sum_var)
    return std_dev
```

### 다양한 모듈 사용법

#### 모듈

```python
import module
from module import var, function, Class
from module import *
```

#### 패키지

```python
from package import module
from package.module import var, function, Class
```

#### 예시

```python
import my_package.math.tools # import 활용해서 왼쪽 경로의 모듈 불러옴

from my_package.math.tools import e # from 과 import 활용해서 해당경로 모듈의 변수 e를 불러옴
print(e)

from my_package.math.tools import * # 왼쪽 경로의 모든 변수, 함수, 클래스 가져옴

# statistics 패키지 tools 모듈에 정의한 standard_deviation 함수를 짧은 이름(sd)으로 줄여봄
from my_package.statistics.tools import standard_deviation as sd
```



## 참고 - help와 dir

``` python
dir(클래스) # 클래스의 변수와 메소드를 나열해준다
help(클래스) # 클래스의 더 자세한 정보가 나온다
```

