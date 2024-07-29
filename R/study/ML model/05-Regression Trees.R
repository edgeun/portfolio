#### 회귀 트리 ? 의사결정트리 + 회귀분석 => 의사결정트리에 수치형(연속형) 데이터의 회귀분석을 결합한 형태

# 데이터를 불러오기 (data: whitewines.csv)
wine <- read.csv("c:\\data\\whitewines.csv", header = T)
head(wine)
unique(wine$quality) # 퀄리티(종속변수)의 값에 뭐가 있는지 중복을 제거해서 출력

# 종속변수가 정규분포에 속하는 안정적인 데이터인지 확인하기
hist(wine$quality) # 히스토그램 결과 데이터가 치우치지 않고 안정적임

# 결측치가 있는지 확인하기
colSums(is.na(wine))

# 훈련 데이터와 테스트 데이터 분리하기
# install.packages("caret")
library(caret)
set.seed(1)
train_num <- createDataPartition(wine$quality, p = 0.9, list = F)

train_data <- wine[train_num, ]
test_data <- wine[-train_num, ]

nrow(train_data) # 4409
nrow(test_data) # 489

# 훈련 데이터로 모델 생성하기
# install.packages("rpart")
library(rpart)
model <- rpart(quality ~ . , data = train_data)
model

# 생성된 모델 시각화하기
# install.packages("rpart.plot")
library(rpart.plot)

rpart.plot(model, digit = 3) # digit = 3 은 소수점 3번째 자리까지 허용하겠다


# 모델 성능 높이기(모델트리 모델 사용하기)
#### 모델 트리 ? 회귀 트리의 보완된 모델 => 의사결정트리의 분류 기준을 수치형(연속형) 데이터로 분류한 후 각각 분류된 데이터에 선형회귀를 적용하는 모델
# install.packages("Cubist")
library(Cubist)

model2 <- cubist(x = train_data[ , -12], y = train_data[ , 12])
model2

## 훈련된 위의 모델로 테스트 데이터를 예측하기
result2 <- predict(model2, test_data[ , -12])
result2

## 위의 모델의 성능 확인
cor(result2, test_data[ , 12]) # 0.51 => 0.59로 상관계수가 올라감
