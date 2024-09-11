# 필요한 패키지 설치 및 로드
if (!require("arules")) {
  install.packages("arules")
  library(arules)
}

# Groceries 데이터 로드
data("Groceries")

# 데이터 요약 확인
summary(Groceries)

# 처음 5개의 트랜잭션 확인
inspect(Groceries[1:5])

# 데이터의 전체 구조 확인
str(Groceries)

rules <- apriori(Groceries, parameter = list(supp = 0.01, conf = 0.5))
rules

# 상위 10개의 규칙을 lift의 기준으로 정렬
rules2 <- sort(rules, by='lift')
top_rules <- head(rules2, 10)
inspect(top_rules)
