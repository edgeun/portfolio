#### 단순 회귀

# 데이터 로드 (data: regression.txt 애벌레 사료 데이터)
reg <- read.table("c:\\data\\regression.txt", header = T)
reg

# 데이터로 산포도 그래프 그리기
attach(reg)
plot(growth ~ tannin, data = reg, pch = 21, col = 'blue', bg = 'blue', cex = 2) # plot(y ~ x, data = 데이터프레임명)

# 단순회귀 모델 생성해서 기울기와 절편 구하기
model <- lm(growth ~ tannin, data = reg)
model

# 산포도 그래프와 회귀직선을 겹쳐서 시각화하기
abline(model, col = 'red')

y_hat <- predict(model, tannin = tannin) # 훈련 데이터로 예측 값 출력
join <- function(i) # join 이라는 이름의 함수 생성
  lines(c(tannin[i], tannin[i]), c(growth[i], y_hat[i]), col = "green") # 실제 값(파란점)과 예측 값(회귀직선)를 잇는 선을 그리기
sapply(1:9, join) # sapply 함수로 join 함수에 숫자 1부터 9까지 전달

# 단순회귀 분석하기
summary(model)


#### 다중 회귀

# 데이터 불러오기 (data: insurance.csv 미국 의료비 데이터)
ins <- read.csv("c:\\data\\insurance.csv", header = T)
head(ins)

# 데이터 살펴보기
View(ins)
colSums(is.na(ins))

# 다중회귀 분석 모델 생성하기
model <- lm(expenses ~  . -id, data = ins)
# model <- lm(expenses ~ age + children + sex + smoker + region + bmi, data = ins) # 또는 id 컬럼을 제외한 모든 컬럼 적기

# 소수점 옵션 사용하고 model 출력하기
options(scipen = 999)
model

# 회귀 분석 결과 해석하기
summary(model)

# Multiple R-squared: 0.7509, p-value: < 0.00000000000000022
# p value 값이 작으므로 대립가설 채택할 충분한 근거가 있음 (유의미함)

# 회귀 분석 모델의 성능 높이기
# 파생변수 추가해서 새 모델 생성하기
ins$bmi30 <- ifelse(ins$bmi >= 30, 1, 0) # 비만이면 1, 아니면 0의 파생변수 추가
head(ins)

## 혹은 파생변수를 따로 생성하지 않고 바로 lm 함수에 넣기
model3 <- lm(expenses ~ age + children + bmi + smoker + bmi30*smoker, data = ins)
summary(model3)

model <- lm(expenses ~ ., data = ins)
summary(model) # Multiple R-squared: 0.7559

ins$smoker_bmi30 <- ifelse(ins$smoker == 'yes' & ins$bmi >= 30, 1, 0)
head(ins)

model2 <- lm(expenses ~ ., data = ins)
summary(model2) # Multiple R-squared: 0.8639

#### 수치형(연속형) 데이터 정규화하기
## 정규화 하지 않고 lm 함수 돌렸을 때
m <- read.csv("sports.csv", header = T)
head(m)

lm(acceptance ~ ., data = m)

## (최대 최소) 정규화 시행하였을 때 결과
normalize <- function(x) { # 정규화를 위한 normalize 함수 생성
                          return((x - min(x))/(max(x) - min(x))) 
}

sports_n <- as.data.frame(lapply(m[ , c(2:5)], normalize)) # 2 ~ 5번째 컬럼 데이터를 정규화한 데이터로 변환해서 추출
head(sports_n)

lm(acceptance ~ ., data = sports_n) # 추출한 데이터로 회귀 분석하기

#### 독립변수 간의 강한 연관성을 보이는 다중공전성 문제 확인하기
## 다중회귀 분석시 종속변수와 독립변수 간의 유의미한 결과나 나오지 않을 때 확인 필요
## 독립변수 간에 강한 연관성을 보일 시 각 독립변수를 따로 분리해서 종속변수와의 연관성을 분석한다.

# 패키지 설치
# install.packages("car")
# install.packages("psych")
library(car)
library(psych)

# 데이터 불러오기 (data: test_vif2.csv)
test2 <- read.csv("c:\\data\\test_vif2.csv", fileEncoding = "euc-kr")
head(test2)

# pairs 패키지를 이용하여 종속변수와 독립변수들끼리의 상관관계 확인
pairs.panels(test2, pch = '.')

# 다중 회귀 모델을 생성합니다.
model <- lm(시험점수 ~ 아이큐 + 공부시간 + 등급평균, data = test2)
summary(model)

# 팽창계수 확인
vif(model) > 10

# 팽창게수가 10보다 큰지를 확인하였을 때 TRUE값이 나오면
# 두 독립변수 간의 연관성이 큰 것으로 간주하고 둘을 분리하여 회귀분석한다.

# 독립변수들끼리 따로 모델 새로 생성해서 회귀 분석하기
model2 <- lm(시험점수 ~ 아이큐 + 공부시간, data = test2)
summary(model2) # 0.90 결정계수

model3 <- lm(시험점수 ~ 등급평균 + 공부시간, data = test2)
summary(model3) # 0.91 결정계수
