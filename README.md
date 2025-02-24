### 데이터 분석/ML/DL 도전기 👀💪 ###
*DATA/ML/DL challenge ~from a (former) motion designer~! Let's go for it!! 🚀* | 🗂️ [포트폴리오 바로가기](https://drive.google.com/file/d/1uE1UfkVBS8lrs2B1hkHzE9awkEiUAHpT/view?usp=drive_link)

---

## 프로젝트 모음 ##
### 1. 카페 창업을 위한 서울시 상권 입지 데이터분석 ☕️
- K-평균 군집분석을 활용한 서울시 카페 상권 분석 및 개업 사장님의 성향에 맞는 상권별 맞춤 입지 선정 | 📋 [PDF 바로보기](https://drive.google.com/file/d/1gEZTkoLJ_RqKsEN-mNNG49LKF7zvd6w-/view?usp=drive_link) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/tree/main/Python/Team_Project/Cafe_Commercial_Area)
- 프로젝트 배경
  - 상대적으로 임대료가 저렴한 커피점 창업은, 창업을 희망하는 2030 세대의 접근이 용이하나 과도한 경쟁으로 인해, 보편화된 분석 기준을 넘어 개개인의 성향과 특성을 살린 맞춤형 입지 선정이 필요해 보임
  - 종합적 응용 분석을 통해 예비 카페 사장님들의 영업 방향성과 타겟 고객층을 고려한 입지 추천 목표

- 사용 데이터
  - '서울시 성권분석서비스'에서 제공하는 서울시 상권 데이터 및 상업용 부동산 임대료 데이터 사용 

- 분석 개요
  - K-클러스터링을 위한 데이터 전처리 및 파생변수 생성
  - K-Means++ 알고리즘을 활용한 K-클러스터링 실시
  - 약 1,600개의 서울 상권을 크게 4개의 상권 그룹으로 세그멘테이션화 하고 표준화 작업을 통해 군집 간 특징 추출
  - 군집 간 특징을 토대로 군집 내 상권 세부 EDA 분석 및 시각화
  - 상권 군집 그룹의 특성을 살린 명칭을 지정하여, 개업 사장님의 성향의 맞는 상권 그룹 추천 및 매칭
  - 매칭 된 상권 그룹에 속한 서울 상권 명을 지도 시각화를 통해 안내 및 제공

- 분석 한계점
  - 군집 간 특색이 더 드러날 수 있도록 면밀한 K값 조정 필요
  - 제한적인 기산 데이터 활용, 추적으로 시계열 데이터를 활용하여 매출 추이등 추가 세밀 분석이 가능할 것으로 예상

### 2. 보행약자 통행 보조 시스템 개발 🧑‍🦽
- YOLO를 활용한 보행약자 통행 장애요소 객체 검출 및 보조 시스템 개발 | 📋 [PDF 바로보기](https://drive.google.com/file/d/1z32_ablLuO489azo5E76yaKwayVCcS5e/view?usp=drive_link) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/tree/main/Python/Team_Project/Walking_Object_Detection)


---

### LLM & Multimodal Model 파인튜닝 실습
1. Task: 뉴스 카테고리 분류(Text Classification) | 🤗 [모델 바로가기](https://huggingface.co/edgeun/roberta-base-klue-title-classification) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Finetuning_Text_Classification.ipynb)
   - Base Model: RoBERTa 기반 한국어 사전학습 모델
   - Datasets: 한국어 뉴스 본문-카테고리
   - 모델 평가: 분류 헤드 장착 후 모델 평가 (모델의 분류 결과를 test 데이터셋의 라벨과 비교 후 정확도 평가)
2. Task: 뉴스 본문 요약(Seq2Seq Generation) | 🤗 [모델 바로가기](https://huggingface.co/edgeun/t5-small-korean-news-summarizer) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_t5_small_korean_news_summarizer.ipynb) | 🖍️ [평가 코드](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/t5_finetuned_bertscore_test.ipynb)
   - Base Model: T5-small 기반의 한국어 사전학습 모델
   - 데이터셋: 한국어 뉴스 본문-요약
   - 모델 평가: ROUGE, BERTScore
3. Task: 뉴스 본문 요약(Text Generation) | 🤗 [모델 바로가기](https://huggingface.co/edgeun/mistral-7b-instruct-v0.1-korean-news-summarizer) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Mistral_7B_Instruct_v0_1_Finetuning_Korean_News_summarizer.ipynb)
   - Base Model: Mistral-7B-Insruct-v0.1 인스트럭션 튜닝 모델
   - 데이터셋: 한국어 뉴스 본문-요약 (대화 형식 변환)
   - 모델 평가: ROUGE, 추론 결과 검토
4. Task: AI 상담사 모델(Text Generation) | 🤗 [모델 바로가기](https://huggingface.co/edgeun/gemma-2-9b-it-ai-counselor) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Gemma_2_9B_it_FineTuning_AI_counselor.ipynb)
   - Base Model: Gemma-2-9B-it 인스트럭션 튜닝 모델
   - 데이터셋: 상담 대화 형식
   - 모델 평가: 챗GPT를 활용한 정성적 평가
5. Task: 한국어 질의 → SQL 생성(Text Generation) | 🤗 [모델 바로가기](https://huggingface.co/edgeun/yi-ko-6b-text2sql) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Finetuning_Text_Generation_Text2SQL.ipynb)
   - Base Model: Llama-2 기반 한/영 혼합 사전학습 모델
   - 데이터셋: 한국어 질의-SQL 쿼리문
   - 모델 평가: 챗GPT와 비교 평가
   
---

### Tableau 데이터 시각화 & 대시보드 제작 실습 ###
- 24년 서울시 공공자전거 이용 현황 | 📊 [대시보드 바로가기](https://public.tableau.com/views/01__17398849609510/1_1?:language=ko-KR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- 23년 서울시 미세먼지농도 현황과 농도 나쁨단계 이상일수 파악 | 📊 [대시보드 바로가기](https://public.tableau.com/views/02__17400408648250/1_1?:language=ko-KR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- 전국 시/도, 시/군/구별 20리터 종량제 쓰레기 봉투 가격 (24년 4월 기준) | 📊 [대시보드 바로가기](https://public.tableau.com/views/03__17400604327870/1_1?:language=ko-KR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
