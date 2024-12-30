# 교재: R을 활용한 머신러닝 | 브레트 란츠

## 데이터 관리와 이해

# R 데이터 구조  # Vector
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
