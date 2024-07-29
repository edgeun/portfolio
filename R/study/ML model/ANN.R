# 데이터 불러오기 (data: concrete.csv)
concrete <- read.csv("c:\\data\\concrete.csv")
head(concrete)

nrow(concrete) # 1030
ncol(concrete) # 9 

# 데이터 살펴보기: 결측치가 있는지 확인
colSums(is.na(concrete))

# 데이터 최대 최소 정규화하기 : 수치형(연속형) 독립변수를 0 ~ 1사이로 변경
normalize <- function(x) {
  return((x-min(x)) / (max(x) - min(x)))
}

concrete_norm <- as.data.frame(lapply(concrete, normalize)) # 종속변수도 숫자여서 분리하지 않고 같이 정규화 시킴

head(concrete_norm)
summary(concrete_norm)

# 훈련 데이터와 테스트 데이터 분리하기
library(caret)
set.seed(1)
k <- createDataPartition(concrete_norm$strength, p = 0.8, list = F)

train_data <- concrete_norm[k, ]
test_data <- concrete_norm[-k, ]

nrow(train_data) # 826
nrow(test_data) # 204

# 모델 생성 및 훈련하기
# install.packages("neuralnet")
library(neuralnet)

set.seed(1)
concrete_model <- neuralnet(formula = strength ~ cement + slag + ash + water + 
                                                 superplastic + coarseagg + fineagg + age,
                                                 data = train_data)

# 신경망을 시각화하기
plot(concrete_model)

# 테스트 데이터 예측하기
result <- compute(concrete_model, test_data[ , 1:8])  
result$net.result

# 모델 성능 평가하기
cor(result$net.result, test_data[ , 9]) # 0.8246728



# 모델 성능 개선하기: 위의 신경망 의 층수(위 기준 2층)를 늘리고 뉴런수 늘리기
set.seed(1)
concrete_model <- neuralnet(formula = strength ~ cement + slag + ash + water + 
                                                 superplastic + coarseagg + fineagg + age,
                                                 data = train_data, hidden = c(5, 2))

# hidden = c(5, 2) => 5가 은닉1층의 뉴런수, 2가 은닉2층의 뉴런수

# 뉴런수 변경한 신경망 시각화하기
plot(concrete_model)

# 테스트 데이터 예측하기
result <- compute(concrete_model, test_data[ , 1:8])
result$net.result

# 모델 성능 평가하기
cor(result$net.result, test_data[ , 9]) # 0.9351368
