## Case 1. 서울시 구별 CCTV 현황 분석
import pandas as pd
import numpy as np

# cctv 데이터 불러오기
# 교재본 데이터 말고 최신 데이터로 불러오기 (데이터 출처: https://data.seoul.go.kr/dataList/OA-2734/F/1/datasetView.do)
cctv_seoul = pd.read_csv("/content/01_cctv_seoul_24.csv", header=1, encoding='utf-8')

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

# 인구 데이터 불러오기 (최근 데이터: https://data.seoul.go.kr/dataList/419/S/2/datasetView.do)
# 3번째(2) 행을 헤더로 사용하고 엑셀 파일에서 B, D, G, J, N 컬럼만 불러오겠다.
pop_seoul = pd.read_excel("/content/등록인구_20250111020137.xls", header = 2, usecols = 'B, D, G, J, N')
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

pop_seoul.sort_values(by='외국인', ascending=False).head(5)     # 구로구, 영등포구, 동대문구, 관악구, 광진구
pop_seoul.sort_values(by='외국인비율', ascending=False).head(5)  # 중구, 종로구, 용산구, 영등포구, 금천구

pop_seoul.sort_values(by='고령자', ascending=False).head(5)     # 송파구, 강서구, 노원구, 은평구, 강남구
pop_seoul.sort_values(by='고령자비율', ascending=False).head(5)  # 강북구, 도봉구, 중랑구, 은평구, 중구

# 두 데이터프레임 병합 기능 살펴보기
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

result = pd.concat([df1, df2, df3])  # 아무 속성이 없으면 열방향(세로방향)으로 이어붙여짐(=행이 추가됨)
result

result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])
result

result.index  # 기본 인덱스 + 지정한 keys로 구성된 다중인덱스 형태

result.index.get_level_values(0)  # 지정한 keys 확인

result.index.get_level_values(1)  # 기본 인덱스 확인

result

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'], 
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])

result = pd.concat([df1, df4], axis=1)  # 행방향(가로)으로 concat 처리 (열이 추가됨)  # 위에서 지정한 인덱스 번호에 붙고 나머지 빈공간은 null
result

result = pd.concat([df1, df4], axis=1, join='inner')  # join='inner' 옵션을 사용하면 공통된 인덱스 부분만 처리
result

result = pd.concat([df1, df4.reindex(df1.index)], axis=1)  # df1 인덱스에 강제로 맞춤
result

result = pd.concat([df1, df4], ignore_index=True)
result

left = pd.DataFrame({'key': ['K0', 'K4', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

left

right

pd.merge(left, right, on='key')  # 'key' 컬럼을 기준으로 두 데이터프레임에서 공통된 데이터를 합침 (sql 이퀄 조인 개념과 비슷)
pd.merge(left, right, how='inner', on='key')

pd.merge(left, right, how='left', on='key')  # left outer join
pd.merge(left, right, how='right', on='key')  # right outer join
pd.merge(left, right, how='outer', on='key')  # full outer join
