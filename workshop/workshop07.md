# 07workshop_윤은솔

## OOP

### 문제1

다음과 같은 클래스 Circle이 있다.

```python
#보기
class Circle():
    pi = 3.14
    x = 0
    y = 0
    r = 0
    def area(self): #넓이
        return self.pi *self.r * self.r
    def circumference(self): #둘레
        return 2 * self.pi *self.r
    def center(self): #새로운 좌표
        return (self.x,self.y)
    def move(self, x, y): #
        self.x = x
        self.y = y
```



반지름이 3이고 x,y 좌표가 (2.4)인 원을 만들어 넓이와 둘레를 출력하세요

```python
o1 = Circle()
o1.r = 3
o1.x = 2
o1.y = 4

a = o1.area()
b = o1.circumference()

print(f"넓이 : {a}, 둘레 {b}")
```

```python
#결과
넓이 : 28.259999999999998, 둘레 18.84
```



---

#### 문제2

두번째 원을 만들고 x,y좌표를(5,-5)로 이동시킨 후 첫번째 원과 외접하는 조건의 반지름을 구하세요.

```python
o2 = Circle()
o2.center = o1.move(5,-5)

o2.r = (((o1.x)-(o2.x))** 2 +((o2.y)-(o1.y))** 2)**0.5 -(o1.r)
print(o2.r)
```

```python
#결과
4.0710678118654755
```

