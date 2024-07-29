# 필요한 패키지 설치 및 로드
# install.packages("ggplot2")
# install.packages("plotly")

library(ggplot2)
library(plotly)

# 아이리스 데이터셋 로드
iris_data <- read.csv("c:\\data\\iris2.csv")

# 주성분 분석 수행
pca_result <- prcomp(iris_data[ ,1:4], scale. = TRUE)
# prcomp는 주성분 분석하는 함수이고 scale. = TRUE는 데이터를 표준화하여 분석해라 (평균 0, 분산 1로 조정)
# pra_result를 출력해보면 주성분(PC1, PC2, PC3, PC4)과 원래 변수(Sepal.lenth, ~ , Petal.width)와 얼마나 관련이 있는지를 나타내는 결과임
# 각 값들이 해당 주성분과 원래 변수 간의 상관계수를 나타냄을 의미

# 주성분 점수 추출
pca_scores <- data.frame(pca_result$x)
# 각 데이터 포인트가 주성분 공간에서 어디에 위치하는지를 설명한 것인데 이 pca
pca_scores$Species <- iris_data$Species

# 2차원 시각화
p <- ggplot(pca_scores, aes(x = PC1, y = PC2, color = Species)) +
  geom_point(size = 3) +
  labs(title = "PCA 결과", x = "PC1", y = "PC2") +
  theme_minimal()

# plotly를 사용한 인터랙티브 시각화
p_interactive <- ggplotly(p)

# 시각화 출력
p_interactive
