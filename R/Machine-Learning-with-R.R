# 교재: R을 활용한 머신러닝 | 브레트 란츠

## 데이터 관리와 이해

# R 데이터 구조 - Vector
subject_name <- c("John Doe", "Jane Doe", "Steve Graves")
temperature <- c(98.1, 98.6, 101.4)
flu_status <- c(FALSE, FALSE, TRUE)

temperature[2]  # 98.6
temperature[2:3] # 98.6 101.4
temperature[-2]  # (-): 해당 항목 제외  # 98.1 101.4
temperature[c(TRUE, TRUE, FALSE)]  # FALSE 항목 제외  # 98.1 98.6

fever <- temperature > 100
subject_name[fever]  # "Steve Graves"

subject_name[temperature > 100]  # "Steve Graves"


# Factor
gender <- factor(c("MALE", "FEMALE", "MALE"))
gender  # Levels: FEMALE MALE

blood <- factor(c("O", "AB", "A"), levels = c("A", "B", "AB", "O"))
blood  # Levels: A B AB O

symptoms <- factor(c("SEVERE", "MILD", "MODERATE"),
            levels = c("MILD", "MODERATE", "SEVERE"),
            ordered = TRUE)
symptoms  # Levels: MILD < MODERATE < SEVERE


# List
subject1 <- list(fullname=subject_name[1],
                 temperature=temperature[1],
                 flu_status=flu_status[1],
                 gender=gender[1],
                 blood=blood[1],
                 symptoms=symptoms[1])
subject1[2]  # $temperature
             # [1] 98.1

subject1[[1]]  # "John Doe"


# DataFrame
pt_data <- data.frame(subject_name, temperature,
                      flu_status, gender, blood, symptoms)
pt_data
#    subject_name temperature flu_status gender blood symptoms
# 1      John Doe        98.1      FALSE   MALE     O   SEVERE
# 2      Jane Doe        98.6      FALSE FEMALE    AB     MILD
# 3  Steve Graves       101.4       TRUE   MALE     A MODERATE

pt_data$subject_name  # "John Doe"     "Jane Doe"     "Steve Graves"

pt_data[c("temperature", "flu_status")]
#   temperature flu_status
# 1        98.1      FALSE
# 2        98.6      FALSE
# 3       101.4       TRUE

pt_data[1, 2]  # 1번째 행, 2번째 열  # 98.1

pt_data[c(1, 3), c(2, 4)]  # 1번째, 3번째 행과 2번째, 4번째 열
#   temperature gender
# 1        98.1   MALE
# 3       101.4   MALE

pt_data[ , 1] # 모든 행, 1번째 열  # "John Doe"     "Jane Doe"     "Steve Graves"

pt_data[ 1, ] # 1번째 행, 모든 열
#   subject_name temperature flu_status gender blood symptoms
# 1     John Doe        98.1      FALSE   MALE     O   SEVERE

pt_data[-2, c(-1, -3, -5, -6)]  # 2번째 행 제외, 1, 3, 5, 6번째 열 제외
#   temperature gender
# 1        98.1   MALE
# 3       101.4   MALE

pt_data$temp_c <- (pt_data$temperature - 32) * ( 5 / 9 )  # 기존 화씨 온도 데이터로 섭씨 데이터 생성
pt_data[c("temperature", "temp_c")]
#   temperature   temp_c
# 1        98.1 36.72222
# 2        98.6 37.00000
# 3       101.4 38.55556


# Matrix, Array
m <- matrix(c(1, 2, 3, 4), nrow=2)  # nrow: 행, ncol: 열
m
#      [,1] [,2]
# [1,]    1    3
# [2,]    2    4

m <- matrix(c(1, 2, 3, 4, 5, 6), nrow=2)
m
#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6

m <- matrix(c(1, 2, 3, 4, 5, 6), ncol=2)
m
#      [,1] [,2]
# [1,]    1    4
# [2,]    2    5
# [3,]    3    6

m[ , 1] # 1 2 3

ls()  # 모든 벡터 확인

rm(m, subject1)  # m과 subject1 객체 삭제

rm(list=ls())  # 모든 객체 삭제 !! 사용시 주의 !!


# 데이터 가져오기
pt_data <- read.csv("pt_data.csv", header = T)  # csv파일에서 헤더도 함께 가져오기

pt_data <- read.csv("pt_data.csv", stringsAsFactors = T)  # 범주형 데이터 팩터로 변환해서 가져오기


# 데이터 탐색
usedcars <- read.csv("/Users/dgriii0606/ml-r-4/Chapter 02/usedcars.csv", stringsAsFactors = F)
str(usedcars)

usedcars$year


# 수치 변수 탐색
summary(usedcars$year)
# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# 2000    2008    2009    2009    2010    2012 

mean(usedcars$price)  # price의 평균값: 12961.93
median(usedcars$price)  # price의 중앙값(2분위수): 13591.5
range(usedcars$price)  # 최댓값과 최솟값: 3800 21992
diff(range(usedcars$price))  # 최댓값과 최솟값의 차이: 18192

quantile(usedcars$price)  # 최소값, 1분위수, 2분위수(중앙값), 3분위수, 최댓값
#     0%     25%     50%     75%    100% 
# 3800.0 10995.0 13591.5 14904.5 21992.0 

IQR(usedcars$price)  # 3분위수와 1분위수의 차이: 3909.5

quantile(usedcars$price, seq(from=0, to=1, by=0.20))  # 0부터 1까지 20%의 간격으로(=5분위수)
#       0%     20%     40%     60%     80%    100% 
#   3800.0 10759.4 12993.8 13992.0 14999.0 21992.0


# 수치 변수 시각화 - 박스 플롯
boxplot(usedcars$price, main="Boxplot of Used Car Prices", ylab="price ($)", col='lightcoral')

# 수치 변수 시각화 - 히스토그램
hist(usedcars$price, main="Histogram of Used Car Prices", xlab="price ($)")


# 분산과 표준편차
var(usedcars$price)  # 9749892
sd(usedcars$price)  # 3122.482


# 범주형 데이터 탐색
table(usedcars$model)
#  SE SEL SES 
#  78  23  49 

model_table <- table(usedcars$model)
prop.table(model_table)  # 비율 계산
#        SE       SEL       SES 
# 0.5200000 0.1533333 0.3266667 


# 관계 시각화 - 산포도 그래프
plot(x = usedcars$mileage, y = usedcars$price,
     main = "Scatterplot of Price vs. Mileage",
     xlab = "Used Car Odometer (mi.)",
     ylab = "Used Car Price ($)")


# 이원 교차표
install.packages("gmodels")  # 패키지 설치
library(gmodels)  # 패키지 로드

unique(usedcars$model)  # "SEL" "SE"  "SES"
unique(usedcars$color)  # "Yellow" "Gray"   "Silver" "White"  "Blue"   "Black"  "Green"  "Red"    "Gold"

usedcars$conservative <- usedcars$color %in% c("Black", "Gray", "Silver", "White")
table(usedcars$conservative)
# FALSE  TRUE 
#    51    99 

CrossTable(usedcars$model, usedcars$conservative)


# 피어슨 카이제곱 검정 - 범주형 데이터의 독립성 검정
pchisq(0.154, df=2, lower.tail = FALSE)
# 0.154: 카이제곱 검정 통계량(기여도의 합), df: 자유도, Lower.tail: 꼬리 확률
# 0.9258899: 100%에 가까울 수록 연관이 없다. <-> 반대는 연관이 크다.(우연이 아니다, p-value가 작다.)

# CrossTable() 호출시 카이제곱 검정 결과 바로 출력
CrossTable( x=usedcars$model, y=usedcars$conservative, chisq=TRUE )
# Pearson's Chi-squared test 
# ------------------------------------------------------------
# Chi^2 =  0.1539564     d.f. =  2     p =  0.92591


##### Chapter 3: 최근접 이웃(k-NN) 방법을 활용한 분류

## 예제: 유방암 샘플 분류하기

wbcd <- read.csv("/Users/dgriii0606/ml-r-4/Chapter 03/wisc_bc_data.csv")
wbcd

# ID 컬럼 삭제
wbcd <- wbcd[-1]
wbcd

# 종속변수 확인 및 팩터화
table(wbcd$diagnosis)
#   B   M 
# 357 212
wbcd$diagnosis <- factor(wbcd$diagnosis, levels = c("B", "M"),
                         labels = c("Benign", "Malignant"))
# 종속변수 비율 확인
round(prop.table(table(wbcd$diagnosis)) * 100, digits = 1)
# Benign Malignant 
#   62.7      37.3 

# 특정 데이터 살펴보기
summary(wbcd[c("radius_mean", "area_mean", "smoothness_mean")])

# 수치 데이터 정규화(0~1 사이값으로 변경)
normalize <- function(x) {
  return ((x - min(x)) / (max(x) - min(x)))
}

wbcd_n <- as.data.frame(lapply(wbcd[2:31], normalize))

summary(wbcd_n$area_mean)
#    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# 0.0000  0.1174  0.1729  0.2169  0.2711  1.0000

# 훈련, 테스트 데이터 셋 생성
wbcd_train <- wbcd_n[1:469, ]
wbcd_test <- wbcd_n[470:569, ]

# 훈련과 테스트의 정답(종속변수) 데이터 셋 생성
wbcd_train_labels <- wbcd[1:469, 1]
wbcd_test_labels <- wbcd[470:569, 1]

# 생성한 데이터로 모델 훈련하기

# 필요한 패키지 설치 및 실행
install.packages("class")
library(class)
wbcd_test_pred = knn(train=wbcd_train, test=wbcd_test, cl=wbcd_train_labels, k=3)  # k: 최근접 이웃의 갯수

# 모델 성능 평가
library(gmodels)
CrossTable(x=wbcd_test_labels, y=wbcd_test_pred, prop.chisq=FALSE)
#                    | wbcd_test_pred
#   wbcd_test_labels |    Benign | Malignant | Row Total |   # 여기서 유심있게 봐야하는 것(=positive): 악성종양(Malignant)
#   -----------------|-----------|-----------|-----------|
#             Benign |    60(TN) |     1(FP) |        61 |   # 우측 상단(1)이 거짓긍정(FP): 틀렸다 ~ (무엇으로?) positive(유의한 결과로=악성종양으로)
#                    |     0.984 |     0.016 |     0.610 |   # => TN/(TN+FP): 특이도(Specificity)
#                    |     0.968 |     0.026 |           |   # 1 - 특이도(Specificity)는 거짓긍정률(FPR): FP/(FP+TN)
#                    |     0.600 |     0.010 |           | 
#   -----------------|-----------|-----------|-----------|
#          Malignant |     2(FN) |    37(TP) |        39 |   # 좌측 하단(2)이 거짓부정(FN): 틀렸다 ~ (실제 유의한 결과를) 유의하지 않은 결과로(negative)
#                    |     0.051 |     0.949 |     0.390 |   # => TP/(TP+FN): 민감도(Sensitivity), 재현율(Recall), 참긍정률(TPR)
#                    |     0.032 |     0.974 |           | 
#                    |     0.020 |     0.370 |           | 
#   -----------------|-----------|-----------|-----------|
#       Column Total |        62 |        38 |       100 | 
#                    |     0.620 |     0.380 |           | 
#   -----------------|-----------|-----------|-----------|
#                                | TP/(TP+FP)               # (TP+TN)/(TP+TN+FP+FN): 정확도(Accuracy)
#                                | 정밀도(Precision)

# 모델 성능 개선하기
# z - 표준화 하기
wbcd_z <- as.data.frame(scale(wbcd[-1]))

summary(wbcd_z$area_mean)
# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# -1.4532 -0.6666 -0.2949  0.0000  0.3632  5.2459

# 표준화한 데이터로 다시 학습시키기
wbcd_train <- wbcd_z[1:469, ]
wbcd_test <- wbcd_z[470:569, ]

wbcd_test_pred = knn(train=wbcd_train, test=wbcd_test, cl=wbcd_train_labels, k=3)

# 다시 성능 지표 확인
CrossTable(x=wbcd_test_labels, y=wbcd_test_pred, prop.chisq=FALSE)  # 성능이 더 안좋아짐

# k 의 대체 값 테스트 (반복문으로 k값 넣기)
k_values <- c(1, 5, 11, 15, 21, 27)  # k 값 후보 선정

for (k_val in k_values) {
  wbcd_test_pred <- knn(train=wbcd_train,
                        test=wbcd_test,
                        cl=wbcd_train_labels,
                        k=k_val)
  CrossTable(x = wbcd_test_labels,
             y = wbcd_test_pred,
             prop.chisq = FALSE)
}


##### Chapter 4: 나이브베이즈를 활용한 확률적 학습 분류

## 예제: 스팸 메일 필터링

# 데이터 불러오기
sms_raw <- read.csv("/Users/dgriii0606/ml-r-4/Chapter 04/sms_spam.csv")

str(sms_raw)

sms_raw$type <- factor(sms_raw$type)

str(sms_raw$type)
table(sms_raw$type)
# ham spam 
# 4812  747 

# tm 패키지로 코퍼스(분석을 위한 말뭉치) 구축
library(tm)
sms_corpus <- VCorpus(VectorSource(sms_raw$text))

print(sms_corpus)
inspect(sms_corpus[1:2])

as.character(sms_corpus[[1]])
lapply(sms_corpus[1:2], as.character)

# 텍스트 마이닝 매핑 함수로 클린 버전 만들기
sms_corpus_clean <- tm_map(sms_corpus, content_transformer(tolower))  # 대문자를 소문자로 변환해서 매핑함수로 clean에 담기

# 원본 데이터와 비교
as.character(sms_corpus[[1]])
as.character(sms_corpus_clean[[1]])

# 클린본에서 숫자, 불용어, 구두점 제거
sms_corpus_clean <- tm_map(sms_corpus_clean, removeNumbers)
sms_corpus_clean <- tm_map(sms_corpus_clean, removeWords, stopwords())
sms_corpus_clean <- tm_map(sms_corpus_clean, removePunctuation)

# 동일한 어근 추출
library(SnowballC)
wordStem(c("learn", "learned", "learning", "learns"))  # 사용예시: 모두 learn으로 변경

sms_corpus_clean <- tm_map(sms_corpus_clean, stemDocument)

sms_corpus_clean <- tm_map(sms_corpus_clean, stripWhitespace) # eliminate unneeded whitespace

# 최종 정제한 클린본 비교
lapply(sms_corpus[1:3], as.character)
lapply(sms_corpus_clean[1:3], as.character)

# 클린본 텍스트 문서를 토큰화하기 (DTM: 문서-용어 희소행렬 생성)
sms_dtm <- DocumentTermMatrix(sms_corpus_clean)

# 위의 과정을 거치지 않고 바로 토큰화 진행하면서 문서 데이터 정제하기
sms_dtm2 <- DocumentTermMatrix(sms_corpus, control = list(  # 원본 데이터(sms_corpus) 불러와서 정제 후 토큰화
  tolower = TRUE,
  removeNumbers = TRUE,
  stopwords = TRUE,
  removePunctuation = TRUE,
  stemming = TRUE
))

# 불용어 제거에 함수 적용 버전 (직전 위에와 결과가 달라지므로 함수로 제거하는 방법을 적용해 위 과정을 거친 결과와 동일하게 만들 수 있음)
sms_dtm3 <- DocumentTermMatrix(sms_corpus, control = list(
  tolower = TRUE,
  removeNumbers = TRUE,
  stopwords = function(x) { removeWords(x, stopwords()) },
  removePunctuation = TRUE,
  stemming = TRUE
))

# 결과 비교
sms_dtm
sms_dtm2
sms_dtm3

# trian, test 분리
sms_dtm_train <- sms_dtm[1:4169, ]
sms_dtm_test  <- sms_dtm[4170:5559, ]

# 종속변수 담기
sms_train_labels <- sms_raw[1:4169, ]$type
sms_test_labels  <- sms_raw[4170:5559, ]$type

# 종속변수 비율 확인
prop.table(table(sms_train_labels))
prop.table(table(sms_test_labels))

# 워드 클라우드로 클린본 텍스트 데이터 시각화
library(wordcloud)
wordcloud(sms_corpus_clean, min.freq = 50, random.order = FALSE)

# subset 함수로 훈련데이터에서 spam, ham 나누기
spam <- subset(sms_raw, type == "spam")
ham  <- subset(sms_raw, type == "ham")

wordcloud(spam$text, max.words = 40, scale = c(3, 0.5))
wordcloud(ham$text, max.words = 40, scale = c(3, 0.5))

# 최소 5번 이상 언급되는 단어 찾기
findFreqTerms(sms_dtm_train, 5)

# 5번 이상 등장한 단어들만 담기
sms_freq_words <- findFreqTerms(sms_dtm_train, 5)
str(sms_freq_words)

# 자주 등장한 단어 모음으로 훈련, 테스트 담기
sms_dtm_freq_train <- sms_dtm_train[ , sms_freq_words]
sms_dtm_freq_test <- sms_dtm_test[ , sms_freq_words]

# 카운트 숫자를 팩터로 변환
convert_counts <- function(x) {
  x <- ifelse(x > 0, "Yes", "No")  # x가 0보다 크면 "Yes"로 변환하고 그렇지 않으면 "No"로 변환해라
}

# 위에서 생성한 함수를 apply 함수로 train, test 데이터에 적용
sms_train <- apply(sms_dtm_freq_train, MARGIN = 2, convert_counts)  # MARGIN = 2: 열, 1은 행
sms_test  <- apply(sms_dtm_freq_test, MARGIN = 2, convert_counts)

## 모델 학습하기
library(naivebayes)
sms_classifier <- naive_bayes(sms_train, sms_train_labels)  # 라플라스 추정값을 안 넣었을 경우 50개 이상 경고 뜸

## 모델 평가하기
sms_test_pred <- predict(sms_classifier, sms_test)

library(gmodels)
CrossTable(sms_test_pred, sms_test_labels,
           prop.chisq = FALSE, prop.c = FALSE, prop.r = FALSE,
           dnn = c('predicted', 'actual'))

## 모델 성능 개선 - 라플라스 수치 넣기
sms_classifier2 <- naive_bayes(sms_train, sms_train_labels, laplace = 1)
sms_test_pred2 <- predict(sms_classifier2, sms_test)
CrossTable(sms_test_pred2, sms_test_labels,
           prop.chisq = FALSE, prop.c = FALSE, prop.r = FALSE,
           dnn = c('predicted', 'actual'))
