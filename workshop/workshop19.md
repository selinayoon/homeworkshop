# 19workshop_윤은솔

## Python 활용 SQL

### 문제 1

17workshop에서 만든 모델을 활용해서
학생들의 정보를 저장하는 CRUD 페이지를 구현하세요

```
workshop 17번 이름 19번으로 변경
```

### 1-1 CREATE

#### /homeworkshop/workshop/workshop19/student/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("new/",views.new),
    path("create/",views.create),
]
```

#### /homeworkshop/workshop/workshop19/student/views.py

```python
from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def index(request):
    #studenyts에 전체 데이터 전달해 넣어주기
    students = Student.objects.all()
    return render(request,"student/index.html",{"students":students})
    
def new(request):
    return render(request,"student/new.html")
```

#### /homeworkshop/workshop/workshop19/student/templates/student/new.html

```html
{% extends "student/base.html" %}

{% block bodyblock %}
    <h1> NEW </h1>
    <hr>
    <h3>학생 정보 생성하기<h3>
    <form action="/students/create/" method="post">
        <!--자동으로 input 태그를 만들어 토큰 값을 저장해준다.-->
        {% csrf_token %}
        NAME: <input type="text" name="name"/>
        EMAIL: <input type="email" name="email"/>
        BIRTHDAY: <input type="date" name="birthday"/>
        AGE: <input type="number" name="age"/>
        <input type="submit" value="Submit"/>
    </form>
{% endblock %}    

```

#### /homeworkshop/workshop/workshop19/student/views.py

```python
from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def index(request):
    #studenyts에 전체 데이터 전달해 넣어주기
    students = Student.objects.all()
    return render(request,"student/index.html",{"students":students})
    
def new(request):
    return render(request,"student/new.html")
    
def create(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    birthday = request.POST.get("birthday")
    age = request.POST.get("age")
    
    Student.objects.create(name=name,email=email,birthday=birthday,age=age)
    
    return redirect("/students")
```

#### /homeworkshop/workshop/workshop19/student/templates/student/base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Students앱</title>
</head>
<body>
    <div class="container">
        <ul>
            <li><a href="/students/">인덱스</a></li>
            <li><a href="/students/new/">글쓰기</a></li>
        </ul>
        {% block bodyblock %}
    </div>
    {% endblock %}
</body>
</html>
```

-----

### 1-2. READ

#### /homeworkshop/workshop/workshop19/student/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("new/",views.new),
    path("create/",views.create),
    path("<int:id>/",views.read),
]
```

#### /homeworkshop/workshop/workshop19/student/templates/student/read.html

```html
{% extends "student/base.html" %}

{% block bodyblock %}
    <h1>이름: {{student.name}}</h1>
    <h3>이메일: {{student.email}}</h3>
    <h3>생년월일: {{student.birthday}}</h3>
    <h3>나이: {{student.age}}</h3>
{% endblock %}
```

#### /homeworkshop/workshop/workshop19/student/urls.py

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("students/",include("student.urls"))
]
```

#### /homeworkshop/workshop/workshop19/student/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("new/",views.new),
    path("create/",views.create),
    path("<int:id>/",views.read),
    ]
```

#### /homeworkshop/workshop/workshop19/student/templates/student/index.html

```html	
{% extends "student/base.html" %}

{% block bodyblock %}
    <h1>여기는 인덱스 입니다.</h1>
    <hr>
    {% for student in students %}
        <h3>이름: {{student.name}}</h3>
        <a href="/students/{{student.id}}">정보 보기</a>
        
    {% endfor %}
{% endblock %}    
```

#### /homeworkshop/workshop/workshop19/student/views.py

```python
from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def index(request):
    #studenyts에 전체 데이터 전달해 넣어주기
    students = Student.objects.all()
    return render(request,"student/index.html",{"students":students})
    
def new(request):
    return render(request,"student/new.html")
    
def create(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    birthday = request.POST.get("birthday")
    age = request.POST.get("age")
    
    Student.objects.create(name=name,email=email,birthday=birthday,age=age)
    
    return redirect("/students")
    
def read(request,id):
    student = Student.objects.get(pk=id)
    return render(request,"student/read.html",{"student":student})
```

-----

## DELETE

#### /homeworkshop/workshop/workshop19/student/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("new/",views.new),
    path("create/",views.create),
    path("<int:id>/",views.read),
    path("<int:id>/delete",views.delete)
    ]
```

