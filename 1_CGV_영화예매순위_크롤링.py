import urllib.request as req
from bs4 import BeautifulSoup  # pip install bs4

# 서버한테 HTML 코드 받기
code = req.urlopen("http://www.cgv.co.kr/movies/")
# print(code.read())

# HTML 코드 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

# 원하는 요소 찾게하기
title = soup.select_one("strong.title")

# 요소의 내용 출력하기
print(title.string)