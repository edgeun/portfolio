# 데이터 불러오기
wine <- read.csv("wine2.csv", stringsAsFactors = T) # 범주형 데이터 팩터로 변환해서 불러오기
head(wine)

# 데이터 살펴보기
nrow(wine) # 177
str(wine)

prop.table(table(wine$Type))
colSums(is.na(wine)) 

# 훈련데이터와 테스트데이터 분리하기
# install.packages("caret")
library(caret)
set.seed(1)

k <- createDataPartition(wine$Type, p = 0.9, list = F)

train_data <- wine[k, ]
test_data <- wine[-k, ]

nrow(train_data) # 161
nrow(test_data) # 16

ncol(train_data)
head(train_data)

# 모델 생성 및 훈련
# install.packages("C50")
library(C50)

wine_model <- C5.0(train_data[ , -1], train_data[ , 1])
summary(wine_model)

# 모델 예측
train_result <- predict(wine_model, train_data[ , -1])
test_result <- predict(wine_model, test_data[ , -1])

# 모델 평가
sum(train_result == train_data[ , 1]) / 161 * 100
sum(test_result == test_data[ , 1]) / 16 * 100

# 모델 개선하기 및 더 높은 정확도 값에 필요한 적절한 trial 값을 찾기 위한 for 루프문으로 모델 생성 및 예측결과로 정확도 계산
y <- 1  # 초기값 설정
jumpby <- 1  # jumpby 값 설정 (예: 1씩 증가)

for (i in 1:10) {
  # trials 값이 100을 넘지 않도록 제한
  trials <- min(y, 100)
  
  wine_model2 <- C5.0(train_data[, -1], train_data[, 1], trials = trials) 
  test_result2 <- predict(wine_model2, test_data[, -1])
  a <- sum(test_result2 == test_data[, 1]) / 16 * 100
  y <- y + jumpby
  print(paste(i, '일때', a))
  
  # 선택적: y가 100을 넘으면 루프 종료
  if (y > 100) break
}

# 거짓부정(FN)을 확인하기 위한 이원교차표 출력하기
# install.packages("gmodels")
library(gmodels)

wine_model2 <- C5.0(train_data[ , -1], train_data[ , 1], trials = 3) # 적절한 trials 값을 알았으므로 trials 값을 입력한 모델을 새로 생성
test_result2 <- predict(wine_model2, test_data[ , -1])

x <- CrossTable(test_data[ , 1], test_result2)

x$t

