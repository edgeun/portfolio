# 0626_SQL 튜닝_CBT 시험 예상문제 풀이

(6월 26일 점심 문제) 아래의 SQL을 튜닝하세요

```sql
select  job, empno, ename, sal,   ( select  sum(sal)
                                      from  emp   e
                                     where  e.empno <= b.empno 
                                       and  e.job = b.job )  sumsal
           from  emp   b
           order  by  job,  empno;
           
select * from table(dbms_xplan.display_cursor(null, null, 'ALLSTATS LAST'));
```

```sql
select  job, empno, ename, sal, sum(sal) over (partition by job order by empno asc) sumsal
 from emp;
 
select * from table(dbms_xplan.display_cursor(null, null, 'ALLSTATS LAST'));
```

![Un![Untitled 1](https://github.com/edgeun/portfolio-2024/assets/60956291/579685c4-f551-446b-bbd5-3d4d3e7836fc)


### **이수자 평가 예상 문제 1)**

---

### 문제 54: Sort Merge Join에 대한 설명으로 가장 적절한 것은? 답 1번

1. 양쪽 집합을 정렬하고 조인하며, 인덱스에 의해 이미 정렬된 집합은 정렬 없이 곧바로 조인에 참여하기도 한다.
2. 먼저 액세스한 테이블의 처리 범위에 따라 전체 일의 양이 결정된다. (x)
3. 오라클에서는 조인 연결고리에 Equi Join 조건이 하나라도 있어야 한다. (x)
4. 테이블별 검색조건은 전체 일의 양에 영향을 미치지 않는다.  (x)

### ⇒ 풀이

```sql
select /*+ leading(d, e) use_merge(e) */ e.ename, d.loc, e.deptno
  from emp  e, dept  d
 where e.deptno = d.deptno and d.loc = 'DALLAS';
 
select * from table(dbms_xplan.display_cursor(null, null, 'ALLSTATS LAST'));
```

3번 풀이 : sort merge 조인은 equi join 문법도 가능하지만 non equi join 문법도 가능합니다. 아래와 같이 non equi join 문법도 sort merge join 이 가능합니다.

```sql
select  /*+ leading(s,e) use_merge(e) */ e.ename, e.sal, s.grade
from  emp  e, salgrade   s
where  e.sal  between  s.losal  and  s.hisal;
```

1번 풀이 : 양쪽 집합을 정렬하고 조인하며, 인덱스에 의해 이미 정렬된 집합은 정렬 없이 곧바로 조인에 참여하기도 한다.

```sql
select  /*+ leading(d,e) use_merge(e) */ e.ename, e.sal, s.grade
from  emp  e, salgrade   s
where  e.sal  between  s.losal  and  s.hisal;
```

2번은 논란이 있는 보기이긴 한데 시험에 위와 같이 나오면 1번을 답으로 고르세요. 2번 보기는 sort merge 조인도 조인 순서에 따라 성능의 차이가 실제로는 있는데 hash 조인이나 nested loop 조인에 비해서는 그 중요도가 상대적으로 낮습니다.

---

### **이수자 평가 예상 문제 2)**

---

### 문제 56: Hash Join에 대한 설명으로 가장 적절한 것은? 답 4번

1. Hash Join은 둘 중 작은 집합(Build Input)을 읽어 Sort Area에서 테이블을 생성한다.
2. Hash Join하는 양쪽 테이블 모두 전체 범위를 읽으므로 양쪽 모두 부분범위처리가 불가능하다.
3. Build Input 해시(Hash) 키 값에 중복이 많을수록 Hash Join의 성능은 좋아진다.
4. Build Input 집합을 Hash Area에서 탐색할 때는 래치(Latch) 획득 과정이 없어서 빠르다.

### ⇒ 풀이

```sql
select /*+ leading(d, e) use_hash(e) */ e.ename, d.loc
  from emp  e, dept  d
 where e.deptno = d.deptno;
 
select * from table(dbms_xplan.display_cursor(null, null, 'ALLSTATS LAST'));
```

1번 풀이 : sort area가 아니라 hash area에 해쉬 테이블을 생성합니다.

2번 풀이 : 해쉬 조인은 보통 하나의 테이블로 메모리로 로드하고 다른 테이블을 스캔하여 조인하는 방식으로 수행이 됩니다.

만약에 사원 테이블에서 다음과 같이 직업이 SALESMAN만 검색하는 SQL문이라면 job에 인덱스가 있다면 직업이 SALESMAN을 검색할 때 부분 범위 처리를 하면서 해쉬 조인을 할 수 있습니다. 그러기 때문에 양쪽 모두를 전체 범위 처리하는건 아닙니다.

3번 풀이 : 중복된 데이터가 많다고 성능이 좋아지는건 하나도 없습니다. 해쉬 키 값에 중복이 많으면 해쉬 테이블의 버킷이 불균형해져서 해쉬 충돌이 증가하고 그로 인해 성능이 저하됩니다.

4번 풀이 : build input 집합은 메모리로 올라가는 해쉬 테이블을 말합니다. 이 집합을 찾을 때 메모리의 락인 latch를 획득하지 않아도 되기 때문에 성능이 빠릅니다. dept 테이블이 메모리로 올라갔고 emp 테이블의 관련된 데이터를 메모리의 데이터를 찾아서 조인하려고 할 때 latch 획득이 필요없습니다. 

---

### **이수자 평가 예상 문제 3)**

---

### 문제 57: Nested Loop Join에 대한 설명으로 가장 적절한 것은? 답 1번

1. 빠르게 결과를 조회할 수 있지만 조인 횟수가 많을수록 다른 조인 방법에 비해 성능 저하가 나타날 수 있다.
2. 3개 테이블이 NL 조인 시 선행 2개 테이블 조인 결과에 대한 부분집합을 생성 후 3번째 테이블과 조인을 시도한다.
3. PGA를 통해 조인하기 때문에 래치(Latch)에 대한 경합이 없다.
4. Driving Table은 반드시 인덱스를 통해 검색해야 한다.

### ⇒ 풀이

4번 풀이 : driving table은 먼저 읽는 테이블인데 위의 SQL에서 dept 테이블입니다.

loc에 인덱스가 없다면 full table scan 해도 됩니다.

3번 풀이 : PGA가 Program Global Area의 약자인데 오라클 서버 프로세서의 개별 메모리 영역입니다.

클라이언트 ——————————> 서버

user process ——— SQL ————> server process

```sql
select ename, sal
  from emp
 where job = 'SALESMAN'
 order by sal desc;
```

2번 풀이 : 맞는 말입니다. 그런데 가장 적절한거는 1번이 가장 적절합니다.

1번 풀이 : 빠르게 결과를 조회할 수 있지만 조인 횟수가 많을수록 다른 조인 방법에 비해 성능 저하가 나타날 수 있다.

nested  loop   조인은 대량의 데이터를 가지고 조인할 때 조인 횟수가 많으면
sort merge 조인이나 해쉬조인보다 성능저하가 더 심합니다.

답: 1번

---

### **이수자 평가 예상 문제 4)**

---

### 문제 58: 아래와 같은 SQL에서 나타날 수 있는 Join 기법으로 가장 적절한 것은? 답 4번

![Untitled](0626_SQL%20%E1%84%90%E1%85%B2%E1%84%82%E1%85%B5%E1%86%BC_CBT%20%E1%84%89%E1%85%B5%E1%84%92%E1%85%A5%E1%86%B7%20%E1%84%8B%E1%85%A8%E1%84%89%E1%85%A1%E1%86%BC%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6%20%E1%84%91%E1%85%AE%E1%86%AF%E1%84%8B%E1%85%B5%205f43f3ad48194ca4b2bb930526ab5d2f/Untitled%201.png)

1. HASH ANTI JOIN
2. HASH SEMI JOIN
3. NESTED LOOP ANTI JOIN
4. NESTED LOOP SEMI JOIN

### ⇒ 풀이

exists 문의 실행 계획도 서브 쿼리이므로 세미조인을 합니다. 서브 쿼리의 실행 계획은 세미조인 아니면 안티조인 입니다.

연산자가 in 이나 exists면 세미조인이고 연산자가 not in 이나 not exists면 안티조인을 합니다.

인덱스가 없다면 해쉬 세미조인이 가장 적절하지만 보기에 인덱스가 있으므로 인덱스가 있다면 nested loop 세미조인이 가장 적절합니다.

답 : 4번

---

### **이수자 평가 예상 문제 5)**

---

### 문제 59: Sort Merge Join에 대한 설명으로 가장 적절하지 않은 것은? 답 4번

1. 조인 칼럼에 적당한 인덱스가 없어서 NL 조인(Nested Loops)이 비효율적일 때 사용할 수 있다.
2. Driving Table의 개념이 중요하지 않은 조인 방식이다.
3. 조인 조건의 인덱스 유무에 영향을 받지 않는다.
4. EQUI(=) 조인 조건에서만 동작한다.

### ⇒ 풀이

between.. and 도 sort merge 조인이 됩니다

```sql
select /*+ leading(s,e) use_merge(e) */ e.ename, s.grade
  from  emp e,  salgrade  s
  where e.sal  between  s.losal  and  s.hisal;
```

---

### **이수자 평가 예상 문제 6)**

---

### 문제 60: Hash Join이 더 효과적일 수 있는 조건으로 가장 적절하지 않은 것은? 답 4번

1. 조인 칼럼에 적당한 인덱스가 없어 자연조인(Natural Join)이 비효율적일 때
2. 자연조인(Natural Join) 시 드라이빙(Driving) 집합 쪽으로 조인 액세스 양이 많아 Random 액세스 부하가 심할 때
3. 소트 머지 조인(Sort Merge Join)을 하기에는 두 테이블이 너무 커서 소트(Sort) 부하가 심할 때
4. 유니크 인덱스를 활용하여 수행시간이 적게 걸리는 소량 테이블을 온라인 조회하는 경우

### ⇒ 풀이

수행시간이 적게 걸리는 소량의 테이블 조인은 해쉬 조인보다는 nested loop 조인이 더 효율적입니다.

---

### 이수자 평가 예상 문제 7)

---

### 문제 61: 조인(Join) 방식 중에서 Hash Join을 선택하는 기준으로 가장 적절한 것은? 답 4번

1. 소량의 데이터를 주로 처리하며, 부분 범위 처리가 극대화되어야 한다. (x)
2. 쿼리의 조인 조건식이 범위 조건이다. (x) → 해쉬 조인은 이퀄(=) 조건일 때만 사용 가능
3. 쿼리 수행 시간이 짧고 수행 빈도가 높다. (x) → nested loop 조인 사용
4. 조인 칼럼에 적당한 인덱스가 없고, 조인 대상 테이블 중 한쪽 테이블의 크기가 작다.

### ⇒ 풀이

인덱스가 없다는것은  full table scan 을 할 수 밖에 없다는것이고 그러면 해쉬조인이 적당합니다. 그리고 한쪽 테이블이 작으면 더욱 해쉬  조인하기 좋습니다.  그 테이블을 메모리의 해쉬 테이블로 구성하면 되기 때문에 4번이 적절한 답입니다.

---

### 이수자 평가 예상 문제 8)

---

### 문제 62: TAB1, TAB2 순으로 NL 조인하도록 유도하려고 할 때, 빈칸 ①에 들어갈 힌트로 가장 적절한 것은? (단, DBMS는 오라클로 가정) 답 3번

![Untitled](0626_SQL%20%E1%84%90%E1%85%B2%E1%84%82%E1%85%B5%E1%86%BC_CBT%20%E1%84%89%E1%85%B5%E1%84%92%E1%85%A5%E1%86%B7%20%E1%84%8B%E1%85%A8%E1%84%89%E1%85%A1%E1%86%BC%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6%20%E1%84%91%E1%85%AE%E1%86%AF%E1%84%8B%E1%85%B5%205f43f3ad48194ca4b2bb930526ab5d2f/Untitled%202.png)

1. ORDERED(A B) USE_NL(B)
2. ORDERED USE_NL(TAB2)
3. LEADING(A) USE_NL(B)
4. DRIVING_SITE(A) USE_NL(B)

### ⇒ 풀이

```sql
select /*+ leading(d, e) usl_nl(e) */ e.ename, d.loc
  from emp  e, dept  d
 where e.deptno = d.deptno
 
-- 이렇게 해도 되고 다음과 같이 작성해도 됩니다.

select /*+ leading(d) usl_nl(e) */ e.ename, d.loc
  from emp  e, dept  d
 where e.deptno = d.deptno
 
-- 힌트 leading에 d, e 를 적어줘도 되고 d 만 적어줘도 된다.
```

---

### 이수자 평가 예상 문제 9)

---

### 문제 32: SELECT 문장의 실행 순서를 올바르게 나열한 것은? 답 4번

1. SELECT - FROM - WHERE - GROUP BY - HAVING - ORDER BY
2. FROM - SELECT - WHERE - GROUP BY - HAVING - ORDER BY
3. FROM - WHERE - GROUP BY - HAVING - ORDER BY - SELECT
4. FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY

---

### 이수자 평가 예상 문제 10)

---

### 문제 33: 5개의 테이블로부터 필요한 칼럼을 조회하려고 할 때, 최소 몇 개의 JOIN 조건이 필요한가? 답 3번

1. 2개
2. 3개
3. 4개
4. 5개

---
