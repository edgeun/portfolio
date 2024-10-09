# 01. (데이터 전처리 1) 문자열을 특정 문자로 감싸는 함수
def wrap(text, char = "'"):
    return char + text + char



# 02. (데이터 시각화 1) 막대 그래프 그리는 함수
import plotly.graph_objects as go

## x와 y 리스트를 받아 막대 그래프를 그리는 함수
def plot_bar_graph(x, y):
    fig = go.Figure(data=[go.Bar(x=x, y=y, marker=dict(color='#1b4d3e'))]) # 막대 그래프 생성
    
    # 레이아웃 설정
    fig.update_layout(
        title="막대 그래프 예시",
        xaxis_title="X 축",
        yaxis_title="Y 축",
        template="plotly", # 다른 스타일 사용 가능: "plotly_dark", "ggplot2"
        font=dict(
            family="Arial, sans-serif",
            size=14,
            color="#6e7b8b"
        ),
        plot_bgcolor='#eee9e9',  # 그래프 플롯 배경색
        paper_bgcolor='#ffffff', # 전체 배경색
        xaxis=dict(
            gridcolor='LightGray'  # X축 그리드 라인 색상
        ),
        yaxis=dict(
            gridcolor='LightGray'  # Y축 그리드 라인 색상
        )
    )
    
    # 그래프 표시
    fig.show()



# 03. (데이터 시각화 2) 원형 그래프 그리는 함수
import plotly.graph_objects as go   # 파이썬 plotly 라이브러리를 가져오는 코드

## labels와 values 리스트를 받아 원형 그래프를 그리는 함수.
def plot_pie_graph(labels, values):    # 원형 그래프 그리는 함수 # 함수(파이조각 이름, 파이조각 크기)

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)]) # 원형 그래프 객체 생성
    # 레이아웃 설정
    fig.update_layout(
    title="원형 그래프 예시",  
    template="plotly",  # 다른 스타일 사용 가능: "plotly_dark", "ggplot2"
    font=dict(   # 그래프에서 사용되는 글꼴 스타일을 지정
    family="Arial, sans-serif",
    size=14,
    color="RebeccaPurple"
    )
    )
    # 그래프 표시
    fig.show()



# 04. (웹스크래핑 1) 한국일보 신문 기사 데이터 수집 함수
# 관련 키워드 상세 기사 url 가져오는 함수 + 상세 url의 본문 기사 가져와서 txt 파일로 저장하는 함수
import urllib.request
from bs4 import BeautifulSoup
import time

# 상세 기사 url 수집함수
def hankook_detail_url(keyword, num):
    text1 = urllib.parse.quote(keyword)
    params = [ ] # 비어있는 리스트를 생성합니다. 
    
    for i in range(1, num+1):
        list_url = "https://search.hankookilbo.com/Search?Page=" + str(i) + "&tab=NEWS&sort=relation&searchText=" + text1 + "&searchTypeSet=TITLE,CONTENTS&selectedPeriod=%EC%A0%84%EC%B2%B4&filter=head"
        url = urllib.request.Request(list_url)
        f = urllib.request.urlopen(url).read().decode("utf-8")
    
        soup = BeautifulSoup(f , "html.parser")
        
        for i in soup.select("div.inn > h3.board-list.h3.pc_only > a"):
            params.append(i.get("href"))
            
        time.sleep(1)
    
    return params

# 함수 실행 테스트
# hankook_detail_url('비건&채식', 1)

# 기사 본문 수집 함수
def hankook(keyword, num):
    f_hankook = open("c:\\data\\hankook.txt", "w", encoding="utf8")
    
    result = hankook_detail_url(keyword, num)
    
    for i in result:
        url = urllib.request.Request(i)
        f = urllib.request.urlopen(url).read().decode("utf-8")
        
        soup = BeautifulSoup(f, "html.parser")

        # 날짜 가져오기
        for d in soup.select("div.innerwrap > div > div.info > dl"):
            date_text = d.text.strip()
            f_hankook.write(date_text + '\n')
            print(date_text)

        print()

        # 본문 가져오기
        for i in soup.select("div.col-main p"):
            article_text = i.text.strip() # 본문 기사 양쪽에 있을지 모르는 공백을 잘라냄
            f_hankook.write(article_text + '\n') # 본문기사 저장
            print(article_text)

        f_hankook.write("\n" + "=" * 50 + "\n\n") # 기사 구분선(저장용)
        print("\n" + "=" * 50 + "\n\n") # 기사 구분선(출력용)

    f_hankook.close()

# 함수 활용 예시
# hankook('비건&채식', 1)



# 05. (웹스크래핑 2) 동아일보 신문 기사 데이터 수집 함수
import urllib.request
from bs4 import BeautifulSoup
import time

# 상세 기사 url 수집함수
def donga_detail_url(keyword, num):
    text1 = urllib.parse.quote(keyword)
    params = [ ] # 비어있는 리스트를 생성합니다. 
    
    for i in range(0, num):
        list_url = "https://www.donga.com/news/search?p=" + str(i) + "1&query=" + text1 + "&check_news=91&sorting=1&search_date=1&v1=&v2=&more=1"
        url = urllib.request.Request(list_url)
        f = urllib.request.urlopen(url).read().decode("utf-8")
    
        soup = BeautifulSoup(f, "html.parser")
        
        for i in soup.select("article > div > h4 > a"):
            params.append(i.get("href"))
            
        time.sleep(1)
    return params

# 함수 실행 테스트    
# donga_detail_url('인공지능', 1)

# 기사 본문 수집 함수
def donga(keyword, num):
    f_donga = open("c:\\data\\donga.txt", "w", encoding="utf8")
    
    result = donga_detail_url(keyword, num)
    
    for i in result:
        url = urllib.request.Request(i)
        f = urllib.request.urlopen(url).read().decode("utf-8")
        
        soup = BeautifulSoup(f, "html.parser")

        # 날짜 가져오기
        for d in soup.select("header > div > section > ul > li:nth-child(2)"):
            date_text = d.text.strip()
            f_donga.write(date_text + '\n\n')
            print(date_text + '\n')

        # 본문 가져오기
        for i in soup.select("div.main_view > section.news_view"):
            article_text = i.text.strip() # 본문 기사 양쪽에 있을지 모르는 공백을 잘라냄
            f_donga.write(article_text + '\n') # 본문기사 저장
            print(article_text)

        f_donga.write("\n" + "=" * 50 + "\n\n") # 기사 구분선(저장용)
        print("\n" + "=" * 50 + "\n\n") # 기사 구분선(출력용)

    f_donga.close()

# 함수 활용 예시
# donga('인공지능', 1)



# 06. (웹스크래핑 3) 중앙일보 신문 기사 데이터 수집 함수
import urllib.request
from bs4 import BeautifulSoup
import time

# 상세 기사 url 수집함수
def ja_detail_url(keyword, num):
    text1 = urllib.parse.quote(keyword)
    params = [ ] # 비어있는 리스트를 생성합니다. 
    
    for i in range(1, num+1):
        list_url = "https://www.joongang.co.kr/search/news?keyword=" + text1 + "&page=" + str(i)
        url = urllib.request.Request(list_url)
        f = urllib.request.urlopen(url).read().decode("utf-8")
    
        soup = BeautifulSoup(f, "html.parser")
        
        for i in soup.select("div.card_body > h2.headline > a"):
            params.append(i.get("href"))

        if len(params) > 5:      # 중앙일보는 옆에 서브 기사까지 같이 스크래핑되므로
            params = params[:-5] # 옆에 관련없는 5개 기사를 제외해주는 코드
            
        time.sleep(1)
    
    return params

# 함수 실행 테스트
# ja_detail_url('에너지', 1)

# 기사 본문 수집 함수
def ja(keyword, num):
    f_ja = open("c:\\data\\ja.txt", "w", encoding="utf8")
    
    result = ja_detail_url(keyword, num)
    
    for i in result:
        url = urllib.request.Request(i)
        f = urllib.request.urlopen(url).read().decode("utf-8")
        
        soup = BeautifulSoup(f, "html.parser")

        # 날짜 가져오기 (datetime 속성 값)
        date_text = ""
        date_element = soup.select_one("time")  # 첫번째 time 태그를 선택합니다. 

        if date_element:
            date_text = date_element['datetime'].strip()  # datetime 속성 값 가져오기
            f_ja.write(date_text + '\n')  # 날짜 저장
            # print(date_text + '\n')

        # 본문 가져오기
        for i in soup.select("#article_body"):
            article_text = i.text.strip() # 본문 기사 양쪽에 있을지 모르는 공백을 잘라냄
            f_ja.write(article_text + '\n') # 본문기사 저장
            # print(article_text)

        f_ja.write("\n" + "=" * 50 + "\n\n") # 기사 구분선(저장용)
        # print("\n" + "=" * 50 + "\n\n") # 기사 구분선(출력용)

    f_ja.close()

# 함수 활용 예시
# ja('에너지', 1)


# 07. (웹스크래핑 4) 한겨레 신문 기사 데이터 수집 함수
import urllib.request
from bs4 import BeautifulSoup
import time

from datetime import datetime # 한겨레 url 내 현재날짜를 변경하기 위한 모듈 불러오기

# 상세 기사 url 수집함수
def hani_detail_url(keyword, num):
    text1 = urllib.parse.quote(keyword)
    params = [ ]   # 상세기사 url 을 저장하기 위한 리스트 입니다.  
    params2 = [ ]  # 날짜를 저장하기 위한 리스트 입니다. 

    today = datetime.today() # 현재날짜를 today 변수에 담음
    date = str(today)[0:10].replace("-", ".") # 현재날짜에서 필요한 부분만 잘라내고 -를 .으로 변환함
    
    for i in range(1,num+1):
        list_url = "https://search.hani.co.kr/search/newslist?searchword=" + text1 + "&startdate=1988.01.01&enddate=" + date + "&page=" + str(i) + "&sort=desc"
        url = urllib.request.Request(list_url)
        f = urllib.request.urlopen(url).read().decode("utf-8")
    
        soup = BeautifulSoup(f, "html.parser")
        # 상세 기사 url 가져오기 
        for i in soup.select("article > a"):
            params.append(i.get("href"))

        # 상세 기사의 날짜 가져오기
        for i in soup.select("span.article-date"):
            params2.append(i.text)
            
        time.sleep(1)
    
    return params, params2

# 함수 실행 테스트
# hani_detail_url('비건&채식', 1)

# 기사 본문 수집 함수
def hani(keyword, num):
    f_hani = open("c:\\data\\hani.txt", "w", encoding="utf8")
    
    result1, result2 = hani_detail_url(keyword, num)
    
    for i, d in zip(result1, result2):
        url = urllib.request.Request(i)
        f = urllib.request.urlopen(url).read().decode("utf-8")
        
        soup = BeautifulSoup(f, "html.parser")

        # 날짜 가져오기
        f_hani.write(d + '\n')
        print(d)

        print()

        # 본문 가져오기
        for i in soup.select("div > p"):
            article_text = i.text.strip() # 본문 기사 양쪽에 있을지 모르는 공백을 잘라냄
            f_hani.write(article_text + '\n') # 본문기사 저장
            print(article_text)

        f_hani.write("\n" + "=" * 50 + "\n\n") # 기사 구분선(저장용)
        print("\n" + "=" * 50 + "\n\n") # 기사 구분선(출력용)

    f_hani.close()

# 함수 활용 예시
# hani('비건&채식', 1)



# 08. (웹스크래핑 5) 국민일보 신문 기사 데이터 수집 함수
import urllib.request
from bs4 import BeautifulSoup
import time

# 상세 기사 url 수집함수
def km_detail_url(keyword, num):
    text1 = urllib.parse.quote(keyword, encoding="cp949")
    params = [ ]   # 상세기사 url 을 저장하기 위한 리스트 입니다.
    
    for i in range(1,num+1):
        list_url = "https://www.kmib.co.kr/search/searchResult.asp?searchWord=" + text1 + "&pageNo=" + str(i) + "&period="
        url = urllib.request.Request(list_url) # 국민일보 url에 접속 요청
        f = urllib.request.urlopen(url).read().decode("cp949") # 국민일보 신문사 html 코드 수집
        # utf-8로 디코딩 안되면 딱 2개만 기억하면 된다. => utf-8 과 cp949
    
        soup = BeautifulSoup(f, "html.parser") # html 코드를 BF 함수로 파싱
        # 상세 기사 url 가져오기 
        for i in soup.select("div.search_nws > dl > dt.tit > a"):
            params.append(i.get("href"))

        time.sleep(1)
    
    return params

# 함수 실행 테스트
# km_detail_url('폭염', 1)

# 기사 본문 수집 함수
def km(keyword, num):
    f_km = open("c:\\data\\km.txt", "w", encoding="utf8")
    
    result = km_detail_url(keyword, num)
    
    for i in result:
        url = urllib.request.Request(i)
        f = urllib.request.urlopen(url).read().decode("cp949")
        
        soup = BeautifulSoup(f, "html.parser")

        # 날짜 가져오기
        for i in soup.select("div.sub_header > div > div > div > div.date"):
            date_text = i.text.strip() # 날짜 텍스트 양쪽에 있을지 모르는 공백을 잘라냄
            f_km.write(date_text + '\n') # 날짜 저장
            print(date_text)

        # 본문 가져오기
        for i in soup.select("div.tx"):
            article_text = i.text.strip() # 본문 기사 양쪽에 있을지 모르는 공백을 잘라냄
            f_km.write(article_text + '\n') # 본문기사 저장
            print(article_text)

        f_km.write("\n" + "=" * 50 + "\n\n") # 기사 구분선(저장용)
        print("\n" + "=" * 50 + "\n\n") # 기사 구분선(출력용)

    f_km.close()

# 함수 활용 예시
# km('폭염', 1)



# 09. (웹스크래핑 6) 조선일보 데이터 수집 함수
import urllib.request           # 웹요청
from bs4 import BeautifulSoup   # HTML 파싱
from selenium import webdriver  # 브라우저 제어 
from selenium.webdriver.chrome.service import Service  # 드라이버 관리
from selenium.webdriver.common.by import By  # 요소 탐색
import time  # 대기 시간

def chs_detail_url(keyword, num):
    # 키워드 검색
    text1 = urllib.parse.quote(keyword)
    # 크롬 드라이버 (크롬 봇) 경로 지정
    service = Service("C:\\data\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    params = []
    for i in range(1, num+1):
        list_url = "https://www.chosun.com/nsearch/?query="+ text1 +"&page="+ str(i) + "&siteid=www&sort=1&date_period=all&date_start=&date_end=&writer=&field=&emd_word=&expt_word=&opt_chk=false&app_check=0&website=www,chosun&category="
        driver.get(list_url) # 크롬이 열리면서 해당 url로 접속
        time.sleep(5) # 페이지가 완전히 로드 될 때까지 대기 (필요에 따라 조정)
        # html 페이지에서 iframe을 찾고 전환하는 코드
        try:
            iframe = driver.find_element(By.CSS_SELECTOR, "iframe_selector_here")
            driver.switch_to.frame(iframe)
            time.sleep(2)
        except:
            print("iframe을 찾을 수 없습니다. 기본 페이지에서 진행합니다.")

        # 크롬 봇이 직접 키워드로 검색한 페이지의 html 코드를 BS로 파싱함
        soup = BeautifulSoup(driver.page_source, "html.parser")
    
        # 기사 상세 URL을 params 리스트에 중복 없이 추가
        for i in soup.select("a.text__link.story-card__headline"):
            href = i.get("href") # i를 append 함수로 parmas에 바로 추가하지 않고 새로운 변수에 담은 후에
            if href not in params:  # 새로운 변수에 params가 담겨있지 않을 때만 (중복 체크)
                params.append(href) # params에 추가해라

    driver.quit() # 작업이 끝나면 브라우저를 종료함

    return params # 중복 없이 순서대로 추가된 기사 URL 리스트 반환

# 함수 실행 테스트
# chs_detail_url('전기차', 1)

# 기사 본문 수집 함수
def chosun(keyword, num):
    # 조선일보 본문 저장할 텍스트 파일 생성
    f_chosun = open("c:\\data\\chosun.txt", "w", encoding="utf8")
    
    # 상세 기사 url 가져오는 코드
    result = chs_detail_url(keyword, num)
    
    # 크롬 봇 위치 지정
    service = Service("C:\\data\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    for i in result:
        driver.get(i) # 상세 기사 url을 하나씩 가져와서 열어라
        time.sleep(5)
        # 자바스크립트가 있을지 모르므로 iframe을 찾아서 
        try:
            iframe = driver.find_element(By.CSS_SELECTOR, "iframe_selector_here")
            driver.switch_to.frame(iframe)
            time.sleep(2)
        except:
            print("iframe을 찾을 수 없습니다. 기본 페이지에서 진행합니다.")

        # 본문기사의 html 코드를 뽑아냄
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # 날짜 가져오기
        for i in soup.find('span', class_='inputDate'):
                f_chosun.write(i.get_text() + '\n')
                print(i.get_text() + '\n')
                
        # 본문 내용 가져오기
        for i in soup.select("div > section > article > section > p"):
            f_chosun.write(i.get_text() + '\n\n')
            print(i.get_text() + '\n\n')

    driver.quit()
    f_chosun.close()

# 함수 사용 예시
# chosun('전기차', 1)



# 10. (웹스크래핑 7) 네이버 블로그 데이터 수집 함수
import urllib.request           # 웹요청
from bs4 import BeautifulSoup   # HTML 파싱
from selenium import webdriver  # 브라우저 제어 
from selenium.webdriver.chrome.service import Service  # 드라이버 관리
from selenium.webdriver.common.by import By  # 요소 탐색
import time  # 대기 시간

def naver_blog_url(keyword, num):
    # 키워드 검색
    text1 = urllib.parse.quote(keyword)
    # 크롬 드라이버 (크롬 봇) 경로 지정
    service = Service("C:\\data\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    params = [] # 상세 url 담는 리스트

    for i in range(1, num+1): # 페이지 번호 제공 숫자
        time.sleep(1) # 블로그가 사진이 많으므로 로딩 시간을 고려함
        text1 = urllib.parse.quote(keyword) # 검색 키워드
        list_url = "https://section.blog.naver.com/Search/Post.naver?pageNo=" + str(i) + "&rangeType=ALL&orderBy=sim&keyword=" + text1

        # 크롬 봇이 웹페이지를 직접 열 수 있게 함
        driver.get(list_url)
        time.sleep(2)

        # 크롬 봇이 직접 연 웹페이지의 html 코드를 가져옴
        html = driver.page_source

        # html 코드를 BS로 파싱
        soup = BeautifulSoup(html, "lxml") # html.parser 또는 lxml을 사용

        # 블로그 상세 url 찾으러 가기
        for i in soup.select("div.desc > a.desc_inner"):
            params.append(i.get("href"))

    return params

# 함수 실행 테스트
# naver_blog_url("김예지선수", 1)

def naver_blog(keyword, num):
    # 상세 기사 url 가져오는 코드
    result = naver_blog_url(keyword, num)
    
    # 크롬 봇 위치 지정
    service = Service("C:\\data\\chromedriver-win32\\chromedriver.exe")
    driver2 = webdriver.Chrome(service=service)

    # 블로그 본문 저장할 텍스트 파일 생성
    f_nblog = open("c:\\data\\naver_blog.txt", "w", encoding="utf8")

    # 상세 url을 하나씩 가져와서 웹브라우저 열기
    for list_url in result:
        driver2.get(list_url)
        time.sleep(5) # 페이지가 열리는 시간을 충분히 줌

        # 자바 스크립트로 막혀있을지 모를 html 코드를 열어줌
        # 웹페이지에서 ID가 'mainFrame'인 html 요소를 찾는다
        # 이 mainFrame의 html 코드가 독립적으로 작동되는 코드여서 기존 코드와 통합 시킬려고 찾음
        try:    
            element = driver2.find_element(By.ID, 'mainFrame')
            driver2.switch_to.frame(element)
            # 현재 페이지의 html 코드를 불러옵니다.
            html = driver2.page_source
            # BS로 html 코드 파싱
            soup = BeautifulSoup(html, "html.parser")
    
            # 날짜 검색
            date2 = soup.select("div > span.se_publishDate.pcol2")
            
            # 본문 검색
            base2 = soup.select("div.se-module.se-module-text > p")

            # 날짜만 추출
            date_text = date2[0].text.strip()
            # print(date_text)
            f_nblog.write(date_text + '\n')

            # 본문만 추출
            for i in base2:
                con_text = i.text.strip()
                # print(con_text)
                f_nblog.write(con_text + '\n')
                
            # print('\n' + '=' * 50 + '\n')
            f_nblog.write('\n' + '=' * 50 + '\n')

        except Exception as e:
            print('iframe을 찾을 수 없습니다.', e)

    f_nblog.close() # 텍스트를 파일에 저장하고 닫음

# 함수 사용 예시
# naver_blog("김예지선수", 1)



# 11. (웹스크래핑 8) 네이버 쇼핑 데이터 수집 함수
import urllib.request  # 웹요청 모듈 
from bs4 import BeautifulSoup  # html 파싱 모듈 
from selenium import webdriver  # 브라우저 제어 모듈 
from selenium.webdriver.chrome.service import Service  # 드라이버 관리 모듈 
from selenium.webdriver.common.by import By  # 요소 탐색 모듈 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time  # 대기 시간 정해주는 모듈

from webdriver_manager.chrome import ChromeDriverManager  # 크롬 봇 자동설치 모듈

def naver_shopping(keyword, n):

    # 크롬 로봇 드라이버의 위치를 지정
    chrome_options =  Options()
    # service = Service('C:\\data\\chromedriver-win32\\chromedriver.exe')
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    # 크롬 드라이버의 위치 지정 후 driver 객체 생성
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    text1 = urllib.parse.quote(keyword)

    list_name = []   # 상품명
    list_price = []  # 상품가격
    list_date = []   # 등록일

    for i in range(1, 1 + n):
        list_url = f'https://search.shopping.naver.com/search/all?adQuery={text1}&origQuery={text1}&pagingIndex={i}&pagingSize=40&productSet=total&query={text1}&sort=rel&timestamp=&viewType=list'
        
        # 크롬 로봇에 웹페이지를 엽니다.
        driver.get(list_url)

        # 크롬 로봇에 마우스 스크롤을 아래로 내려서 전체 페이지가 다 보이게 합니다.
        for  i  in  range(1,6):
            driver.find_element(By.XPATH, value='//body').send_keys(Keys.END)
            time.sleep(0.5)

        # 보이는 웹페이지의 html 코드를 뷰티플 스프로 파싱합니다. 
        time.sleep(2) # 웹페이지가 다 뜰 수 있도록 기다려 줌 

        # 현재 페이지를 BS 로 파싱
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 광고 상품 정보가 있는 html 코드 부분으로 접근
        goods_list = soup.select('div.adProduct_item__1zC9h') # 상품명
        price_list = soup.select('strong.adProduct_price__9gODs > span.price > span.price_num__S2p_v > em')  # 가격
        reg_list = soup.select('div.adProduct_etc_box__UJJ90') # 등록일
        
        # 상품명, 가격, 등록일을 리스트에 각각 담아냄 
        for g, p, r in zip(goods_list, price_list, reg_list):
            price_text = p.text.strip()
            reg_list = r.text.strip().lstrip('리뷰,별점,만,천,백,십,일,구매,(,),1,2,3,4,5,6,7,8,9,0,.,,,찜').rstrip('.정보,신고하기,톡톡,수정요청').rstrip('.정보 ')
            # 상품명 
            # print(g.select_one('div.adProduct_title__amInq > a').get('title'), price_text,reg_list)
            # print('-' * 80)
            
        # 광고가 아닌 상품 정보가 있는 html 코드 부분으로 접근
        goods_list = soup.select('div.product_item__MDtDF') # 상품명
        price_list = soup.select('strong.product_price__52oO9 > span.price > span.price_num__S2p_v > em')  # 가격
        reg_list = soup.select('div.product_etc_box__ElfVA') # 등록일
        
        # 광고가 아닌 상품명, 가격, 등록일을 리스트에 각각 담아냄 
        for g, p, r in zip(goods_list, price_list, reg_list):
            product_name = g.select_one('div.product_title__Mmw2K > a').get('title')
            price_text = p.text.strip()
            reg_list = r.text.strip().lstrip('등록일,리뷰,별점,만,천,백,십,일,구매,(,),1,2,3,4,5,6,7,8,9,0,.,,,찜').rstrip('.정보,신고하기,톡톡,수정요청').rstrip('.정보 ')

            # 리스트에 추가하기
            list_name.append(product_name)
            list_price.append(price_text)
            list_date.append(reg_list)

    # 판다스 데이터 프레임 생성
    df = pd.DataFrame({'상품명' : list_name,
                       '가격' : list_price,
                       '등록일' : list_date})

    # csv 파일로 저장
    df.to_csv("c:\\data\\naver_shopping.csv", encoding="utf8", index=False)
    print("성공적으로 c:\\data\\naver_shopping.csv 가 저장되었습니다.")

# naver_shopping('그릭 요거트', 2)



# 12. (웹스크래핑 9) 쿠팡 데이터 수집 함수
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_coupang_data(keyword, pages):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Accept-Language": "ko-KR, ko;q=0.9, en-US;q=0.8, en;q=0.7",
        "Referer": "https://www.coupang.com/"
    }
    list_name = []
    list_price = []
    list_review = []
    list_star = []
    list_ad = []
    list_rank = []
    list_url = []

    for page in range(1, pages + 1):
        search_url = f"https://www.coupang.com/np/search?q={keyword}&channel=user&page={page}"
        response = requests.get(search_url, headers=headers)
        # print(response)

        if response.status_code == 200: # 사이트 접속이 정상이면
            soup = BeautifulSoup(response.text, 'html.parser')
            goods_list = soup.select('ul.search-product-list > li')
            # print(goods_list)

            for item in goods_list:
                # 상품명 가져오기
                item_name = item.select_one('dl > dd > div > div.name')
                if item_name:
                    list_name.append(item_name.text.strip())
                else:
                    list_name.append('')
                    
                # 상품 가격 가져오기
                item_price = item.select_one('strong.price-value')
                if item_price:
                    list_price.append(item_price.text.strip())
                else:
                    list_price.append('')

                # 리뷰수 가져오기
                descriptions_inner = item.select_one('div.descriptions-inner')
                # 이 안에 리뷰수도 있고 별점도 있기 때문에 이걸 먼저 만들어 준 후
                # 이 경로 밑에 리뷰수와 별점의 태그 경로를 적어서 descriptions_inner 공간 안의 데이터를 가져온다
                if descriptions_inner and descriptions_inner.select_one('div.other-info'):
                    item_review = descriptions_inner.select_one('span.rating-total-count')
                    if item_review:
                        list_review.append(item_review.text.strip('()'))
                    else:
                        list_review.append('0')
                # if 문을 두번 작성하였으므로 겉 if 문도 else를 적어줌
                else:
                    list_review.append('0')

                # 별점 가져오기
                if descriptions_inner and descriptions_inner.select_one('div.other-info'):
                    item_star = descriptions_inner.select_one('em.rating')
                    if item_star:
                        list_star.append(item_star.text.strip())
                    else:
                        list_star.append('0')

                else:
                    list_star.append('0')

                # 광고 상품 여부 가져오기
                if descriptions_inner and descriptions_inner.select_one('div.other-info'):
                    item_ad = descriptions_inner.select_one('span.ad-badge-text')
                    if item_ad:
                        list_ad.append('O')
                    else:
                        list_ad.append('X')

                else:
                    list_ad.append('X')

                # 순위 가져오기
                item_rank = item.select_one('span[class^="number no-"]') # span의 클래스 이름이 " " 이 안에 해당되는 것을 모두 경로로 지정
                # 순위는 descriptions_inner 안에 없으므로 상품명 처럼 item.select_one으로 경로지정
                if item_rank:
                    list_rank.append(item_rank.text.strip())
                else:
                    list_rank.append('') # 순위가 없는 상품은 NA로 넣기

                # 상품의 상세 URL 가져오기
                item_url = item.select_one('a.search-product-link')
                if item_url:
                    list_url.append("https://www.coupang.com" + item_url['href'])
                else:
                    list_url.append('')

    # 판다스 데이터 프레임 만들기
    df = pd.DataFrame({'상품명' : list_name,
                       '가격' : list_price,
                       '리뷰수' : list_review,
                       '별점' : list_star,
                       '광고 상품 여부' : list_ad,
                       '순위' : list_rank})

    # df 데이터 프레임의 결과를 csv 파일로 내리기
    df.to_csv("c:\\data\\coupang.csv", encoding="utf8", index=False)
    print('성공적으로 c:\\data\\coupang.csv 가 저장되었습니다.')

# get_coupang_data('그릭 요거트', 2)


# 13. (웹스크래핑 10) 네이버 이미지 데이터 수집 함수
def get_naver_image(keyword):
    # 모듈 불러오기
    import urllib.request
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 
    import time
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service 
    
    # 크롬 드라이버의 위치 지정 후 driver 객체 생성
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # 네이버 이미지 검색 페이지로 이동
    driver.get("https://search.naver.com/search.naver?where=image&sm=stb_nmr&")
    
    time.sleep(5)
    
    # 검색창에 검색 키워드를 입력
    search = driver.find_element(By.XPATH, '//*[@id="nx_query"]') # 검색창 영역 클릭하고 개발자모드에서 오른쪽 클릭 Copy - Copy XPath 로 경로 복사
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)
    
    # 페이지를 아래로 스크롤하여 더 많은 이미지를 로드
    for i in range(1, 20):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
        time.sleep(5)
    
    # 현재 페이지의 HTML 소스 코드를 가져와 파싱
    html = driver.page_source  
    soup = BeautifulSoup(html, "lxml")
    
    # 이미지 태그를 찾고 이미지 URL을 수집
    params_n = []
    imgList = soup.find_all("div", class_=["image_tile_bx", "_fe_image_viewer_focus_target"])
    for i in imgList:
        img_tag = i.find("img")  # 'img' 태그 찾기
        if img_tag:
            img_url = img_tag.get("data-src", img_tag.get("src"))  # 이미지 URL 가져오기
            if img_url:
                params_n.append(img_url)
    
    # 수집한 이미지 URL을 사용하여 이미지를 다운로드
    for idx, p in enumerate(params_n, 1):
        urllib.request.urlretrieve(p, "c:\\data_image5\\" + str(idx) + ".jpg")
    
    # 작업 완료 후 브라우저 닫기
    driver.quit()

# 함수 실행 예시
# get_naver_image('말티푸')



# 14. (웹스크래핑 11) 다음 이미지 데이터 수집 함수
def get_daum_image(keyword):
    # 모듈 불러오기
    import urllib.request
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 
    import time
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service 
    
    # 크롬 드라이버의 위치 지정 후 driver 객체 생성
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # 다음 이미지 검색 페이지로 이동
    driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=")
    
    time.sleep(5)
    
    # 검색창에 검색 키워드를 입력
    search = driver.find_element(By.XPATH, '//*[@id="q"]') # 검색창 영역 클릭하고 개발자모드에서 오른쪽 클릭 Copy - Copy XPath 로 경로 복사
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)
    
    # 페이지를 아래로 스크롤하여 더 많은 이미지를 로드
    for i in range(1, 20):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
        time.sleep(5)
    
    # 현재 페이지의 HTML 소스 코드를 가져와 파싱
    html = driver.page_source  
    soup = BeautifulSoup(html, "lxml")
    
    # 이미지 태그를 찾고 이미지 URL을 수집
    params_d = []
    imgList = soup.find_all("div", class_=["wrap_thumb"])
    for i in imgList:
        img_tag = i.find("img")  # 'img' 태그 찾기
        if img_tag:
            img_url = img_tag.get("data-src", img_tag.get("src"))  # 이미지 URL 가져오기
            if img_url:
                params_d.append(img_url)
    
    # 수집한 이미지 URL을 사용하여 이미지를 다운로드
    for idx, p in enumerate(params_d, 1):
        urllib.request.urlretrieve(p, "c:\\data_image6\\" + str(idx) + ".jpg")
    
    # 작업 완료 후 브라우저 닫기
    driver.quit()

# 함수 실행 예시
# get_daum_image('슈나우저')



# 15. (웹스크래핑 12) 구글 이미지 데이터 수집 함수
def get_google_image(keyword):
    # 1. 모듈 임포트
    import urllib.request
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service 
    from webdriver_manager.chrome import ChromeDriverManager
    
    # 2. 크롬 드라이버의 위치 지정후 driver 객체를 생성
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # 3.구글 이미지 검색 페이지로 이동
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ei=l1AdWbegOcra8QXvtr-4Cw&ved=0EKouCBUoAQ")
    
    # 4. 검색창 객체 생성
    search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    
    # 5.검색어 입력
    name = keyword
    search.send_keys(name)
    
    # 6.엔터 입력
    search.submit()
    
    # 7.스크롤을 아래로 내려서 이미지를 더 로드
    for i in range(1, 9):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
        time.sleep(10)
    
    # 8. 결과 더보기 클릭 (버튼이 있는 경우에만)
    try:
        driver.find_element(By.XPATH, "//*[@class='mye4qd']").click()
        # 결과 더보기를 눌렀으니 마우스를 다시 아래로 내림
        for i in range(1, 9):
            driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
            time.sleep(10)
    except Exception as e:
        print("결과 더보기 버튼이 없습니다. 다음 단계로 넘어갑니다.")
    
    # 9. 현재 페이지의 HTML 코드를 가져옴
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    
    # 10. 이미지 URL들을 params 리스트에 담기
    params_g = []
    imgList = soup.find_all("g-img", class_="mNsIhb")
    
    for g_img in imgList:
        img_tag = g_img.find("img")  # g-img 태그 내의 img 태그를 찾음
        if img_tag:
            img_url = img_tag.get("src", img_tag.get("data-src"))
            params_g.append(img_url)
    
    # 결과 확인
    #print(params_g)
    
    
    # 11. 이미지들을 로컬 디렉토리에 저장
    for idx, p in enumerate(params_g, 1):
        if p:
            urllib.request.urlretrieve(p, "c:\\data_image2\\" + str(idx) + ".jpg")
        else:
            print(f"이미지 {idx}는 다운로드할 수 없습니다.")

# 함수 활용 예시
# get_google_image('알리오올리오')


# 16. (웹스크래핑 13) 빙 이미지 데이터 수집 함수
def bing_image_get(keyword):
    # 필요한 모듈 임포트
    import urllib.request
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 
    import time
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service 
    
    # 크롬 드라이버의 위치 지정 후 driver 객체 생성
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # 빙이미지 검색 페이지로 이동
    driver.get("https://www.bing.com/images/feed?form=HDRSC2")
    
    time.sleep(5)
    
    # 검색창에 검색 키워드를 입력
    search = driver.find_element(By.XPATH, "//*[@class='b_searchbox ']")
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)
    
    # 이미지가 불러와질때까지 대기 하는 시간 지정
    time.sleep(2)
    
    # 페이지를 아래로 스크롤하여 더 많은 이미지를 로드
    for i in range(1, 10):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
        time.sleep(5)
    
    try:
        # 이미지 더보기 버튼 클릭
        show_more_button = driver.find_element(By.XPATH, "//a[contains(@class,'btn_seemore')]")
        show_more_button.click()
    except  Exceptions  as  e:
        print("결과 더보기 버튼이 없습니다. 다음 단계로 넘어갑니다.")
        print(f'오류:{e}')
    
    # 페이지를 아래로 스크롤하여 더 많은 이미지를 로드
    for i in range(1, 10):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
        time.sleep(5)
    
    # 현재 페이지의 HTML 소스 코드를 가져와 파싱
    html = driver.page_source  
    soup = BeautifulSoup(html, "lxml")
    #print(soup)
    
    # 이미지 태그를 찾고 이미지 URL을 수집
    params = []
    imgList = soup.find_all('img', class_='mimg')
    for  i  in  imgList:
        params.append( i.get('src'))
    
    # 수집한 이미지 URL을 사용하여 이미지를 다운로드
    for idx, p in enumerate(params, 1):
        urllib.request.urlretrieve(p, "c:\\data_image4\\" + str(idx) + ".jpg")
    
    # 작업 완료 후 브라우저 닫기
    driver.quit()

# 함수 활용 예시
# bing_image_get('경복궁')



# 17. (웹스크래핑 14) 유튜브 댓글 데이터 수집 함수
# 모듈 불러오기
import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd

# 키워드를 검색하면 해당 영상의 상세 url을 가져오는 함수 생성
def get_url_youtube(keyword):
    titles = [] # 유튜브 영상 제목을 담을 리스트
    urls = []   # 키워드를 넣었을 때 나오는 모든 영상들의 url 주소를 담기위한 리스트

    # 입력한 키워드를 컴퓨터가 알아들을 수 있는 언어로 인코딩 실시
    search_keyword_encode = requests.utils.quote(keyword)

    # 유튜브에서 해당 키워드의 영상 리스트를 찾을 수 있는 url을 만들어서 url 변수에 입력
    url = "https://www.youtube.com/results?search_query=" + search_keyword_encode

    # 크롬 봇 위치 지정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # 크롬 봇이 url을 직접 열게 함
    driver.get(url)

    # 키워드로 받아온 영상 리스트 웹페이지의 처음부터 맨 마지막까지의 높이를 추출
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    # print(last_page_height) # 페이지의 총 높이 : 8804

    while True: # 아래의 실행문을 무한히 반복
        # 마우스 스크롤을 끝까지 내리게 함
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        time.sleep(3)

        # 키워드로 받아온 영상 리스트 웹페이지의 처음부터 맨 마지막까지의 높이를 추출
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        
        # 지금의 높이가 웹페이지의 끝이라면
        if new_page_height == last_page_height: # last_page_height 는 위에서 구한 키워드 검색의 총 길이
            break # 무한 루프 종료해라

        # new_page_height 의 값을 last_page_height 에 할당
        last_page_height = new_page_height

    html_source = driver.page_source # 페이지의 html 소스를 html_source 에 담음
    driver.quit() # 브라우저 닫기

    # html 코드를 뷰티풀 스프로 파싱
    soup = BeautifulSoup(html_source, 'html.parser')

    # 영상 제목과 상세 url 가져오기
    datas = soup.select("a#video-title")
    for i in datas:
        title = i.get("title")
        url = "https://www.youtube.com/" + i.get("href")
        if title:
            titles.append(title)
            urls.append(url)

    return titles, urls

# 상세 url을 넣고 html을 받아오는 코드
def youtube_page_html_source(keyword):
    
    title, url = get_url_youtube(keyword)
    
    html_sources = [] # html 코드를 저장하기 위한 리스트를 생성

    # 크롬 봇 위치 지정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    for i in range(0, 2): # 전체 url(위 코드 기준 596개) 말고 2개의 url 만 가져옴
        # 크롬 봇이 url을 직접 열게 함
        driver.get(url[i])
    
        # 키워드로 받아온 영상 리스트 웹페이지의 처음부터 맨 마지막까지의 높이를 추출
        last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        # print(last_page_height) # 페이지의 총 높이 : 8804
    
        while True: # 아래의 실행문을 무한히 반복
            # 마우스 스크롤을 끝까지 내리게 함
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    
            time.sleep(3)
    
            # 키워드로 받아온 영상 리스트 웹페이지의 처음부터 맨 마지막까지의 높이를 추출
            new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
            
            # 지금의 높이가 웹페이지의 끝이라면
            if new_page_height == last_page_height: # last_page_height 는 위에서 구한 키워드 검색의 총 길이
                break # 무한 루프 종료해라
    
            # new_page_height 의 값을 last_page_height 에 할당
            last_page_height = new_page_height

        time.sleep(5)
        html_source = driver.page_source # 페이지의 html 소스를 html_source 에 담음
        time.sleep(5)

        html_sources.append(html_source)
    print('OK')

    driver.quit() # 브라우저 닫음
        
    return html_sources

# 글쓴이와 댓글 가져오는 함수
def get_comments(html_sources):
    # 상세 url 마다 담길 뎃글의 데이터 프레임을 위한 리스트
    my_dataframes = []
    cnt = 0 
    while cnt < len(html_sources):
        html = html_sources[cnt]
        cnt += 1
        soup = BeautifulSoup(html, 'lxml')

        # 글쓴이 가져오기 
        writer = soup.select('div#header-author > h3 > a > span')
        # 댓글 가져오기
        comments = soup.select('yt-attributed-string#content-text > span')

        # 글쓴이와 댓글의 길이가 다를 경우에 예외처리 
        min_len = min( len(writer), len(comments) )

        if min_len == 0:
            continue

        # 글쓴이 데이터를 writer2 리스트에 추가합니다. 
        writer2 = []
        for i in range(min_len):
            str_temp = str(writer[i].text).strip()  
            writer2.append(str_temp)

        # 댓글 데이터를 comments2 리스트에 추가합니다. 
        comments2 = []
        for i in range(min_len):
            str_temp2 = str(comments[i].text).strip()
            comments2.append(str_temp2)

        # 글쓴이와 댓글 데이터로 판다스 데이터 프레임을 생성
        pd_data = {"id" : writer2, "comment" : comments2}
        pd_df = pd.DataFrame(pd_data)

        # 판다스 데이터 프레임을 my_dataframes 리스트에 append 시킴
        if not pd_df.empty:
            my_dataframes.append(pd_df)
            
    # 글쓴이와 댓글을 가지고 판다스 데이터 프레임을 생성하기
    if my_dataframes:
        comments_df = pd.concat( my_dataframes, ignore_index=True)
    else:
        comments_df = pd.DataFrame(columns=['id','comment'])

    return  comments_df

# 키워드를 입력해서 해당 키워드의 유튜브 댓글이 수집되는 함수
def scroll_youtube(keyword):

    k = youtube_page_html_source(keyword)
    my_data = get_comments(k)
    my_data.to_csv(f'c:\\data\\{keyword}_youtube.csv', index=False, encoding="utf-8")

# 함수 활용 예시
# scroll_youtube('부산맛집')



# 18. (데이터 시각화 3) 중앙일보 키워드 언급 시각화 및 최다 언급 기사 날짜 출력 함수
def relation_word_ja(keyword, num):
    import ldg
    ldg.ja(keyword, num)
    
    import pandas as pd
    from collections import Counter # 텍스트 데이터에서 단어를 카운트하는 모듈
    
    # 텍스트 파일 열기 (with 절을 써서 열면 파이썬이 알아서 파일을 닫는다.)
    with open("c:\\data\\ja.txt", "r", encoding="utf-8") as file:
        text = file.read()
    
    # 텍스트를 엔터 기준으로 분리함
    lines = text.split('\n')
    
    # Counter 모듈을 객체화 합니다.
    date_counts = Counter()
    current_date = None
    
    # 2024년으로 시작하는 라인만 추출 (기사 날짜와 제목을 추출)
    for line in lines:
        if line.startswith('2024-'): # startswith 함수는 sql like 처럼 '입력값'으로 시작하는 요소를 추출할 수 있음
            current_date = line[:10] # 날짜만 추출
    
        if current_date and keyword in line: # 인공지능을 포함한다면
            date_counts[current_date] += line.count(keyword)
    
    # 판다스 데이터 프레임으로 구성
    df = pd.DataFrame(list(date_counts.items()), columns=['date', 'count'])
    
    # 날짜를 datetime 형식으로 변환
    df['date'] = pd.to_datetime(df['date'])
    
    # 모듈 불러오기
    import matplotlib.pyplot as plt
    from matplotlib import font_manager, rc # 한글 폰트 깨지지 않게하는 모듈
    
    # 한글 폰트 설정
    plt.rcParams['font.family'] = 'Malgun Gothic'
    
    # 시각화 하기
    plt.figure(figsize = (10, 6)) # 가로 10, 세로 6으로 그래프 사이즈 설정
    plt.plot(df['date'], df['count'], marker='o', color='b')
    plt.fill_between(df['date'], df['count'], color='gray', alpha=0.3)
    
    # 피크값의 날짜를 가져오기 
    peak_indices = df[df['count'] == df['count'].max() ].index
    for  i  in  peak_indices:
        plt.text(df['date'][i], df['count'][i] + 0.5, df['date'][i].strftime('%Y-%m-%d'),
                 color='red', fontsize=12)
    
    plt.title(f'날짜별 {keyword} 언급량')
    plt.xlabel('날짜')
    plt.ylabel('언급량')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

# 함수 활용 예시
# relation_word_ja('한파', 3)



# 19. (데이터 시각화 4) 네이버 블로그 키워드 워드 클라우드 출력 함수
def related_wordcloud(location, keyword, num):

    import ldg
    ldg.naver_blog(keyword, num)

    # !pip install konlpy
    
    from collections import Counter # 단어의 건수를 체크하기 위한 모듈
    from konlpy.tag import Okt # 한글 형태소 분석 모듈
    
    # 분석할 데이터 불러오기
    with open(location, 'r', encoding='utf8') as f:
        text = f.read()
    
    # 키워드와 연관이 높은 단어 추출
    related_words = [] # 결과 담을 빈 리스트 생성
    okt = Okt()
    for sentence in text.split('.'): # .을 기준으로 분리한다는 것은 문장 단위로 분리한다는 의미
        if keyword in sentence: # 키워드가 포함된 문장인 경우에만 단어 추출
            nouns = okt.nouns(sentence) # 문장에서 명사 추출
            for i in nouns:
                if len(i) > 1 : # 철자가 1개보다 큰 명사이면
                    related_words.append(i)
    
    # print(related_words) # 키워드를 포함하는 문장에 들어간 단어들
    
    # related_words 에서 자주 나오는 단어들만 추출
    if related_words:
        top_words = Counter(related_words).most_common(100) # 출현된 단어들 중 상위 100개 단어 추출
        # print(top_words) # 출력되는 거 확인 후 다음 코드 작성을 위해 주석으로 막기
    
    else:
        print(f'{keyword}과(와) 연관된 단어가 없습니다.')
    
    # top_words 리스트를 딕셔너리로 변환하기
    dct = {'keyword' : [], 'cnt' : []}
    
    for key, value in top_words:
        # print(key, value)
        dct['keyword'].append(key)
        dct['cnt'].append(value)
    # print(dct)
    
    # 데이터 프레임으로 생성하기
    import pandas as pd
    df = pd.DataFrame(dct)
    df.columns = ['title', 'count']
    # df
    
    # 워드 클라우드를 그리기 위해 다시 딕셔너리 형태로 생성
    wc = df.set_index('title').to_dict()['count']
    # wc
    
    # 키워드와 연관성이 높은 단어들 중에서 빈도수 높은 단어만 빨간색, 나머지는 검정색으로 출력하기
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    
    # 사용자 정의 색상 함수
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        if word in top_10_words:
            return 'red' # 빈도수 상위 10개 단어를 빨간색으로
        else:
            return 'black'
    
    # 한글 안깨지게 하는 코드 
    from matplotlib import font_manager, rc
    font = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font)
    
    wordCloud = WordCloud(font_path = "c:/Windows/Fonts/malgun.ttf", # 폰트 지정
                          width = 1000, # 워드 클라우드의 너비 지정
                          height = 800, # 워드클라우드의 높이 지정
                          max_font_size=100, # 가장 빈도수가 높은 단어의 폰트 사이즈 지정
                          background_color = 'white' # 배경색 지정
                         ).generate_from_frequencies(wc) # 워드 클라우드 빈도수 지정
    
    top_10_words = { word for word, count in Counter(wc).most_common(10) }
    
    plt.imshow(wordCloud.recolor(color_func=color_func), interpolation='bilinear')
    plt.axis('off')
    plt.show()

# 함수 활용 예시
# related_wordcloud('c:\\data\\naver_blog.txt', '봄옷', 2)



# 20. (데이터 시각화 5) 수집한 텍스트 데이터를 기반으로 긍정/부정 단어를 출력하고 워드클라우드를 생성하는 함수
def emotion(location):
    # 텍스트 파일 3개 (데이터 수집 파일, 긍정 단어 모음, 부정 단어 모음) 불러오기
    origin_text = open(location, encoding="utf8")
    positive = open("c:\\data\\pos_pol_word.txt", encoding="utf8")
    negative = open("c:\\data\\neg_pol_word.txt", encoding="utf8")

    # 위의 텍스트 파일 3개를 엔터 기준으로 구분해서 변수에 담기
    origin = origin_text.read() # orgin_text 를 문자형 변수 orgin 에 담음
    pos = positive.read().split('\n') # 긍정단어를 엔터로 구분해서 리스트로 구성
    neg = negative.read().split('\n') # 부정단어를 엔터로 구분해서 리스트로 구성

    # pos 와 neg 리스트에서 결측치를 제거함
    pos = list(filter(lambda x : x, pos))
    neg = list(filter(lambda x : x, neg))

    # 한자리수 단어는 삭제
    pos1 = list(filter(lambda x : True if len(x) > 1 else False, pos))
    neg1 = list(filter(lambda x : True if len(x) > 1 else False, neg))

    # 분석하고자하는 텍스트에 나오는 긍정 단어와 부정단어를 저장할 csv 파일을 생성
    f2 = open("c:\\data\\origin_pos.csv", "w", encoding="utf8")
    f3 = open("c:\\data\\origin_neg.csv", "w", encoding="utf8")

    # 긍정단어에서 제외시키고 싶은 단어들을 제외 시킴 (의미 없는 이모티콘 등등)
    pos1.remove('ㅎㅎ')
    pos1.remove('^^')
    pos1.remove('이벤트')
    pos1.remove('어진')

    # 부정단어에서 제외시키고 싶은 단어들을 제외 시킴 (의미 없는 이모티콘 등등)

    # 원본 데이터에서 긍정단어가 얼마나 포함되었는지 확인하고 내리는 코드
    for i in pos1:
        if i in origin:
            f2.write(i + ',' + str(origin.count(i)) + '\n')

    # 원본 데이터에서 부정단어가 얼마나 포함되었는지 확인하고 내리는 코드
    for j in neg1:
        if j in origin:
            f3.write(j + ',' + str(origin.count(j)) + '\n')

    f2.close()
    f3.close()

    # 위에서 생성한 csv 파일을 판다스 데이터 프레임으로 만들어서 출력하는 코드
    import pandas as pd

    pd.set_option('display.max_rows', None) # 결과 출력시 중간 생략하지 않고 다 출력

    origin_df_pos = pd.read_csv("c:\\data\\origin_pos.csv", header=None)
    origin_df_neg = pd.read_csv("c:\\data\\origin_neg.csv", header=None)
    
    origin_df_pos.columns = ['긍정 WORD', '긍정 CNT'] # 컬럼명 생성
    origin_df_neg.columns = ['부정 WORD', '부정 CNT'] # 컬럼명 생성
    
    origin_df_pos['긍정 RANK'] = origin_df_pos['긍정 CNT'].rank(method='dense', ascending=False).astype(int)
    origin_df_neg['부정 RANK'] = origin_df_neg['부정 CNT'].rank(method='dense', ascending=False).astype(int)
    
    a_pos = origin_df_pos[:].sort_values(by=['긍정 RANK']).head(20) # 상위 20개만 출력
    a_neg = origin_df_neg[:].sort_values(by=['부정 RANK']).head(20) # 상위 20개만 출력

    # a_pos 와 a_neg 데이터 프레임을 각각 csv 파일로 저장하기
    a_pos.to_csv("c:\\data\\a_pos.csv", index=False, encoding='utf-8-sig')
    a_neg.to_csv("c:\\data\\a_neg.csv", index=False, encoding='utf-8-sig')

    # 긍정 단어와 부정 단어 한 데이터 프레임으로 합치기
    combined_df = pd.concat([a_pos.reset_index(drop=True), a_neg.reset_index(drop=True)], axis=1)

    # 위에 생성된 csv 파일로 워드클라우드 그리기

    # 필요한 모듈 불러오기
    import pandas as pd
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    
    # csv 파일 불러오기
    file_path_pos = "c:\\data\\a_pos.csv" # 긍정단어 불러오기
    file_path_neg = "c:\\data\\a_neg.csv" # 부정단어 불러오기
    df_pos = pd.read_csv(file_path_pos) # 긍.단 df 생성
    df_neg = pd.read_csv(file_path_neg) # 부.단 df 생성
    
    # 긍정 단어와 부정 단어의 word와 cnt를 사전 타입으로 변환
    word_freq_pos = dict(zip(df_pos['긍정 WORD'], df_pos['긍정 CNT']))
    word_freq_neg = dict(zip(df_neg['부정 WORD'], df_neg['부정 CNT']))
    
    # 긍정/부정별 상위 7개의 단어를 추출
    top_pos_words = df_pos.nlargest(7, '긍정 CNT')['긍정 WORD'].tolist()
    top_neg_words = df_neg.nlargest(7, '부정 CNT')['부정 WORD'].tolist()
    
    # 주요 단어 설정
    highlight_words = set(top_pos_words + top_neg_words)
    # print(highlight_words)
    
    # 긍정 색상 설정 함수
    def color_func_pos(word, font_size, position, orientation, random_state=None, **kwargs):
        return 'darkblue' if word in highlight_words else 'grey'
    
    # 부정 색상 설정 함수
    def color_func_neg(word, font_size, position, orientation, random_state=None, **kwargs):
        return 'darkred' if word in highlight_words else 'grey'
    
    # 긍정 워드클라우드 생성
    wordcloud_pos = WordCloud(font_path = 'c:\\windows\\Fonts\\malgun.ttf',
                              width=800,
                              height=400,
                              background_color='white',
                              color_func=color_func_pos
                             ).generate_from_frequencies(word_freq_pos)
    
    # 부정 워드클라우드 생성
    wordcloud_neg = WordCloud(font_path = 'c:\\windows\\Fonts\\malgun.ttf',
                              width=800,
                              height=400,
                              background_color='white',
                              color_func=color_func_neg
                             ).generate_from_frequencies(word_freq_neg)
    
    # 두 워드클라우드를 나란히 시각화
    fig, axes = plt.subplots(1, 2, figsize=(20, 10)) # 1행 2열
    
    # 첫번째 워드 클라우드(긍정)
    axes[0].imshow(wordcloud_pos, interpolation='bilinear')
    axes[0].set_title('Positive word cloud', fontsize=20)
    axes[0].axis('off')
    
    # 두번째 워드 클라우드(부정)
    axes[1].imshow(wordcloud_neg, interpolation='bilinear')
    axes[1].set_title('Negative word cloud', fontsize=20)
    axes[1].axis('off')

    return combined_df
    return plt.show()

# 함수 활용 예시
# emotion('c:\\data\\article.txt')



# 21. (데이터 시각화 6) 수집하여 종합한 텍스트 파일에서 두 키워드의 언급량을 라인그래프로 비교한 함수
def relation_word_comp(location, keyword1, keyword2):

    # 비교 분석 함수 생성
    
    # 모듈 불러오기
    import pandas as pd
    import matplotlib.pyplot as plt
    from collections import Counter
    
    # 비교 분석할 텍스트 파일 열기
    with open(location, "r", encoding = "utf-8") as file:
        text = file.read()
    
    # 텍스트를 엔터 기준으로 분리하기
    lines = text.split('\n')
    # print(lines[:100])
    
    # Counter 모듈 객체화하기
    date_counts1 = Counter()
    date_counts2 = Counter()
    current_date = None
    
    # 2023년 또는 2024년으로 시작하는 라인만 추출 (기사날짜와 제목을 추출)
    for line in lines:
        if line.startswith('2023-') or line.startswith('2024-'):
            current_date = line[:10] # 날짜만 추출
            # print(current_date)
        if current_date:
            if keyword1 in line: # keyword1 라는 단어를 포함한다면
                date_counts1[current_date] += line.count(keyword1)
    
            if keyword2 in line: # keyword2 라는 단어를 포함한다면
                date_counts2[current_date] += line.count(keyword2)
    
    # 판다스 데이터 프레임 생성
    df1 = pd.DataFrame(list(date_counts1.items()), columns = ['date', f'{keyword1} CNT'])
    df2 = pd.DataFrame(list(date_counts2.items()), columns = ['date', f'{keyword2} CNT'])
    
    # 날짜를 datetime 형식으로 변환
    df1['date'] = pd.to_datetime(df1['date'])
    df2['date'] = pd.to_datetime(df2['date'])
    
    # 두 데이터 프레임을 날짜 기준으로 병합하기
    df = pd.merge(df1, df2, on = 'date', how = 'outer').fillna(0)
    
    # 2024년 4월 1일부터 6월 30일 까지 데이터만 필터링
    start_date = pd.Timestamp('2024-04-01')
    end_date = pd.Timestamp('2024-06-30')
    
    # 문법 : df[컬럼선택][검색조건]
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    
    # 시각화 하기
    plt.rcParams['font.family'] = 'Malgun Gothic' # 한글 안 깨지게 함
    plt.figure(figsize = (16, 8))
    plt.plot(df['date'], df[f'{keyword1} CNT'], marker='o', color='b', label=keyword1)
    plt.plot(df['date'], df[f'{keyword2} CNT'], marker='o', color='orange', label=keyword2)
    plt.fill_between(df['date'], df[f'{keyword1} CNT'], color='blue', alpha=0.1)
    plt.fill_between(df['date'], df[f'{keyword2} CNT'], color='orange', alpha=0.1)
    
    # 첫번째 그래프 피크 값의 날짜를 표시
    for keyword in [keyword1, keyword2]:
        peak_indices = df[df[f'{keyword1} CNT'] == df[f'{keyword1} CNT'].max()].index
        for i in peak_indices:
            plt.text(df['date'][i], df[f'{keyword1} CNT'][i] + 1, df['date'][i].strftime('%Y-%m-%d'),
                     color = 'red', fontsize = 14)
    
    # 두번째 그래프 피크 값의 날짜를 표시
    for keyword in [keyword1, keyword2]:
        peak_indices = df[df[f'{keyword2} CNT'] == df[f'{keyword2} CNT'].max()].index
        for i in peak_indices:
            plt.text(df['date'][i], df[f'{keyword2} CNT'][i] + 1, df['date'][i].strftime('%Y-%m-%d'),
                     color = 'red', fontsize = 14)
    
    plt.title(f'날짜별 {keyword1}와 {keyword2} 언급량 비교', fontsize = 18)
    plt.xlabel('날짜', fontsize = 14)
    plt.ylabel('언급량', fontsize = 14)
    plt.legend(fontsize = 14)
    plt.grid(True)

# 함수 활용 예시
# relation_word_comp('c:\\data\\ja_new_ive.txt', '뉴진스', '아이브')



# (하단 인덱스) ldg.py 스크립트 맨아래에 아래의 코드를 추가한다.

if __name__ != "__main__":
    print("ldg 모듈이 임포트 되었습니다.")
    print("함수 목록")
    print("01. wrap : 문자열을 특정 문자로 감싸는 함수")
    print("02. plot_bar_graph : 막대 그래프 그리는 함수")
    print("03. plot_pie_graph : 원형 그래프 그리는 함수")
    print("04. hankook(키워드, 페이지수) : 한국일보 데이터 수집")
    print("05. donga(키워드, 페이지수) : 동아일보 데이터 수집")
    print("06. ja(키워드, 페이지수) : 중앙일보 데이터 수집")
    print("07. hani(키워드, 페이지수) : 한겨레신문 데이터 수집")
    print("08. km(키워드, 페이지수) : 국민일보 데이터 수집")
    print("09. chosun(키워드, 페이지수) : 조선일보 데이터 수집")
    print("10. naver_blog(키워드, 페이지수) : 네이버 블로그 데이터 수집")
    print("11. naver_shopping(키워드, 페이지수) : 네이버 쇼핑 데이터 수집")
    print("12. get_coupang_data(키워드, 페이지수) : 쿠팡 데이터 수집")
    print("13. get_naver_image(키워드) : 네이버 이미지 데이터 수집")
    print("14. get_daum_image(키워드) : 다음 이미지 데이터 수집")
    print("15. get_google_image(키워드) : 구글 이미지 데이터 수집")
    print("16. get_bing_image(키워드) : 빙 이미지 데이터 수집")
    print("17. scroll_youtube(키워드) : 유튜브 댓글 데이터 수집")
    print("18. relation_word_ja(키워드, 페이지수) : 중앙일보 키워드 언급 시각화 및 최다 언급 기사 날짜 출력 함수")
    print("19. related_wordcloud(파일경로, 키워드) : 네이버 블로그 키워드 연관 워드클라우드 생성 함수")
    print("20. emotion(파일경로) : 긍정/부정 워드클라우드 생성 함수")
    print("21. relation_word_comp(파일경로, 키워드1, 키워드2) : 수집하여 종합한 텍스트 파일에 두 키워드의 언급량을 라인그래프로 비교한 함수")
else:
    print("ldg.py 가 직접 실행되었습니다.")
