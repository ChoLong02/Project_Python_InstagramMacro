# * chapter01_crawl.py
# * : requests로 크롤링하는 부분을 모듈화 하고, import해서 사용하는 코드
# *

from libs.crawler import crawl

# 수집하고 싶은 인스타그램의 #해시태그 페이지 URL주소
url = 'https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%A6%88%EC%9B%90/'

pageString = crawl(url)
print(pageString)