# 10homework_윤은솔

### CSS

----

#### 문제1.

CSS 은무엇의약자인가?

```
(1) Creative Style Sheets 
(2) Cascading Style Sheets 
(3) Computer Style Sheets 
(4) Colorful Style Sheets
```

```
#답
(2) Cascading Style Sheets 
```

----

#### 문제2

다음 중 맞으면T, 틀리면F 를 기입하시오.

```
HTML과CSS는 각자 문법을 갖는 별개의 언어이다.[  T   ]
웹 브라우저는 내장기본스타일이 있어 CSS가 없어도 작동한다.[   T  ]
자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속받는다.[  F   ]
```

---

#### 문제3

크기 단위 em 은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이
즈를
설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하
기 위해
HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가?

```
#답
rem
```

---

#### 문제4

다음 예제를 통해 “후손셀렉터”와 “자식셀렉터”의 차이를 설명하시오.

```css
/*보기*/
/*후손 셀렉터*/
div p{
    color: crimson;
}

/*자식 셀렉터*/
div > p{
    color:crimson;
}
```

```
후손셀렉터는 자신과 자식의 P태그 모두에 영향을 미친다.
자식셀렉터는 자신의 P태그에만 영향을 미친다.
```

