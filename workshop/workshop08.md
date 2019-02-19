# 08homework_윤은솔

## Flask

### 문제 1.

Flask에서 Dictionary 자료형을 이용하여 다음 조건을 만족하는 ‘나만의 영어 단어장’
페이지를 만들어보세요.

#### 08workshop.py

```python
# 08workshop.py
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dictionary/<string:word>") 
def dictionary(word):
    words={"apple":"사과","banana":"바나나","kiwi":"키위","melon":"메론","watermelon":"수박"}
    if word in dict.keys(words):
        # 딕셔너리에서 키 값이 있는 지 찾아보려면 dict.keys() 함수를 사용한다.
        result = f"{word}의 뜻은 {words[word]}입니다."
    else:
        result = f"{word}는 등록되어있지 않은 단어입니다."
    return render_template("dictionary.html",result = result)
   
if __name__=="__main__":
    #디버그모드를 통해 08workshop.py로 실행되게 한다.
    app.run(debug=True,host="0.0.0.0",port=8080)
```

#### dictionary.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>dictionary 페이지 입니다.</h1>
    {{result}}
</body>
</html>
```

#### bash

```bash
python 08workshop.py
```

