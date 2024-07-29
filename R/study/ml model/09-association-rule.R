# install.packages("arules")
library(arules)

# 예제 트랜잭션 데이터
data <- list(
  c("milk", "bread", "butter"),
  c("beer", "bread"),
  c("milk", "diapers", "beer", "bread"),
  c("bread", "butter")
)

# 트랜잭션 객체 생성
transactions <- as(data, "transactions")

# 트랜잭션 내용 확인
inspect(transactions)
