# 데이터 불러오기 (데이터: mushrooms.csv)
mush <- read.csv("c:\\data\\mushrooms.csv", stringsAsFactors = TRUE) # 종속변수를 포함한 범주형 데이터, 팩터로 변환해서 불러오기

# 데이터 관찰하기
dim(mush)
str(mush)

# 훈련과 테스트 분할하기
library(caret)
set.seed(1)
k <- createDataPartition(mush$type, p = 0.8, list = F) # 훈련 데이터 80%
train_data <- mush[k, ]
test_data <- mush[-k, ]

nrow(train_data)
nrwo(test_data)

# 모델 훈련하기
library(e1071)
model <- naiveBayes(type ~ . , data = train_data, laplace = 0.00001) # naiveBayes 함수로 버섯 데이터의 빈도표를 우도표로 만들어 줌

# 테스트 데이터 예측하기
result <-  predict(model, test_data[ , -1]) # 정답 빼고 넣어주기

# 모델 평가하기
library(gmodels)
sum(result == test_data[ , 1] )  / length(test_data[ , 1]) * 100
CrossTable(x = result, y = test_data[ , 1], chisq = TRUE)

# 모델 개선하기 (for loop 문을 실행해서 적절한 FN 값과 정확도 조율하기)
library(e1071)
library(gmodels)

options(scipen = 999) # 소숫점 자리 전체 보기

y <- 0
jumpby <- 0.00001

for (i in 1:10) {
                 y <- y + jumpby
                 model2 <- naiveBayes(type ~ ., data = train_data, laplace = y) 
                 result2 <- predict(model2, test_data[, -1])
  
                 ## 이원 교차표의 출력을 억제
                 ct <- capture.output(a <- CrossTable(x = result2, y = test_data[, 1], print.chisq = FALSE))
  
                 fn_value <- a$t[1, 2]  # FN 값 추출
                 accuracy <- sum(result2 == test_data[, 1]) / length(test_data[, 1]) * 100
  
                 print(paste(y, '일때 FN 값', fn_value, '정확도는', accuracy))
}
