## 참고: 파이썬으로 데이터 주무르기

### #1. 서울시 구별 CCTV 현황 분석
import pandas as pd
import numpy as np

# cctv 데이터 불러오기  # 교재본 데이터 말고 최신 데이터로 불러오기
cctv_seoul = pd.read_csv("/Users/dgriii0606/data/01_cctv_seoul_24.csv", header=1, encoding='utf-8')

# 순번 컬럼 삭제
cctv_seoul = cctv_seoul.drop(['순번'], axis=1)
cctv_seoul

cctv_seoul.columns

# 컬럼명 변경
cctv_seoul.rename(columns={ cctv_seoul.columns[0] : '구별',
                            cctv_seoul.columns[1] : '소계',
                            cctv_seoul.columns[2] : '2016년 이전',
                            cctv_seoul.columns[-1] : '2024년' }, inplace=True)

# 2024년 컬럼 삭제  # 24년도는 최신화가 안 되어있으므로 23년도 까지만 사용
cctv_seoul = cctv_seoul.drop(['2024년'], axis=1)
cctv_seoul

# 합계 행 삭제
cctv_seoul.drop([0], inplace=True)
cctv_seoul.head()

# 인구 데이터 불러오기  # 3번째(2) 행을 헤더로 사용하고 엑셀 파일에서 B, D, G, J, N 컬럼만 불러오겠다.
pop_seoul = pd.read_excel("/Users/dgriii0606/data/등록인구_20250111020137.xls", header = 2, usecols = 'B, D, G, J, N')
pop_seoul.head()

# 각 컬럼명 변경
pop_seoul.rename(columns={pop_seoul.columns[0] : '구별',
                          pop_seoul.columns[1] : '인구수',
                          pop_seoul.columns[2] : '한국인',
                          pop_seoul.columns[3] : '외국인',
                          pop_seoul.columns[4] : '고령자'}, inplace=True)
pop_seoul.head()

# cctv 수가 가장 적은 자치구 상위 5개 뽑기
cctv_seoul.sort_values(by='소계', ascending=True).head(5)  # 종로구, 도봉구, 중구, 노원구, 금천구

# cctv 수가 가장 많은 자치구 상위 5개 뽑기
cctv_seoul.sort_values(by='소계', ascending=False).head(5)  # 강남구, 관악구, 구로구, 서초구, 은평구

# 최근증가율 구해서 새 컬럼 생성하기  # 21~23년의 cctv 수 합 / 16~17년의 cctv 수 합  # '16년 이전' 데이터가 교재 데이터(13년 이전)보다 훨씬 적어서 업데이트가 안 된 듯
# 구하기 전에 최신 데이터는 값에 콤마(,)가 들어간 문자형 데이터가 들어가 있으므로 콤마를 제거하고 모두 숫자형으로 변환 후 교재 내용대로 진행

# 숫자 변환 대상 컬럼 리스트 지정
numcolumns = ['소계', '2016년 이전', '2016년', '2017년', '2018년', '2019년', 
                      '2020년', '2021년', '2022년', '2023년']

# 콤마 제거 후 숫자형 변환
for col in numcolumns:
    cctv_seoul[col] = cctv_seoul[col].replace(',', '', regex=True).astype(int)

cctv_seoul.head()

cctv_seoul['최근증가율'] = (cctv_seoul['2021년'] + cctv_seoul['2022년'] + cctv_seoul['2023년']) / (cctv_seoul['2016년'] + cctv_seoul['2017년'])
cctv_seoul.sort_values(by='최근증가율', ascending=False).head(5)

# 인구 데이터에서 합계 행 삭제하기
pop_seoul.drop([0], inplace=True)
pop_seoul.head()

# 구별 컬럼의 unique값 조사
pop_seoul['구별'].unique()

# 외국인 비율과 고령자 비율 구하기
pop_seoul['외국인비율'] = pop_seoul['외국인'] / pop_seoul['인구수'] * 100
pop_seoul['고령자비율'] = pop_seoul['고령자'] / pop_seoul['인구수'] * 100
pop_seoul.head()

# 인구수 순위 조사하기
pop_seoul.sort_values(by='인구수', ascending=False).head(5)  # 송파구, 강남구, 강서구, 노원구, 관악구
pop_seoul.sort_values(by='외국인', ascending=False).head(5)  # 구로구, 영등포구, 동대문구, 관악구, 광진구
