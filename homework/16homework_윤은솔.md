# 16homework_윤은솔

### Django Web Framework

----

#### 아래 동작을 수행하기 위한 SQL을 각각 작성하세요.

#### 문제1

다음과 같은 스키마를 가지는  DB테이블 friends를 생성한다.

```bash
yooneunsol:~/workspace/16workshop (master) $ sqlite3 tutorial.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> CREATE TABLE friends(
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT,
   ...> location TEXT
   ...> );
sqlite> .schema
CREATE TABLE friends(
id INTEGER PRIMARY KEY,
name TEXT,
location TEXT
);
sqlite> 
```

---

#### 문제2

해당 테이블에 다음과 같이 데이터를 입력한다.

```bash
sqlite> INSERT INTO friends(id,name,location) VALUES(1,"Justin","Seoul");
sqlite> INSERT INTO friends(id,name,location) VALUES(2,"Simon","New York");
sqlite> INSERT INTO friends(id,name,location) VALUES(3,"Chang","Las Vegas");
sqlite> INSERT INTO friends(id,name,location) VALUES(4,"John","Sydney");
sqlite> SELECT * FROM friends;
1|Justin|Seoul
2|Simon|New York
3|Chang|Las Vegas
4|John|Sydney
sqlite> .mod column
sqlite> .header on
sqlite> SELECT * FROM friends;
id          name        location  
----------  ----------  ----------
1           Justin      Seoul     
2           Simon       New York  
3           Chang       Las Vegas 
4           John        Sydney    
sqlite> 

```

---

#### 문제3

스키마를 다음과 같이 변경한다.

```bash
sqlite> SELECT * FROM friends;
id          name        location  
----------  ----------  ----------
1           Justin      Seoul     
2           Simon       New York  
3           Chang       Las Vegas 
4           John        Sydney    
sqlite> DELETE FROM friends;                                                  sqlite> SELECT * FROM friends;                                                sqlite> 
```

---

#### 문제4

데이터를 다음과 같이 추가한다.

```bash
sqlite> DELETE FROM friends;
sqlite> ALTER TABLE friends ADD COLUMN 'married' INTEGER;                     
sqlite> INSERT INTO friends(id,name,location,married) VALUES(1,"Justin","LA",1); sqlite> INSERT INTO friends(id,name,location,married) VALUES(2,"Simon","New York",0);
sqlite> INSERT INTO friends(id,name,location,married) VALUES(3,"Chang","LasVegas",0);
sqlite> INSERT INTO friends(id,name,location,married) VALUES(4,"John","Sydney",1); 
sqlite> SELECT * FROM friends;id          name        location    married   
----------  ----------  ----------  ----------
1           Justin      LA          1         
2           Simon       New York    0         
3           Chang       LasVegas    0         
4           John        Sydney      1         
sqlite> 
```

---

#### 문제5

married가 0인 데이터를 모두 삭제한다.

```bash
sqlite> DELETE FROM friends WHERE married=0;
sqlite> SELECT * FROM friends;
id          name        location    married   
----------  ----------  ----------  ----------
1           Justin      LA          1         
4           John        Sydney      1         
sqlite> 
```

---

#### 문제6

테이블을 삭제한다.

```bash
sqlite> Drop TABLE friends;
sqlite> .schema
sqlite> 
```

