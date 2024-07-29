# 작업 디렉토리 설정
setwd("c:\\data")

# plotly 패키지 로드
# install.packages("plotly")
library(plotly)

# 데이터 로드 (data: usedcars.csv)
cars <- read.csv("usedcars.csv", header = T)

# 모델별 인원 수 계산
car_counts <- table(cars$model)

# 색상 목록 정의
colors <- c("gold", "skyblue", "tomato", "lightgreen", "purple")

# plotly를 사용한 원형 그래프 생성
fig <- plot_ly(labels = names(car_counts),
               values = as.numeric(car_counts),
               type = 'pie',
               marker = list(colors = colors))
               
fig
