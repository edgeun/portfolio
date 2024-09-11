# 패키지 설치
# install.packages("svDialogs")

# 패키지 불러오기
library(svDialogs)
library(plotly)

# 옵션 메시지 정의
options_list <- list("01: 막대 그래프 코드",
                     "02: 원형 그래프 코드",
                     "03: 라인 그래프 코드",
                     "04: 히스토그램 그래프 코드",
                     "05: 산포도 그래프 코드",
                     "06: 박스 플롯 그래프 코드",
                     "07: 워드클라우드 그래프 코드",
                     "08: PCA 주성분 분석 코드",
                     "09: pairs 상관관계 분석 코드")

# 사용자 입력 받기 (대화 상자 사용)
dialog_result <- dlgList(options_list, title = "번호를 선택하세요")$res

# switch 문을 사용해서 선택에 따라 다른 메세지 출력 및 실행
if (is.null(dialog_result)) {
  cat("유효하지 않은 선택입니다.\n")
} else {
  num <- as.integer(substr(dialog_result, 1, 2)) # 선택한 옵션의 1~2번째 글자를 숫자로 변환
  fig <- switch(as.character(num),
         "1" = {
           cat(readLines("bar_plot.R"), sep = "\n")
           source("bar_plot.R", local = TRUE)
           fig  # bar_plot.R에서 생성된 fig 객체 반환
         },
         "2" = {
           cat(readLines("pie_plot.R"), sep = "\n")
           source("pie_plot.R", local = TRUE)
           fig  # pie_plot.R에서 생성된 fig 객체 반환
         },
         "3" = {
           cat(readLines("line_plot.R"), sep = "\n")
           source("line_plot.R", local = TRUE)
           fig  # line_plot.R에서 생성된 fig 객체 반환
         },
         "4" = {
           cat(readLines("hist_plot.R"), sep = "\n")
           source("hist_plot.R", local = TRUE)
           fig  # hist_plot.R에서 생성된 fig 객체 반환
         },
         "5" = {
           cat(readLines("marker_plot.R"), sep = "\n")
           source("marker_plot.R", local = TRUE)
           fig  # marker_plot.R에서 생성된 fig 객체 반환
         },
         "6" = {
           cat(readLines("box_plot.R"), sep = "\n")
           source("box_plot.R", local = TRUE)
           fig  # box_plot.R에서 생성된 fig 객체 반환
         },
         "7" = {
           cat(readLines("wcloud_plot.R"), sep = "\n")
           source("wcloud_plot.R", local = TRUE)
           fig  # wcloud_plot.R에서 생성된 fig 객체 반환
         },
         "8" = {
           cat(readLines("pca.R"), sep = "\n")
           source("pca.R", local = TRUE)
         },
         "9" = {
           cat(readLines("pairscorr.R"), sep = "\n")
           source("pairscorr.R", local = TRUE)
         },
         {
           cat("유효하지 않은 선택입니다.\n")
           NULL
         }
  )
  if (!is.null(fig)) {
    print(fig)  # fig 객체를 명시적으로 출력
  }
}
