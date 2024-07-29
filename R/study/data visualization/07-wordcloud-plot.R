# 라이브러리 로드
# install.packages("wordcloud2")
# install.packages("RColorBrewer")
# install.packages("plyrr")
# install.packages("data.table")

library(wordcloud2) 
library(RColorBrewer)
library(plyr) # 데이터 조작을 위한 패키지
library(data.table)

# 텍스트 데이터 로드 (data: ladybug5.txt)
txt <- readLines("c:\\data\\ladybug5.txt", encoding = "UTF-8")

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
