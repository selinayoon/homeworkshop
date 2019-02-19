# 15homework_윤은솔

### Django Web Framework

---

#### 문제1

우리가 사용하는 SQLite 는 RDBMS 에 속한다. RDBMS 의 특징을 2가지만 작성하
세요.

```bash
#답
1. 관계형 모델을 기반으로하는 데이터베이스 관리시스템이다.
2. SQL을 사용하여 데이터를 관리한다.
SQL은 Structured Query Language로서 데이터를 접근하는데 사용하는 언어이다
```

---

#### 문제2

True False

```
2.1. RDBMS를 조작하기 위해서는 SQL 문을 사용한다. [T] 
2.2. SQL 에서 명령어는 대문자로 써야만 동작한다. [F] 
2.3. 일반적인 SQL 문에서 명령어는 세미콜론(;) 으로 끝난다. [T] 
2.4. SQLite 에서 dot(.) 으로 시작하는 명령어는 SQL이 아니다.[T] 
	=>SQLite이다.
2.5. 한 개의 DB 에는 한개의 테이블만 존재한다. [F]
```

---

#### 문제3

다음 코드의 실행 결과로 나타나는 값을 작성하세요.

```bash
sqlite> .nullvalue “NULL”
sqlite> CREATE TABLE ssafy (
...> id INTEGER,
...> location TEXT,
...> class INTEGER
...> );
sqlite> INSERT INTO ssafy (id, location)
...> VALUES (1, ‘JEJU’);
sqlite> SELECT class FROM ssafy WHERE id=1;
```

```bash
#정답
null
```

