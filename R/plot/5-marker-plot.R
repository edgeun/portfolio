# plotly 패키지 로드
# install.packages("plotly")
library(plotly)

# 데이터 로드 (data: usedcars.csv)
car <- read.csv("c:\\data\\usedcars.csv", header = TRUE)
car

# 산점도 생성
fig <- plot_ly(data = car, 
               x = ~mileage, 
               y = ~price, 
               type = 'scatter', 
               mode = 'markers', 
               marker = list(color = 'blue')) 

# 추세선 추가
fig <- fig %>% add_trace(x = car$mileage, 
                         y = fitted(lm(price ~ mileage, data = car)), 
                         type = 'scatter', 
                         mode = 'lines', 
                         line = list(color = 'red'), 
                         name = 'Trend Line')

# 그래프 출력
fig

# 상관계수값 출력
cor <- cor(car$mileage, car$price)
cor
