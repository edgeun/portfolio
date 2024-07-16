setwd("c:\\data") # 작업 디렉토리 설정

# install.packages("plotly")
library(plotly)

## 01. 막대 그래프

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

## 02. 원 그래프

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

## 03. 라인 그래프

# 데이터 로드 (data: 2호선_강남역_시간대별_승하차현황_수정2.csv)
data <- read.csv("2호선_강남역_시간대별_승하차현황_수정2.csv", header = TRUE, fileEncoding = "euc-kr")
data

# plotly를 사용한 라인 그래프 생성 (승차 수 라인 + 하차 수 라인 추가)
fig <- plot_ly(data, x = ~time) %>%
       add_trace(  y = ~in_cnt,
                name = '승차',
                type = 'scatter',
                mode = 'lines+markers',
                line = list(color = 'blue')) %>% # 승차 수 라인 생성
       add_trace(  y = ~out_cnt,
                name = '하차',
                type = 'scatter',
                mode = 'lines+markers',
                line = list(color = 'red')) # 하차 수 라인 생성

# 그래프 출력
fig

## 04. 
