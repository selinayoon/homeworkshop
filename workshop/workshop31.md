## workshop31

# 데이터베이스 유효성 검사

1.데이터베이스에 값을 추가할 때, 아래와 같이 검증하려고 한다. 적절한 코드를 작성하시오.

```python
from django.db import models
from django.core.validators import EmailValidator, MinValueValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, validators=[EmailValidator(message="이메일 아님")])
    age = models.IntegerField(validators=[MinValueValidator(20, message="미성년자")])
```

