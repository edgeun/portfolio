# 작업 디렉토리 설정
setwd("c:\\data")

# 데이터 불러오기 
usedcars <- read.csv("usedcars.csv", header=T)
mileage <- usedcars$mileage

# 평균값, 중앙값, 최빈값 계산 함수
calculate_stats <- function(data) {
  mean_value <- mean(data)
  median_value <- median(data)
  mode_value <- density(data)$x[which.max(density(data)$y)]
  return(list(mean = mean_value, median = median_value, mode = mode_value))
}

# 통계량 계산
mileage_stats <- calculate_stats(mileage)

# 대칭분포 그래프 그리기
hist(mileage, breaks=30, col="grey", border="white", prob=TRUE, main="대칭분포", xlab="값", ylab="밀도")
lines(density(mileage), col="red")  # 확률 밀도 함수 그래프
abline(v=mileage_stats$mean, col="blue", lwd=2, lty=2)   # 평균값
abline(v=mileage_stats$median, col="green", lwd=2, lty=2) # 중앙값
abline(v=mileage_stats$mode, col="purple", lwd=2, lty=2)  # 최빈값
