# 07homework_윤은솔

### OOP

------

#### 문제1

파이썬에서은 객체지향프로그래밍 언어입니다.

파이썬에서 기본적으로 정의된 클래스 5개만 작성해보세요.

```python
#실행
int
str
complex
bool
float
```

---

#### 문제2

아래의 코드에서 x의 데이터타입을 확인하고자 할 때, 기본적으로 type(x) == int로 비교할 수 있다.

x = 3

뿐만 아니라 클래스 – 인스턴스 관계를 활용하여 확인할 수도 있는데, 이 때 사용되는 함수를 작성해보세요.

```python
#실행
isinstance(555555,int)
```

```
#결과
True
```

---

#### 문제3

우리가 지금껏 문자열, 리스트, 딕셔너리 등을 조작할 때 활용하였던 것은 모두 클래스에 정의된 메소드를
활용한 것이다. 예를 들면, 리스트를 정렬할 때 다음과 같이 코드를 작성할 수 있다.

numbers = [5, 1, 2]
numbers.sort()
print(numbers)

이처럼 지금껏 활용했던 문자열, 리스트, 딕셔너리 메소드 중 3가지만 작성해보세요.

```python
numbers = [5,1,2]
numbers.sort()
print(numbers)

a = "fawefwaef".upper()
print(a)

b = "fawefwaef".lower()
print(b)

c = "fawefwaef".capitalize()
print(c)
```

```
#결과
[1, 2, 5]
FAWEFWAEF
fawefwaef
Fawefwaef
```

----

#### 문제4

각각의 인스턴스들은 데이터 어트리뷰트(data attribute)를 가지고 있다. 다음의 코드는 복소수의 허수부의
값을 확인할 수 있으며, 이는 복소수 클래스(complex)면 모두 가지고 있다.

num = 3+4j
num.imag

변수 num의 실수부를 출력하는 코드를 아래에 작성해보고, 메소드 호출과 차이점을 확인해보자.

```python
#실행
num = 1+6j
num.real

#차이점 : ()있냐 없냐
```

```
#결과
1.0
```



