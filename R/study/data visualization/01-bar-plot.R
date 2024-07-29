setwd("c:\\data") # 작업 디렉토리 설정

# install.packages("plotly")
library(plotly)

#### 01. 막대 그래프

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


#### 02. 원 그래프

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


#### 03. 라인 그래프

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


#### 04. 히스토그램 그래프

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


#### 05. 산포도 그래프

# 데이터 로드
car <- read.csv("usedcars.csv", header = TRUE)
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


#### 06. 산포도 그래프

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


#### 07. 워드클라우드 그래프

# 라이브러리 로드
library(wordcloud2) 
library(RColorBrewer)
library(plyr) # 데이터 조작을 위한 패키지
library(data.table)

# 텍스트 데이터 로드
txt <- readLines('ladybug5.txt', encoding = "UTF-8")

# 불필요한 텍스트 제거
cleaned_txt <- iconv(txt, "UTF-8", "UTF-8", sub="")
cleaned_txt <- gsub("[^[:alnum:][:space:]ㄱ-ㅎㅏ-ㅣ가-힣]", " ", cleaned_txt) # 특수문자 제거 및 공백 처리
cleaned_txt <- gsub("\\s+", " ", cleaned_txt) # 특수문자 제거 및 공백 처리

# 명사 추출 함수
extract_nouns_simple <- function(doc) {
  doc <- as.character(doc)
  words <- unlist(strsplit(doc, "\\s+"))  # 공백을 기준으로 단어 분리
  nouns <- Filter(function(x) {grepl("^[가-힣]+$", x) && nchar(x) >= 2}, words)  # 한글로만 구성된 단어 추출 및 길이 2 이상 필터링
  return(nouns)
}

# 명사 추출
nouns <- extract_nouns_simple(cleaned_txt)

# 추출된 명사 확인
print(head(nouns, 10))  # 상위 10개 단어 확인

# 단어 빈도수 계산
word_freq <- table(nouns)
word_freq <- as.data.frame(word_freq, stringsAsFactors = FALSE)
word_freq <- arrange(word_freq, desc(Freq)) # 명사의 빈도수를 내림차순으로 정렬

# 상위 10개 단어 확인
print(head(word_freq, 10))

# 유효하지 않은 값 확인 및 제거
# 빈 문자열을 포함하는 행 제거
word_freq <- word_freq[word_freq$nouns != "", ]

# 특정 단어 제외하기
word_freq <- subset(word_freq, nouns != "너무")

# 단어 빈도수 데이터프레임 확인
print(head(word_freq, 10))

# 워드클라우드 생성 (하트 모양)
fig <- wordcloud2(data = word_freq, shape = "heart", color = brewer.pal(8, "Dark2"))

fig
