# plotly 패키지 로드
# install.packages("plotly")
library(plotly)

# 데이터 정의
x1 <- c(7, 8, 9, 9, 10, 10, 11, 11, 12, 13)
x2 <- c(7, 9, 9, 10, 10, 10, 10, 11, 11, 13)
x3 <- c(3, 3, 6, 7, 7, 10, 10, 10, 11, 13, 30)

# x1 데이터의 박스 플롯 생성
fig1 <- plot_ly(y = ~x1, type = "box", name = "x1")

# x2 데이터의 박스 플롯 생성
fig2 <- plot_ly(y = ~x2, type = "box", name = "x2")

# x3 데이터의 박스 플롯 생성
fig3 <- plot_ly(y = ~x3, type = "box", name = "x3")

# 서브플롯으로 합치기
fig <- subplot(fig1, fig2, fig3, nrows = 1, titleX = TRUE, titleY = TRUE)

# 레이아웃 업데이트
fig <- fig %>% layout(title = "Quartile Plots of x1, x2, and x3")

# 그래프 표시
fig
