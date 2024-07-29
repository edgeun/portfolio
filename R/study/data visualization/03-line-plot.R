# plotly 패키지 로드
library(plotly)

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


