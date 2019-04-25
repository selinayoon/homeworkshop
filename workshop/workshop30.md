## workshop30

# M:N 관계

1.게시물의 해시태그를 구현하기 위하여 아래와 같이 객체-관계 다이어그램을 작성하였
다. 다이어그램을 바탕으로 models.py 에 Post 모델과 Hashtag 모델을 정의해본다.

```python
class Hashtag(models.Model):
    content = models.TextField()
   
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
  		hashtag = models.ManyToManyField(hashtag,related_name="",on_delete=models.CASCADE)
```

