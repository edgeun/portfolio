# 교재: R을 활용한 머신러닝 | 브레트 란츠

## 데이터 관리와 이해

# R 데이터 구조  # Vector
subject_name <- c("John Doe", "Jane Doe", "Steve Graves")
temperature <- c(98.1, 98.6, 101.4)
flu_status <- c(FALSE, FALSE, TRUE)

temperature[2]  # 98.6
temperature[2:3] # 98.6 101.4
temperature[-2]  # (-): 해당번째 항목 제외  # 98.1 101.4
temperature[c(TRUE, TRUE, FALSE)]  # FALSE 항목 제외  # 98.1 98.6

fever <- temperature > 100
subject_name[fever]  # "Steve Graves"

subject_name[temperature > 100]  # "Steve Graves"


# Factor
gender <- factor(c("MALE", "FEMALE", "MALE"))
gender  # Levels: FEMALE MALE

blood <- factor(c("O", "AB", "A"), levels = c("A", "B", "AB", "O"))
blood  # Levels: A B AB O
