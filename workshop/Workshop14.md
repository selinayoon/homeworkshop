# 14Workshop_윤은솔

## Django Web Framework



### 문제 1

이름이 first_workshop인 프로젝트를 생성해주세요

```bash
yooneunsol:~/workspace/homeworkshop/workshop (master) $ django-admin startproject workshop14
yooneunsol:~/workspace/homeworkshop/workshop (master) $ 
```

하면 자동으로 workshop 폴더 안에 자동 생성된다.

----

### 문제 2

 https://<your-server-url>/info 의 경로로 들어갔을 때 다음과 같이 반 정보를 보여주는 페이지를 만들어 주세요

#### 2-1.

#### app만들기

```bash
yooneunsol:~/workspace/homeworkshop/workshop (master) $ django-admin startapp info
yooneunsol:~/workspace/homeworkshop/workshop (master) $ 
```

#### 2-2.

#### /homeworkshop/workshop/workshop14/workshop14/settings.py

```python
#01. 템플릿 경로 지정
TEMPLATES_DIR = os.path.join(BASE_DIR,"templates") #템플릿 경로 지정
#02. 다 열어주겠다는 의미로 *로 설정하기
ALLOWED_HOSTS = ["*"]
#'03. info' 추가
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'info',
]
#04. 'DIRS': [TEMPLATES_DIR] 추가
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

#### 2-3.

#### /homeworkshop/workshop/workshop14/workshop14/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/',include("info.urls"))
]
```

#### 2-4.

#### /homeworkshop/workshop/workshop14/info/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),    
]
```

#### 2-5.

#### /homeworkshop/workshop/workshop14/info/views.py

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
```

#### 2-6.

#### /homeworkshop/workshop/workshop14/info/templates/index.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>우리반정보</h1>
    <h2>Teacher</h2>
    <ul>
        <li>Name</li>
    </ul>
    <h2>Student</h2>
    <ul>
        <li>홍길동</li>
        <li>김길동</li>
        <li>박길동</li>
    </ul>
</body>
</html>
```

---

### 문제 3

https://<your-server-url>/student/<학생이름>의 경로로 들어갔을 때 다음과 같이 학생의 이름과 나이를 보여주는 페이지를 만들어 주세요.

#### 3-1.

#### /homeworkshop/workshop/workshop14/info/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("student/<str:name>/",views.student),
]
```

#### 3-2.

#### /homeworkshop/workshop/workshop14/info/views.py

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def student(request,name):
    students = {"홍길동":24,"박길동":28,"김길동":30}
    age = students.get(name)
    return render(request,"student.html",{"name":name,"age":age})
```

#### 3-3.

#### /homeworkshop/workshop/workshop14/info/templates/student.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>이름:{{name}}</h1>
    <h2>나이:{{age}}</h2>
</body>
</html>
```







