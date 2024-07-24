# 필요한 패키지 설치 및 로드
if (!require("readr")) install.packages("readr")
if (!require("dplyr")) install.packages("dplyr")
if (!require("caret")) install.packages("caret")
if (!require("class")) install.packages("class")
if (!require("plotly")) install.packages("plotly")

library(readr)
library(dplyr)
library(caret)
library(class)
library(plotly)

# 1단계: 데이터 수집
wbcd <- read.csv("c:\\data\\wisc_bc_data.csv", stringsAsFactors = TRUE) # 범주형 데이터 팩터로 변환해서 불러오기
nrow(wbcd) # 569
ncol(wbcd) # 32

# 2단계: 데이터 탐색
# 1. 결측치 확인
colSums(is.na(wbcd))

# 2. 종속변수의 데이터 비율
table(wbcd$diagnosis)
prop.table(table(wbcd$diagnosis))

# 3. 데이터 스케일링 (최대 최소 정규화)
wbcd2 <- wbcd[ , c(-1, -2)] # 정규화 불필요 독립변수(id)와 종속변수(diagnosis)를 제외
normalize <- function(x) {return((x - min(x)) / (max(x) - min(x)))} # 최대 최소 정규화 함수 생성
wbcd_n <- as.data.frame(lapply(wbcd2, normalize)) # 독립변수를 정규화하여 추출
summary(wbcd_n)

# 3단계: 모델 훈련
# 훈련 데이터와 테스트 데이터를 분리합니다. 90% 학습, 10% 시험
set.seed(1)
k <- createDataPartition(wbcd$diagnosis, p = 0.9, list = FALSE)

# 기계를 학습 시킬 훈련 데이터와 테스트 데이터 생성
wbcd_train <- wbcd_n[k, ]
wbcd_test <- wbcd_n[-k, ]
nrow(wbcd_train)  # 513
nrow(wbcd_test)   # 56 

# 기계를 학습 시킬 훈련 데이터의 정답과 테스트 데이터의 정답 생성
wbcd_train_label <- wbcd$diagnosis[k]
wbcd_test_label <- wbcd$diagnosis[-k]
length(wbcd_train_label)  # 513
length(wbcd_test_label)   # 56

# 4단계: 모델 성능 평가 (for loop 문을 실행해서 정확도가 높게 나오는 k값 구하기)
accuracies <- data.frame(k = integer(), accuracy = numeric())

set.seed(10)
for (i in seq(1, 29, 2)) {
  result1 <- knn(train = wbcd_train, test = wbcd_test, cl = wbcd_train_label, k = i)
  accuracy <- sum(result1 == wbcd_test_label) / length(wbcd_test_label) * 100
  accuracies <- rbind(accuracies, data.frame(k = i, accuracy = accuracy))
  print(paste(i, '개 일때 정확도 ', accuracy))
}

# 정확도 데이터 프레임 확인
accuracies

# plotly로 k값에 대한 정확도 라인 그래프 출력
fig <- plot_ly(accuracies, x = ~k, y = ~accuracy, type = 'scatter', mode = 'lines+markers', line = list(color = 'red'))
fig <- fig %>% layout(title = "K 값에 따른 정확도",
                      xaxis = list(title = "K 값"),
                      yaxis = list(title = "정확도"))
fig
