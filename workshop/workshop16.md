# 16workshop_윤은솔

### 문제 1.

저번 워크샵에서 아래 표와 같은 DB를 제작한 상태다.

```sqlite
yooneunsol:~/workspace/16workshop (master) $ sqlite3 tutorial.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> CREATE TABLE bands(
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT,
   ...> debut INTEGER
   ...> );
sqlite> INSERT INTO bands(id,name,debut) VALUES(1,"Queen",1973);
sqlite> INSERT INTO bands(id,name,debut) VALUES(2,"Coldplay",1998);
sqlite> INSERT INTO bands(id,name,debut) VALUES(3,"MCR",2001);
sqlite> SELECT * FROM bands;
1|Queen|1973
2|Coldplay|1998
3|MCR|2001
sqlite> .mod column
sqlite> .header on
sqlite> SELECT * FROM bands;
id          name        debut     
----------  ----------  ----------
1           Queen       1973      
2           Coldplay    1998      
3           MCR         2001      
sqlite> 
```

---

### 문제 2

해당 테이블을 수정하여, 다음과 같이 컬럼을 추가하고, 데이터를 삽입하라.

```sqlite
sqlite> ALTER TABLE bands ADD COLUMN 'members' INTEGER;
sqlite> UPDATE bands SET members=4 WHERE id=1;
sqlite> UPDATE bands SET members=5 WHERE id=2;                                    
sqlite> UPDATE bands SET members=9 WHERE id=3;                                    
sqlite> SELECT * FROM bands;                          
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
2           Coldplay    1998        5         
3           MCR         2001        9         
sqlite> 
```

---

### 문제3

Id 가 3인 레코드의 members 를 5로 수정하라.

```sqlite
sqlite> UPDATE bands SET members=5 WHERE id=3;                                    
sqlite> SELECT * FROM bands;
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
2           Coldplay    1998        5         
3           MCR         2001        5         
sqlite> 
```

---

### 문제4

Id 가 2인 레코드를 삭제하라.

```sqlite
sqlite> DELETE FROM bands WHERE id=2;
sqlite> SELECT * FROM bands;
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
3           MCR         2001        5         
sqlite> 
```

