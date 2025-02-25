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
- 프로젝트 배경
  - 시각장애인 분들을 포함한 보행 약자의 원할한 통행을 방해하는 여러 장애 요소들이 보행로에 산재
  - 이러한 요인을 해소하기 위해 다양한 공공 보조 수단이 존재하지만, 통행 약자의 개인별 상황을 고려한 개인 보조 장치가 필요해 보임.

- 사용 데이터
  - 'AI Hub'에서 제공하는 인도보행 영상 시퀀스 이미지와 신호등, 킥보드 이미지를 웹크롤링하여 수집

- 실습 개요
  - 바운딩 박스로 라벨링된 이미지 데이터를 제한된 실습 환경을 고려하여 임의로 1000개의 데이터를 선정하여 9:1의 train / valid 데이터로 Yolov8 모델 파인튜닝
  - 모델 학습 규격에 맞도록 제공받은 xml 형식의 라벨 정보 데이터를 파싱 후 학습용 txt 파일 및 학습 정보를 제공할 yaml 파일 생성
  - 학습 후 모델 평가 실시, 'AI Hub' 데이터로 미세 조정 결과 0.9 이상의 높은 검출 신뢰도와 mAP50 기준 0.4~0.5의 수치를 보였음. 하지만 별도의 추가 객체 검출을 위해 크롤링한 데이터를 포함하여 미세 조정하였을 때 성능이 떨어지는 현상을 보임.
  - 검출된 객체의 사용자 접근 거리별 영역 색상 분리(초록 -> 노랑 -> 빨강(최근접 경고) -> 노랑 -> 초록) 처리 및 신호등 색상 구분을 위해 OpenCV를 활용하여 입력한 영상 데이터를 처리하고 관련 PNG 이미지를 영상에 입히는 작업을 진행
  - Google TTS를 활용하며 검출된 객체의 라벨을 인식해 텍스트 및 오디오 출력

- 실습 한계점
  - 기능 구현 결과 영역별(관심영역 접근별) 민감한 색상 구분과 변화를 보였으나 음성의 출력 속도와 텍스트 길이 등의 이슈로 인해 싱크가 잘 맞지 않았음. (빨간 영역에 닿은 객체만 우선적으로 음성으로 알려주거나 보행 인지를 고려해 몇초간 우선적으로 알려주는 등의 해결을 시도)
  - 크롤링 후 라벨링하여 학습 시킨 신호등과 킥보드의 검출력이 다소 떨어졌음.
  - 녹화본 데모 영상 위주로 실습을 테스트 해보았으나 실사용에 있어 실시간 영상 속 객체를 검출해내는 성능이 필요해 보임.

---

### LLM & Multimodal Model 파인튜닝 실습
1. RoBERTa 계열 모델을 활용한 뉴스 카테고리 분류 | 🤗 [모델 바로가기](https://huggingface.co/edgeun/roberta-base-klue-title-classification) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Finetuning_Text_Classification.ipynb)
- 목적: 뉴스 제목을 기반으로 기사 카테고리 분류 모델 학습 및 평가
- 모델: KLUE/roberta-base (BERT 변형, 인코더 기반)
- 데이터셋: KLUE-YNAT (연합뉴스 기사 제목 및 카테고리)
- 실습 내용:
  - 토큰화 및 데이터 전처리
  - AutoModelForSequenceClassification을 활용한 모델 불러오기 및 학습
  - Trainer API vs. 직접 학습 비교 (85% vs. 83% 정확도)
 - 결과 및 한계점:
  - Trainer API는 간편하지만 내부 과정 확인이 어려움
  - 일부 키워드 중심 예측 현상, 비정제 데이터에서는 성능 저하 가능 <br>

<br>

2. T5-small vs. Mistral-7B: 한국어 뉴스 요약 모델 비교 <br>
🤗 [T5 기반 모델 바로가기](https://huggingface.co/edgeun/t5-small-korean-news-summarizer) | 📝 [T5 파인튜닝 코드](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_t5_small_korean_news_summarizer.ipynb) <br>
🤗 [Mistral 기반 모델 바로가기](https://huggingface.co/edgeun/mistral-7b-instruct-v0.1-korean-news-summarizer) | 📝 [Mistral 파인튜닝 코드](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Mistral_7B_Instruct_v0_1_Finetuning_Korean_News_summarizer.ipynb)
- 목적: 뉴스 본문을 요약하는 모델 학습 및 성능 비교
- 모델: T5-small (Text2Text), Mistral-7B-Instruct (디코더 기반)
- 데이터셋: daekeun-ml/naver-news-summarization-ko (네이버 뉴스 요약)
- 실습 내용:
  - T5: “summarize:” 프롬프트 추가, 패딩 처리 (-100)
  - Mistral: Instruction Following 방식으로 프롬프트 구성
  - LoRA 적용 후 학습 (제한된 환경 고려, 1 epoch)
- 결과 및 한계점:
  - ROUGE: Mistral > T5 (0.41 vs. 0.26)
  - BERTScore: T5 > Mistral (0.81 vs. 0.79)
  - 튜닝 모델 추론 결과 입력 문장을 이해하고 문장을 요약하는 T5의 요약문의 끝맺음과 완성도가 높아보임
  - Mistral은 문장 끝맺음, 중복 단어 문제 발생
  - 모델 구조에 따라 데이터 전처리 방식이 성능에 큰 영향 <br>
  
<br>

3. Task: AI 상담사 모델(Text Generation) | 🤗 [모델 바로가기](https://huggingface.co/edgeun/gemma-2-9b-it-ai-counselor) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Gemma_2_9B_it_FineTuning_AI_counselor.ipynb)
   - Base Model: Gemma-2-9B-it 인스트럭션 튜닝 모델
   - 데이터셋: 상담 대화 형식
   - 모델 평가: 챗GPT를 활용한 정성적 평가 <br>

<br>

4. Task: 한국어 질의 → SQL 생성(Text Generation) | 🤗 [모델 바로가기](https://huggingface.co/edgeun/yi-ko-6b-text2sql) | 📝 [코드 바로가기](https://github.com/edgeun/portfolio-24-25/blob/main/Python/STUDY/ML_DL/LLM_Finetuning_Text_Generation_Text2SQL.ipynb)
   - Base Model: Llama-2 기반 한/영 혼합 사전학습 모델
   - 데이터셋: 한국어 질의-SQL 쿼리문
   - 모델 평가: 챗GPT와 비교 평가 <br>
   
<br>

### Tableau 데이터 시각화 & 대시보드 제작 실습 ###
- 24년 서울시 공공자전거 이용 현황 | 📊 [대시보드 바로가기](https://public.tableau.com/views/01__17398849609510/1_1?:language=ko-KR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- 23년 서울시 미세먼지농도 현황과 농도 나쁨단계 이상일수 파악 | 📊 [대시보드 바로가기](https://public.tableau.com/views/02__17400408648250/1_1?:language=ko-KR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- 전국 시/도, 시/군/구별 20리터 종량제 쓰레기 봉투 가격 (24년 4월 기준) | 📊 [대시보드 바로가기](https://public.tableau.com/views/03__17400604327870/1_1?:language=ko-KR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
