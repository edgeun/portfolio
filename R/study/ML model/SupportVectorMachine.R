# 데이터 로드 (변속기가 수동인지 자동인지를 분류하기 위한 데이터)
data(mtcars)

# am 변수를 팩터형으로 변환 (1 또는 0인 범주형 데이터이기 때문에)
mtcars$am <- as.factor(mtcars$am)

# 필요한 변수만 선택
mtcars_subset <- mtcars[, c("am", "mpg", "wt", "hp")]

# 훈련 데이터와 테스트 데이터를 분리
library(caret)
set.seed(1)

k <- createDataPartition(mtcars_subset$am, p = 0.7, list = FALSE)
train_data <- mtcars_subset[k, ]
test_data <- mtcars_subset[-k, ]

nrow(train_data) # 훈련 데이터의 개수 24
nrow(test_data)  # 테스트 데이터의 개수 8

# 모델 생성 및 하이퍼파라미터 설정
library(e1071)

# C와 gamma 값을 조정하여 모델 훈련
set.seed(1)
mtcars_svm_model <- svm(am ~ . , data = train_data, kernel = "radial", cost = 10, gamma = 0.1)

# 모델 예측
result <- predict(mtcars_svm_model, test_data[, -1]) # 종속변수(정답) 제외하고 예측함
result

# 모델 평가
accuracy <- sum(result == test_data$am) / length(test_data$am)
accuracy

# 교차 테이블
library(gmodels)
r1 <- CrossTable(x = test_data$am, y = result)
r1$t

# 정확도 및 교차 테이블 출력
cat("Accuracy: ", accuracy, "\n")
print(r1)
