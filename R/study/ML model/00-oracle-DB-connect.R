# 라이브러리 로드
# install.packages("rJava")
# install.packages("DBI")
# install.packages("RJDBC")

library(rJava)
library(DBI)
library(RJDBC)

driver <- JDBC('oracle.jdbc.driver.OracleDriver', 'c:\\data\\ojdbc8.jar') 

oracle_db <- dbConnect(driver, 'jdbc:oracle:thin:@127.0.0.1:1521/xe', 'c##scott','tiger')
# 오라클DB에 접속하기 위한 ip주소, 포트번호, 서비스 이름 입력
# 오라클DB 사용자 유저 이름, 비밀번호 입력

emp_query <- 'select e.ename, d.loc
                       from  emp  e, dept  d
                     where  e.deptno = d.deptno'

emp_data <- dbGetQuery( oracle_db, emp_query)
emp_data
