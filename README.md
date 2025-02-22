### 데이터 분석/ML/DL 도전기 👀💪 ###
*DATA/ML/DL challenge ~from a (former) motion designer~! Let's go for it!! 🚀* | 🗂️ [포트폴리오 바로가기](https://drive.google.com/file/d/1uE1UfkVBS8lrs2B1hkHzE9awkEiUAHpT/view?usp=drive_link)

---

## 프로젝트 모음 ##
### 1. 카페 창업을 위한 서울시 상권 입지 데이터분석 ☕️
- K-평균 군집분석을 활용한 서울시 카페 상권 분석 및 개업 사장님의 성향에 맞는 상권별 맞춤 입지 선정 | 📋 [PDF 바로보기](https://drive.google.com/file/d/1gEZTkoLJ_RqKsEN-mNNG49LKF7zvd6w-/view?usp=drive_link) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/tree/main/Python/Team_Project/Cafe_Commercial_Area)

### 2. 보행약자 통행 보조 시스템 개발 🧑‍🦽
- YOLO를 활용한 보행약자 통행 장애요소 객체 검출 및 보조 시스템 개발 | 📋 [PDF 바로보기](https://drive.google.com/file/d/1z32_ablLuO489azo5E76yaKwayVCcS5e/view?usp=drive_link) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/tree/main/Python/Team_Project/Walking_Object_Detection)

---

### LLM & Multimodal Model 파인튜닝 실습
1. Task: 뉴스 카테고리 분류 | 🤗 [모델 바로가기](https://huggingface.co/edgeun/roberta-base-klue-title-classification) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Finetuning_Text_Classification.ipynb)
   - Base Model: RoBERTa 기반 한국어 사전학습 모델
   - Datasets: 한국어 뉴스 본문-카테고리
   - 모델 평가: 분류 헤드 장착 후 모델 평가 (모델의 분류 결과를 test 데이터셋의 라벨과 비교 후 정확도 평가)
2. Task: 뉴스 본문 요약 | 🤗 [모델 바로가기](https://huggingface.co/edgeun/t5-small-korean-news-summarizer) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_t5_small_korean_news_summarizer.ipynb) | 🖍️ [평가 코드](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/t5_finetuned_bertscore_test.ipynb)
   - Base Model: T5-small
   - 데이터셋: 한국어 뉴스 본문-요약
   - 모델 평가: ROUGE, BERTScore
3. Task: 뉴스 본문 요약(생성) | 🤗 [모델 바로가기](https://huggingface.co/edgeun/mistral-7b-ko-news-summarizer) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_t5_small_korean_news_summarizer.ipynb)
   - Base Model: Mistral
   - 데이터셋: 한국어 뉴스 본문-요약 (대화 형식 변환)
   - 모델 평가: ROUGE, 추론 결과 검토
4. Task: AI 상담사 모델(텍스트 생성) | 🤗 [모델 바로가기](https://huggingface.co/edgeun/gemma-2-9b-it-ai-counselor) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Gemma_2_9B_it_FineTuning_AI_counselor.ipynb)
   - Base Model: Gemma 2
   - 데이터셋: 상담 대화 형식
   - 모델 평가: 챗GPT를 활용한 정성적 평가
5. Task: 한국어 질의 → SQL 생성 | 🤗 [모델 바로가기](https://huggingface.co/edgeun/yi-ko-6b-text2sql) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Finetuning_Text_Generation_Text2SQL.ipynb)
   - Base Model: Llama 기반 한/영 사전학습 모델
   - 데이터셋: 한국어 질의-SQL 쿼리문
   - 모델 평가: 챗GPT와 비교 평가
   
---

### Tableau 데이터 시각화 & 대시보드 제작 실습 ###
- 24년 서울시 공공자전거 이용 현황 | 📊 [대시보드 바로가기](https://public.tableau.com/views/01__17398849609510/1_1?:language=ko-KR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- 23년 서울시 미세먼지농도 현황과 농도 나쁨단계 이상일수 파악 | 📊 [대시보드 바로가기](https://public.tableau.com/views/02__17400408648250/1_1?:language=ko-KR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- 전국 시/도, 시/군/구별 20리터 종량제 쓰레기 봉투 가격 (24년 4월 기준) | 📊 [대시보드 바로가기](https://public.tableau.com/views/03__17400604327870/1_1?:language=ko-KR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
