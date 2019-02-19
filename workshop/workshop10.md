# 10workshop_윤은솔

## CSS

### 문제 1.

Selector 를 활용한 DOM 탐색 실습. 

생각하는 대로 선택되지 않을 것이다. 그렇다면 nth-of-type 를 사용해 보자

```html
<!-- 보기 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <style>
        #ssafy>p:nth-child(3){
            /* nth-of-type : 같은요소 중 에서 세번째를 의미 */
            color:red;
        }
    </style>
    <div id="ssafy">
        <h2>어떤게 선택될까?</h2>
        <p>첫번째 단락</p>
        <p>두번째 단락</p>
        <p>세번째 단락</p>
        <p>네번째 단락</p>
    </div>
</head>
<body>
    
</body>
</html>
```

```html
<!-- 제출 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <style>
        #ssafy>p:nth-of-type(2) {
            /* nth-of-type : 다 포함해서 자식들끼리 경쟁해 몇번 째 자식인지 찾는다. */
            color:blue;
        }
    </style>
    <div id="ssafy">
        <h2>어떤게 선택될까?</h2>
        <p>첫번째 단락</p>
        <p>두번째 단락</p>
        <p>세번째 단락</p>
        <p>네번째 단락</p>
    </div>
</head>
<body>
    
</body>
</html>
```

