from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request  #이미지 url로 다운로드


driver = webdriver.Chrome('chromedriver.exe')



#구글 이미지 페이지 이동
driver.get('https://www.google.co.kr/imghp?hl=ko&ogbl')

#검색
e = driver.find_elements_by_class_name('gsfi')[1]
e.click()
time.sleep(2)
e.send_keys('엑소 수호') #검색어
e.send_keys(Keys.ENTER)
time.sleep(2)





#스크롤 최대로 내리기 & '결과 더보기 버튼 클릭' 해서 모든 이미지 로드하기

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight") #자바스크립트 코드를 실행해서 브라우저의 높이를 return한다.

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")        #0 ~ 브라우저의 최대 높이(끝까지) 스크롤을 내린다.

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")     #자바스크립트 코드를 실행해서 브라우저의 높이를 return한다.
    if new_height == last_height:               #만약 새로운 높이 == 이전 높이 ==> break :: 모든 스크롤을 내림
        try:
            #'결과 더보기'버튼을 만났을 때 클릭
            driver.find_element_by_css_selector('.mye4qd').click()
        except:
            #'결과 더보기'버튼이 없을 때 break
            break
    last_height = new_height
 



#이미지 크롤링

#사진 선택 (리스트 저장)
images=driver.find_elements_by_css_selector('.rg_i.Q4LuWd')

count=1
for image in images:

    try:
        #images[image]번째 사진 클릭
        image.click()

        #images[image]번째 사진 img URL 가져오기
        imgUrl = driver.find_element_by_xpath('/html/body/div[3]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute('src')
        time.sleep(2)

        # @특정 사이트 이미지 다운로드 에러 방지 (브라우저 인것 처럼 속이는 header 추가)@
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        #URL로 이미지 다운로드 
        #urllib.request.urlretrieve(imgUrl, str(count)+".jpg")
        urllib.request.urlretrieve(imgUrl,".\수호\\"+str(count)+".jpg")   #  .\폴더명\저장할이미지명.jpg   ==> 폴더를 지정해 그곳에 이미지를 다운로드 할 수 있다.

        count = count+1

    except:
        pass


driver.close()
