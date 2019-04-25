## WORKSHOP24

# Django

Function Based View로 작성된 다음의 코드를 온전히 동일하게 동작하는 Class Based
View로 다시 작성해 보자. (TemplateView 사용)
v Project의 이름은 ‘fbv’이고, App의 이름은 ‘pages’이다.
v fbv/urls.py

```python
class HelloView(TemplateView):
    http_method_names = ['get']
    template_name = "intro/hello.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = kwargs.get('name')
        return context
```

