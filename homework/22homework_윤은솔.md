# 22homework_윤은솔

## Media & Static Files

### 문제 1.

attachment column에 파일을 저장하려고 한다. 아래의 (a)에 정의 해야 하는 field는?

```python
class Post(models.Model):
    attachment = models.FileField()
```

---

### 문제 2.

사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더 내부의 '/uploaded_files'로 지정하고자 한다. 이 때, settings.py에 작성해야 할 설정 2가지와 이것이 의미하는 바를 간략하게 작성하시오.

```python
STATIC_URL = '/static/'
# STATICFILES_DIRS =[
#     os.path.join(BASE_DIR,"hihi")
# ]
```

```
#의미하는바
STATICFILES_DIRS: 개발 단계에서 사용하는 정적 파일이 위치한 경로들을 지정하는 설정 항목이다.

STATIC_URL: 웹페이지에서 사용할 정적 파일의 최상위 url경로이다. 최상위 경로 자체는 실제 파일이나 디렉터리가 아니며, url로만 존재하는 단위이다.
```

---

### 문제 3.

개발자가 작성한 CSS 파일이나 넣고자 하는 이미지 파일 등이 Django 프로젝트 폴더 내부의 '/assets'에 있 다. '이 폴더 안에 정적 파일이 있다.'라고 Django 프로젝트에게 알려주기 위해서 settings.py에 작성해야 하는 설정을 작성하시오.

```python
MEDIA_URL = '/uploaded_files/'
MEDIA_ROOT = os.path.join(BASE_DIR,"uploaded_files")
```

```
#의미하는 바
MEDIA_ROOT : 업로드가 끝난 파일을 배치할 최상위 경로를 지정하는 설정 항목

MEDIA_URL: STATIC_URL과 역할이 비슷하다. 웹페이지에서 사용할 정적 파일의 최상위 url경로이다. 

```

------