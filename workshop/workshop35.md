## workshop35

# REST API

1.아래의 두 코드에 적절한 데코레이터를 작성하여 허용되지 않은 HTTP Method의 경우
405 Method Not Allowed 상태코드를 반환하도록 하시오.

```python
@require_http_methods(["GET","POST"])
def create():
	pass
```

