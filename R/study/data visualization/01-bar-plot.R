# 작업 디렉토리 설정
setwd("c:\\data")

# plotly 패키지 로드
# install.packages("plotly")
library(plotly)

# 데이터 로드 (data: emp.csv)
setwd("c:\\data")
emp <- read.csv("emp.csv", header = T)

# 직업별 인원 수 계산
job_counts <- table(emp$job)

# 색상 목록 정의
colors <- c("gold", "skyblue", "tomato", "lightgreen", "purple")

# plotly를 사용한 막대 그래프 생성
fig <- plot_ly(x = names(job_counts), y = as.numeric(job_counts), type = 'bar',
               marker = list(color = colors))

# 그래프 출력
fig
