# 04workshop_윤은솔

## Python 1. 파이썬 기초

### 문제 1

두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로 의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

```python
n = int(input("숫자를 입력하세요 : "))
m = int(input("숫자를 입력하세요 : "))
a = ('*'*n)+"\n"
print(a*m)
```

```
#출력
숫자를 입력하세요 : 5
숫자를 입력하세요 : 4
*****
*****
*****
*****
```

----

### 문제2

다음 딕셔너리에서 평균 점수를 출력하시오.

```python
student = {'python':80, 'algorithm':99, 'django':89, 'flask':83}
a=0
for score in student.values():
    a=score+a
print(a/len(student))
```

```
#출력
87.75
```

---

### 문제3

다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.

```python
blood = ['A','B','O','A','AB','AB','O','A','B','O','B','AB']
A = 0
B = 0
O = 0
AB = 0
for i in blood:
    if i =='A':
        A=A+1
    elif i == 'B':
        B=B+1
    elif i=='O':
        O=O+1
    elif i =='AB':
        AB=AB+1
else:
    print(f"A형:{A},B형:{B},O형:{O},AB형:{AB}")
```

---

