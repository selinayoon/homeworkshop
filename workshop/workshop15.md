# 15workshop_윤은솔

## Django Web Framework

### 문제 1

아래 표와 같은 스키마를 가진 DB 테이블을 생성하고, 아래와 같이 Data 를 입력해 봅 시다.

```squlite
yooneunsol:~/workspace/15workshop (master) $ sqlite3 tutorial.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .schema bands
sqlite> CREATE TABLE bands(
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT,
   ...> debut INTEGER);
sqlite> INSERT INTO bands(id,name,debut)                                                                        
   ...> VALUES(1,"QUEEN",1973);                                                                                 
sqlite> INSERT INTO bands(id,name,debut)                                                                        
   ...> VALUES(2,)                                                                                              
   ...> 
   ...> ;
Error: near ")": syntax error
sqlite> INSERT INTO bands(id,name,debut) VALUES(2,"Coldplay",1998);                                             
sqlite> INSERT INTO bands(id,name,debut) VALUES(3,"MCR",2001);                                                  
sqlite> SELECT * FROM bands;
1|QUEEN|1973
2|Coldplay|1998
3|MCR|2001
sqlite> .mode csv
sqlite> .mod column
sqlite> .header on
sqlite> SELECT * FROM bands;
id          name        debut     
----------  ----------  ----------
1           QUEEN       1973      
2           Coldplay    1998      
3           MCR         2001      
sqlite> 

```

---

### 문제 2

bands 테이블에서 모든 데이터 레코드의 id 와 name 만 조회하는 Query 를 작성하라.

```sql
sqlite> SELECT id,name from bands;
id          name      
----------  ----------
1           QUEEN     
2           Coldplay  
3           MCR       
sqlite> 
```

---

### 문제 3

bands 테이블에서 debut 가 2000 보다 작은 밴드들의 이름만을 조회하는 Query 를 작성하라.

```sqlite
sqlite> SELECT name FROM  bands WHERE debut<=2000;                                                            
name      
----------
QUEEN     
Coldplay  
sqlite> 
```

