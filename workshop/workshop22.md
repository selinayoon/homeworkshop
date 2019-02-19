# 22workshop_윤은솔

## Media & Static Files

### 문제 1

항상 CDN으로만 사용해왔던 Bootstrap을 이번에는 직접 CSS, JS 파일로 다운로드 받 아 Django Project에 정적 파일로 추가하고 사용해보자.

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="C:\Users\student\Downloads\bootstrap-4.2.1-dist\bootstrap-4.2.1-dist\css">
</head>head>

<body>
<script src="C:\Users\student\Downloads\bootstrap-4.2.1-dist\bootstrap-4.2.1-dist\js"></script>
</body>
</html>
```

