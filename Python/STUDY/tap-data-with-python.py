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

pd.merge(left, right, on='key')  # 'key' 컬럼을 기준으로 두 데이터프레임에서 공통된 데이터를 합침 (sql 이퀄 조인 개념)
pd.merge(left, right, how='inner', on='key')

pd.merge(left, right, how='left', on='key')  # left outer join
pd.merge(left, right, how='right', on='key')  # right outer join
pd.merge(left, right, how='outer', on='key')  # full outer join

# CCTV 데이터와 인구 데이터 합치고 분석하기
data_result = pd.merge(cctv_seoul, pop_seoul, on='구별')
data_result.head()

del data_result['2016년 이전']  # del 열방향으로 삭제하는 명령어(컬럼 삭제)
del data_result['2016년']
del data_result['2017년']
del data_result['2018년']
data_result.head()

data_result.set_index('구별', inplace=True)  # 구별 컬럼을 인덱스로 -> 이후에 그래프를 그릴 때 유리
data_result.head()

# 상관계수 확인
np.corrcoef(data_result['고령자비율'],data_result['소계'])

np.corrcoef(data_result['외국인비율'],data_result['소계'])

np.corrcoef(data_result['인구수'],data_result['소계'])

data_result.sort_values(by='소계', ascending=False).head(5)

data_result.sort_values(by='인구수', ascending=False).head(5)

# matplotlib로 그래프 그리기
import matplotlib.pyplot as plt
%matplotlib inline

plt.figure()
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()

import numpy as np
t = np.arange(0, 12, 0.01)
y = np.sin(t)

plt.figure(figsize=(7, 5))
plt.plot(t, y)
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(t, y)
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(t, np.sin(t))  # y값 대신 직접 첫번째 그래프 지정
plt.plot(t, np.cos(t))  # 두번째 그래프 지정
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(t, np.sin(t), label='sin')  # 범례 이름 지정
plt.plot(t, np.cos(t), label='cos')  # 범례 이름 지정
plt.grid()
plt.legend()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(t, np.sin(t), lw=3, label='sin')  # 범례 이름 지정
plt.plot(t, np.cos(t), 'r', label='cos')  # 범례 이름 지정
plt.grid()
plt.legend()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()

t = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]
plt.figure(figsize=(7, 5))
plt.plot(t, y, color='green')  # 컬러 지정
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(t, y, color='green', linestyle='dashed')  # 라인 스타일 지정
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(t, y, color='green', linestyle='dashed', marker='o')  # 값에 마커 추가
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(t, y, color='green', linestyle='dashed', marker='o')  # 값에 마커 추가
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(t, y, color='green', linestyle='dashed', marker='o', markerfacecolor = 'blue')
plt.show()

t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([9, 8, 7, 9, 8, 3, 2, 4, 3, 4])

plt.figure(figsize=(7, 5))
plt.scatter(t, y)
plt.show()

plt.figure(figsize=(7, 5))
plt.scatter(t, y, marker='>')
plt.show()

colormap = t

plt.figure(figsize=(7, 5))
plt.scatter(t, y, s=50, marker='>', c=colormap)
plt.colorbar()
plt.show()

s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)

plt.figure(figsize=(7, 5))
plt.plot(s1, label='s1')
plt.plot(s2, label='s2')
plt.plot(s3, label='s3')
plt.legend()
plt.show()

# 박스 플롯
plt.figure(figsize=(7, 5))
plt.boxplot((s1, s2, s3))
plt.grid()
plt.show()

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib-rf

import sys

# Google Colab 환경에서 실행 중인지 확인
if 'google.colab' in sys.modules:
    # debconf를 Noninteractive 모드로 설정
    !echo 'debconf debconf/frontend select Noninteractive' | \
    debconf-set-selections

    # fonts-nanum 패키지를 설치
    !sudo apt-get -qq -y install fonts-nanum
    
    # Matplotlib의 폰트 매니저 가져오기
    import matplotlib.font_manager as fm
    
    # 나눔 폰트의 시스템 경로 찾기
    font_files = fm.findSystemFonts(fontpaths=['/usr/share/fonts/truetype/nanum'])
    
    # 찾은 각 나눔 폰트를 Matplotlib 폰트 매니저에 추가
    for fpath in font_files:
        fm.fontManager.addfont(fpath)

plt.rcParams['font.family'] = 'NanumGothic'    #사용 방법1
plt.rc('font', family='NanumBarunGothic', size=11) #사용 방법2
print(plt.rcParams['font.family'], plt.rcParams['font.size'])   # 폰트확인

data_result.head()

plt.figure
# data_result['소계'].plot(kind='barh', grid=True, figsize=(10, 10))
# plt.show()

data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10, 10))
plt.show()

data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100
data_result['CCTV비율'].sort_values().plot(kind='barh', grid=True, figsize=(10, 10))
plt.show()

plt.figure(figsize=(6, 6))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

# numpy의 polyfit으로 회귀선 그리기
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
fp1

f1 = np.ploy1d(fp1)  # 
fx = np.linspace(100000, 700000, 100)

plt.figure(figsize=(6, 6))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)

fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)  # 인구수와 소계에 대한 1차 회귀 직선
fp1  # array([5.24640838e-03, 2.06897579e+03]) : 기울기, 절편

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)

# 회귀 선과 실제 데이터의 차이값(잔차)을 오차 컬럼에 저장
data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구수']))

# 잔차 상위 10개의 구를 뽑기 위해 오차 순으로 정렬 후 df_sort에 저장
df_sort = data_result.sort_values(by='오차', ascending=False)
df_sort.head()

plt.figure(figsize=(14, 10))
plt.scatter(data_result['인구수'], data_result['소계'], c=data_result['오차'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

for n in range(10):  # 잔차 상위 10개의 값만 스캐터 포인트에 표시
    plt.text(df_sort['인구수'][n]*1.02, df_sort['소계'][n]*0.98, df_sort.index[n], fontsize=15)  # *1.02는 점과 텍스트가 겹치지 않도록 텍스트 위치 조정

plt.xlabel('인구수')
plt.ylabel('인구당 CCTV 설치 비율')

plt.colorbar()
plt.grid()
plt.show()

# 강남구, 관악구, 구로구, 서초구는 서울의 다른 구와 비교했을 때 상대적으로 CCTV 설치 비율이 높고
# 송파구, 강서구, 강동구, 노원구, 도봉구는 CCTV 설치 비율이 낮다.
