# 20homework_윤은솔

## 데이터베이스 관계(1:N)

### 문제1

Question 모델과 Comment 모델이 1:N관계라고 할때 하나의 Question을 보여 주는 페이지에서 Comment를 모두 보여주려고 한다. 다음과 같은 detail.html이 있을 때 모든 Comment의 content를 h3태그를 이용해서 출력하는 for문을 작성 하세요. (related_name은 설정해주지 않았다고 가정한다.)

```html
class Student(models.Model):
	#외래키: 어떤 정보를 가져올지(부모역할을 한다.)
    class_1 = models.ForeignKey(class_1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
```

---

### 문제2

다음과 같은 urls.py 파일이 있다고 가정할때 comment를 작성하는 버튼을 만들기 위해 form태그 안에 action속성값으로 넣어줘야 하는 경로를 작성하세요.

```python
A.student_set.all()
```

---

### 문제3

기본적으로 1:N관계를 설정을 할때 ForeignKey를 이용해서 1에 해당하는 클래스 를 지정해준다. 지정한 클래스가 Movie일때 ForeignKey로 지정된 컬럼의 이름은 무엇인가?

```bash
#답
movie_id


>>>from question.models import Comment
>>>Comment.objects.first()
<Comment: 뭔소리야??>
>>>Comment.objects.first().question
<Question: 파이썬 너무 쉬워요>


Comment.objects.first().question.id
```

