# 06workshop_윤은솔

## 함수

#### 문제1

양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요. 

sqrt() 사용 금지

```python
def my_qrt(n):
    #left는 양의 정수이기 때문에 1보다는 크다.
    left = 1
    #n의 제곱근은 n보다 작기때문에 오른쪽 끝을 n으로 설정
    right = n
    answer = 0
    #구하려는 제곱근을 제곱한 결과와 m의 차이가 0.00001보다 크면 계속
    while abs(answer**2 - n)>0.00001:
        #양쪽 끝의 숫자의 중간 지점을 찾는다.
        answer = (left+right)/2
        #만약 answer의 제곱의 결과가 구해야하는 n보다 수직선상보다 왼쪽에 있다면 
        #왼쪽의 기준점을 바꿔준다.
        if answer**2 < n:
            left = answer
        else:
            right = answer
    return answer
    
print(my_qrt(2))
```

```python
#결과
1.414215087890625
```

