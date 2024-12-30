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
