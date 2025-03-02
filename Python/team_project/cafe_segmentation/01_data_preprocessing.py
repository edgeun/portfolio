# 사용 데이터: 서울시 상권분석 ‘상권’ 단위 데이터 (제공: 서울 열린데이터 광장) / 상업용부동산 분기별 지역별 임대료 데이터 / 2023년 4분기
# 데이터 출처: https://data.seoul.go.kr/dataList/OA-15560/S/1/datasetView.do

# 데이터 불러오기 → 필요 컬럼 추출 → 데이터 병합 → 파생변수 생성 → 결측치 처리

# 데이터 불러오기
import pandas as pd

# 모든 컬럼을 출력하도록 설정
pd.set_option('display.max_columns', None)

# 영역, 점포, 상권
area = pd.read_csv('~/areas.csv', encoding = 'cp949')
store = pd.read_csv('~/stores.csv', encoding = 'cp949')
change = pd.read_csv('~/changes.csv', encoding = 'cp949')

# 유동인구, 상주인구, 직장인구, 아파트
work = pd.read_csv('~/works.csv', encoding = 'cp949')
road = pd.read_csv('~/roads.csv', encoding = 'cp949')
live = pd.read_csv('~/lives.csv', encoding = 'cp949')
apt = pd.read_csv('~/apts.csv', encoding = 'cp949')

# 소득, 매출
money = pd.read_csv('~/moneys.csv', encoding = 'cp949')
sell = pd.read_csv('~/sells.csv', encoding = 'cp949')

# 집객시설
infra = pd.read_csv('~/infras.csv', encoding = 'cp949')

# 임대료
rent = pd.read_csv('~/rent_avg.csv', encoding = 'utf-8')


# area 상권명, 면적 추출
area2 = area[['상권_코드_명', '영역_면적', '자치구_코드_명', '행정동_코드_명']]
# area2.shape  # (1650, 2)

# change 상권 변화 지표 컬럼 추출
change2 = change[['기준_년분기_코드', '상권_코드_명', '상권_변화_지표', '운영_영업_개월_평균', '폐업_영업_개월_평균']][change['기준_년분기_코드']==20234]

# store 상권 변화 지표 컬럼 추출
store2 = store[['상권_코드_명', '유사_업종_점포_수', '개업_점포_수', '폐업_점포_수', '프랜차이즈_점포_수']][( store['기준_년분기_코드']==20234 ) & ( store['서비스_업종_코드_명']=='커피-음료' )]

# live 상주인구 필요한 컬럼 추출
live2 = live[['상권_코드_명', '총_상주인구_수', '여성_상주인구_수']][live['기준_년분기_코드']==20234]

# road 유동인구 필요한 컬럼 추출
road2 = road[['상권_코드_명', '총_유동인구_수', '연령대_20_유동인구_수', '연령대_30_유동인구_수']][road['기준_년분기_코드']==20234]

# apt 아파트 필요한 컬럼 추출
apt2 = apt[['상권_코드_명', '아파트_단지_수']][apt['기준_년분기_코드']==20234]

# work 직장인구 필요한 컬럼 추출
work2 = work[['상권_코드_명', '총_직장_인구_수']][work['기준_년분기_코드']==20234]

# money 소득소비 컬럼 추출
money2 = money[['상권_코드_명', '월_평균_소득_금액', '지출_총금액']][money['기준_년분기_코드']==20234]

# sell 매출 컬럼 추출
sell2 = sell[['상권_코드_명', '당월_매출_금액', '연령대_20_매출_금액', '연령대_30_매출_금액']][( sell['기준_년분기_코드']==20234 ) & ( sell['서비스_업종_코드_명']=='커피-음료' )]

# infra 집객 시설 추출
infra2 = infra[['상권_코드_명', '집객시설_수', '지하철_역_수', '버스_정거장_수', '대학교_수']][infra['기준_년분기_코드']==20234]

# # rent 임대료 추출해서 area와 조인하기 위한 컬럼명 변경
# rent2 = rent[rent['자치구_코드_명'].notnull()]
# rent3 = rent2[['자치구_코드_명','2023년 4분기']]
# rent4 = rent3.groupby('자치구_코드_명')['2023년 4분기'].mean().round(2).reset_index()  # 자치구별 임대료 평균
# rent4.columns = ['자치구_코드_명', '임대료']

# rent에 상권 붙이기
arear = area2[['상권_코드_명', '자치구_코드_명']]
rent2 = arear.merge(rent, on='자치구_코드_명', how='left')  # '자치구_코드_명'을 기준으로 두 데이터프레임 병합
rent3 = rent2.drop(columns=['자치구_코드_명'])


# 머지 작업
merge1 = pd.merge( area2, change2, on= '상권_코드_명', how= 'left' )
merge2 = pd.merge( merge1, store2, on= '상권_코드_명', how= 'left' )
merge3 = pd.merge( merge2, live2, on= '상권_코드_명', how= 'left' )
merge4 = pd.merge( merge3, road2, on= '상권_코드_명', how= 'left' )
merge5 = pd.merge( merge4, apt2, on= '상권_코드_명', how= 'left' )
merge6 = pd.merge( merge5, work2, on= '상권_코드_명', how= 'left' )
merge7 = pd.merge( merge6, money2, on= '상권_코드_명', how= 'left' )
merge8 = pd.merge( merge7, sell2, on= '상권_코드_명', how= 'left' )
merge9 = pd.merge( merge8, infra2, on= '상권_코드_명', how= 'left' )
merge10 = pd.merge( merge9, rent3, on= '상권_코드_명', how= 'left' )


# 파생변수 생성
sang1 = merge10.copy()
sang1['100m_당_카페_점포_수'] = ( sang1['유사_업종_점포_수'] / ( sang1['영역_면적'] / 10000 ) ).round(1) # 10000 제곱 미터로 나누니깐 100미터 x 100미터 당
sang1['100m_당_프랜차이즈_점포_수'] = ( sang1['프랜차이즈_점포_수'] / ( sang1['영역_면적'] / 10000 ) ).round(1)
sang1['100m_당_유동인구_수'] = ( sang1['총_유동인구_수'] / ( sang1['영역_면적'] / 10000 ) ).round(1)
sang1['100m_당_2030_유동인구_수'] = ( ( sang1['연령대_20_유동인구_수'] + sang1['연령대_30_유동인구_수'] ) / ( sang1['영역_면적'] / 10000 ) ).round(1)
sang1['100m_당_상주인구_수'] = ( sang1['총_상주인구_수'] / ( sang1['영역_면적'] / 10000 ) ).round(1)
sang1['100m_당_직장인구_수'] = ( sang1['총_직장_인구_수'] / ( sang1['영역_면적'] / 10000 ) ).round(1)
sang1['100m_당_집객시설_수'] = ( sang1['집객시설_수'] / ( sang1['영역_면적'] / 10000 ) ).round(1)
sang1['점포_당_당월_매출_금액'] = ( sang1['당월_매출_금액'] / sang1['유사_업종_점포_수'] ).round(2)
sang1['점포_당_2030_당월_매출_금액'] = ( ( sang1['연령대_20_매출_금액'] + sang1['연령대_30_매출_금액'] ) / sang1['유사_업종_점포_수'] ).round(2)


# 결측치 확인 및 처리
sang1.isnull().sum()

# '수'로 끝나는 컬럼들의 결측치를 0으로 채우기
sang1 = sang1.fillna({col: 0 for col in sang1.columns if col.endswith('수')})

sang1.isnull().sum()

# 나머지 결측치가 있는 컬럼들에 대해 평균값으로 결측치 채우기 (inplace=False 방식으로 처리)
for col in sang1.columns:
    if sang1[col].isnull().sum() > 0:  # 결측치가 있는 컬럼만 처리
        # '유사_점포_업종_수'가 0인 경우 해당 컬럼의 결측치를 0으로 채우기
        condition = (sang1['유사_업종_점포_수'] == 0) & (sang1[col].isnull())
        sang1.loc[condition, col] = 0

        # 그 외의 결측치는 평균으로 채우기
        sang1[col] = sang1[col].fillna(sang1[col].mean().round(2))

# 결과 확인
sang1.isnull().sum()

sang1.to_csv('sang_2023_nn_de_10.csv', index=False)  # csv 파일로 저장
