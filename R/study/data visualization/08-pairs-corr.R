# 패키지 설치
# install.packages("psych")
library(psych)

# 데이터 불러오기 (data: challenger.csv)
cha <- read.csv("c:\\data\\challenger.csv", header = T)

# pairs 패키지를 이용하여 종속변수와 독립변수들끼리의 상관관계 확인
pairs.panels(cha, pch = '.')
