# 21workshop_윤은솔

## 데이터베이스관계(1:N)

### 문제1

투표를 위한 설문조사 앱을 만들려고한다. 이 앱은 질문에 대한 답변을 투표하여 각 각의 항목이 몇표를 받았는지 저장하는 기능을 가지고 있다. 설문조사 앱은 Question 모델과 Choice 모델을 가지고 있다. 그리고 각각의 모델은 다음과 같은 컬럼을 가지고 있고 1:N 관계를 가지고 있다.

Question 하나를 보여주는 페이지에서 Choice를 위의 오른쪽 그림과 같이 출력하려 고 한다. html파일에서 내용과 투표수를 출력해주는 코드를 작성하세요. 현재 html파 일에는 아래와 같은 코드가 들어있다고 가정한다.



#### models.py 

```python
from django.db import models
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
  
    def __str__(self):
        return self.title
        
class Choice(models.Model):
    #어떤정보를 가져올지 (부모역할): on_delete=models.CASCADE
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    votes = modelf.IntegerField()
    
    def __str__(self):
        return self.content
```



#### html

```html
{% extends "question/base.html" %}

{% block bb %}
<h1>{{question.title}}</h1>
    {% for choice in question.choice_set.all %}
		<h4>{{choice.content}}:{{choice.votes}}표</h4>
    {% endfor %}
{% endblock %}
```



