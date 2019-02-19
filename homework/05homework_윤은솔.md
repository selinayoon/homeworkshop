# 05homework_윤은솔

### 함수

-----

#### 문제1

List는 for 문을 실행하면 모든 요소를 순차적으로 돌면서 반복문을 수행합니다.
임의의 리스트 my_list의 값을 하나씩 출력하는 코드를 아래에 작성하시오.

```python
#실행
my_list = ["안녕","안녕하세요","반갑습니다","반가워요","오랜만이네요"]

#for문으로 값 출력
for hello in my_list:
    print(hello)
```

```
#결과
안녕
안녕하세요
반갑습니다
반가워요
오랜만이네요
```

------

#### 문제2

위에 작성한 코드를 인덱스(index) 값과 함께 출력하는 코드로 변경하시오.

```python
#실행
for key, value in enumerate(my_list):
    print(f"인덱스: {key}, 값:{value}")
```

```
#결과
인덱스: 0, 값:안녕
인덱스: 1, 값:안녕하세요
인덱스: 2, 값:반갑습니다
인덱스: 3, 값:반가워요
인덱스: 4, 값:오랜만이네요
```

-------

#### 문제3

딕셔너리는 key, value로 구성되어 있습니다. 따라서, 딕셔너리 my_dict 각각의 상황에 따라 반복문을 수행할 수 있도록 빈칸을 채우시오.

key : for key in __________:
value : for value in ___________:
key와 value : for key, value in _________:

```python
#실행
my_dict = {'생년':'95','월':'10','일':'02'}

#key
for key in my_dict.keys():
    print(key)
    
#value
for value in my_dict.values():
    print(value)

#key 와 value 
for key, value in items(my_dict):
    print(f"키: {key}, 값:{value}")
```

```
#출력
생년
월
일
95
10
02
```

-------

#### 문제4

result에 저장된 값은?

def my_func(a, b):
c = a + b
print(c)
result = my_func(1, 5)

```python
#실행
def my_func(a, b): 
    c = a + b 
    print(c) 

result = my_func(1, 5)
print(result)
#정답 None
```

```
#출력
6
None
```

