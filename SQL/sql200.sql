## 출처: 초보자를 위한 SQL200제
CREATE DATABASE my_db;
USE my_db;


CREATE TABLE DEPT
       (DEPTNO number(10),
        DNAME VARCHAR2(14),
        LOC VARCHAR2(13) );


INSERT INTO DEPT VALUES (10, 'ACCOUNTING', 'NEW YORK');
INSERT INTO DEPT VALUES (20, 'RESEARCH',   'DALLAS');
INSERT INTO DEPT VALUES (30, 'SALES',      'CHICAGO');
INSERT INTO DEPT VALUES (40, 'OPERATIONS', 'BOSTON');

CREATE TABLE EMP (
 EMPNO               NUMBER(4) NOT NULL,
 ENAME               VARCHAR2(10),
 JOB                 VARCHAR2(9),
 MGR                 NUMBER(4) ,
 HIREDATE            DATE,
 SAL                 NUMBER(7,2),
 COMM                NUMBER(7,2),
 DEPTNO              NUMBER(2) );

INSERT INTO EMP VALUES (7839,'KING','PRESIDENT',NULL,'81-11-17',5000,NULL,10);
INSERT INTO EMP VALUES (7698,'BLAKE','MANAGER',7839,'81-05-01',2850,NULL,30);
INSERT INTO EMP VALUES (7782,'CLARK','MANAGER',7839,'81-05-09',2450,NULL,10);
INSERT INTO EMP VALUES (7566,'JONES','MANAGER',7839,'81-04-01',2975,NULL,20);
INSERT INTO EMP VALUES (7654,'MARTIN','SALESMAN',7698,'81-09-10',1250,1400,30);
INSERT INTO EMP VALUES (7499,'ALLEN','SALESMAN',7698,'81-02-11',1600,300,30);
INSERT INTO EMP VALUES (7844,'TURNER','SALESMAN',7698,'81-08-21',1500,0,30);
INSERT INTO EMP VALUES (7900,'JAMES','CLERK',7698,'81-12-11',950,NULL,30);
INSERT INTO EMP VALUES (7521,'WARD','SALESMAN',7698,'81-02-23',1250,500,30);
INSERT INTO EMP VALUES (7902,'FORD','ANALYST',7566,'81-12-11',3000,NULL,20);
INSERT INTO EMP VALUES (7369,'SMITH','CLERK',7902,'80-12-09',800,NULL,20);
INSERT INTO EMP VALUES (7788,'SCOTT','ANALYST',7566,'82-12-22',3000,NULL,20);
INSERT INTO EMP VALUES (7876,'ADAMS','CLERK',7788,'83-01-15',1100,NULL,20);
INSERT INTO EMP VALUES (7934,'MILLER','CLERK',7782,'82-01-11',1300,NULL,10);

commit;


-- 모든 열 출력
SELECT *
 FROM emp;
 
SELECT empno, ename, job, mgr, hiredate, sal, comm, deptno
 FROM emp;
 
-- 컬럼 별칭
SELECT empno AS 사원번호, ename AS 사원이름, sal AS "Salary"
 FROM emp;
 
-- 연결 연산자
SELECT ename || sal -- mysql에서는 concat 함수 사용 ||은 or 연산자
 FROM emp;

SELECT CONCAT(ename, '의 월급은 ', sal, ' 입니다.') AS "사원의 월급 정보"
 FROM emp;
 
-- 중복 데이터 제거해서 출력
SELECT DISTINCT job
 FROM emp;
 
-- 데이터 정렬 
SELECT ename, sal
 FROM emp
 ORDER BY sal ASC;
 
SELECT ename, sal AS 월급
 FROM emp
 ORDER BY 월급 ASC;
 
SELECT ename, deptno, sal
 FROM emp
 ORDER BY deptno ASC, sal DESC;
 
SELECT ename, deptno, sal
 FROM emp
 ORDER BY 2 ASC, 3 DESC;

-- WHERE절
SELECT ename, sal, job
 FROM emp
 WHERE sal = 3000;
 
SELECT ename AS 이름, sal AS 월급
 FROM emp
 WHERE sal >= 3000;
 
SELECT ename, sal, job, hiredate, deptno
 FROM emp
 WHERE ename='SCOTT';
 
SELECT ename, hiredate
 FROM emp
 WHERE hiredate = '81/11/17';
 
SELECT *
 FROM NLS_SESSION_PARAMETERS
 WHERE PARAMETER = 'NLS_DATE_FORMAT';

ALTER SESSION SET NLS_DATE_FORMAT='YY/MM/DD';  -- 오라클 SQL -- 연도 RR(50년 기준 전/현/다음세기 출력), YY(현재세기) 구분 주의
 
SELECT @global.date_format;

SET @session.date_format = '%Y-%m-%d %H:%i:%s';  -- mySQL -- y(소문자): 두자리 연도, Y(대문자): 네자리 연도

SELECT @session.date_format;  -- %Y-%m-%d %H:%i:%s

-- 산술 연산자
SELECT ename, sal * 12 AS 연봉
 FROM emp
 WHERE sal * 12 >= 36000;
 
SELECT ename, sal, comm, sal + comm
 FROM emp
 WHERE deptno = 10;
 
-- 비교 연산자
SELECT ename, sal, job, deptno
 FROM emp
 WHERE sal <= 1200;
 
SELECT ename, sal
 FROM emp
 WHERE sal BETWEEN 1000 AND 3000;
 
SELECT ename, sal
 FROM emp
 WHERE (sal >= 1000 AND sal <= 3000);
 
SELECT ename, sal
 FROM emp
 WHERE ename LIKE 'S%';
 
SELECT ename
 FROM emp
 WHERE ename LIKE '_M%';
 
SELECT ename
 FROM emp
 WHERE ename LIKE '%T';
 
SELECT ename
 FROM emp
 WHERE ename LIKE '%A%';
