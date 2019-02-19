# 05workshop_윤은솔

## 함수

### 문제 1

Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 

따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다. 



따라서, 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.

```python
def palindrome(words):
    if len(words)%2 ==0:
        #짝수 : 대칭끼리 비교
        for i in range(len(words)//2): #반잘라서 대칭으로 비교
            if words[i] == words[-(i+1)]:
                continue
            else:
                return False
        return True
    else:
        #홀수 : 가운데 글자 제외하고 비교 
        a = list(words)
        a.pop(len(words)//2)
        
        for i in range(len(a)//2): #반잘라서 대칭으로 비교
            if a[i] == a[-(i+1)]:
                continue
            else:
                return False
        return True
    
print(palindrome("토마토"))
print(palindrome("nan"))
print(palindrome("nanta"))
print(palindrome("naen"))

print("----")
#강사님코드
def palindrome2(word):
    list_word = list(word)
    for i in range(len(list_word)//2):
        if list_word[i] != list_word[-i-1]:
            return False
    return True
print(palindrome2("토마토"))
print(palindrome2("nan"))
print(palindrome2("nanta"))
print(palindrome2("naen"))

def short_palin(word):
    return list(word) == list(reversed(word))

print("----")
print(short_palin("토마토"))
print(short_palin("nan"))
print(short_palin("nanta"))
print(short_palin("naen"))
```

```python
#결과
True
True
False
False
----
True
True
False
False
----
True
True
False
False
```

