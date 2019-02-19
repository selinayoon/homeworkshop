# 19homework_윤은솔

## DB / Model 기초(CRUD)

### 문제 1

Django에서는 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행의를 특정
웹 사이트에 요청하게 하는 공격을 막는 기능을 기본적으로 동작시킨다. 위의 공
격은 어떤걸 의미 하는가?

```
CSRF 공격
```

---

### 문제 2

기본적으로 Django에서 views.py에 함수들을 정의할때 request인자값을 넣어줘야
한다. request를 활용해서 아래의 폼을 통해서 들어온 데이터를 가져오는 코드를
작성하세요

```html
<!--보기-->
form action="create" method="post">
    <input type="text" name="name"/>
    <input type="submit" value="Submit"/>
</form>
```

```python
def create(request):
    title = request.POST.get("title")
```

---

### 문제 3

다음은 사용자가 이미 작성한 글을 수정하기 위해서 기존의 글을 보여주는
edit페이지를 위한 views.py의 코드이다.

```python
#보기
def edit(request,id):
	post = Post.objects.get(id=id)
	return render(request,'board/edit.html',{'post':post})
```



아래의 코드에 기존의 데이터를 보여줄 수 있도록 코드를 수정하세요

```html
    <form action="/Posts/{{post.id}}/update/" method="post">
        <!--자동으로 input태그를 만들어 토큰값을 저장해준다-->
        {% csrf_token %}
        <input type="text" name="title" value="{{post.title}}"/>
        <input type="text" name="content" value="{{post.content}}"/>
        <input type="submit" value="Submit"/>
    </form>
```

