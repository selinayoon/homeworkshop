# 11homework_윤은솔

### Bootstrap & Grid System

---

#### 문제1

다음은 부트스트랩의 어떤 component 이며 아래와 같이 만들려면 어떤 class 를 주어야 하는
가.

```html
<!--답-->

<!--Button 컴포넌트이다. -->
<class="btn btn-danger">
```

---

#### 문제2

```html
<!--답-->

<!--Alerts 컴포넌트이다. -->
<div class="alert alert-primary" role="alert">
  Hello SSAFY?
</div>
```

---

#### 문제3

다음 빈칸을 채우시오.

“부트스트랩 그리드 시스템은 레이아웃을 ( ) 개의 column 으로,
( ) 개의 반응형 사이즈 조건을 사용하여 구축한다.”

```
#답
12개  column
5개 반응형 사이즈 조건 사용
```

---

#### 문제4

아래와 같은 분할을 grid system 을 활용하여 만들어 보시오.

```html
<!--예시에 사용된 css-->
<head>
    <style>
        div{
            border: solid 1px black;
        }
        .row{
            background-color: moccasin;
        }
    </style>
</head>
```

```html
<!--답-->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
        <head>
        <style>
            div{
                border: solid 1px black;
            }
            .row{
                background-color: moccasin;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-sm">
                    One of three columns
                </div>
                <div class="col-sm">
                    One of three columns
                </div>
                <div class="col-sm">
                    One of three columns
                </div>
            </div>
        </div>
    </body>
</html>
```

