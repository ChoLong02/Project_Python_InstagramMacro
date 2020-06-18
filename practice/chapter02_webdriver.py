# * chapter02_webdriver.py
# * : Selenium의 Webdriver 사용방법(+Chrome Driver)
# *

from selenium import webdriver

# instagram 페이지에서 원하는 해쉬태그로 selenium 접속(+Chrome Driver)
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')

# https://www.instagram.com/explore/tags/아이즈원/
# URL 주소의 한글은 유니코드로 변환(한글이면 깨지는 경우가 있음)
url = 'https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%A6%88%EC%9B%90/'
driver.get(url)
# driver.close() # 실행 후 브라우저 종료

