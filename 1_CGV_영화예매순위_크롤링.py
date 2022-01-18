import urllib.request as req
from bs4 import BeautifulSoup  # pip install bs4

# 서버한테 HTML 코드 받기
code = req.urlopen("http://www.cgv.co.kr/movies/?lt=1&ft=1")
# print(code.read())

# HTML 코드 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

# 원하는 요소 찾게하기
# <CSS 선택자> : 기호를 이용해서 내가 원하는 요소를 알려줌
# - "." : 속성명이 class
# - "#" : 속성명이 id
# - " > " : 자손
# - " " : 후손
# title = soup.select_one("ol div.box-contents > a > strong.title") # 요소 하나만 가져옴
title = soup.select("strong.title") # 요소 여러개 한번에 가져옴

# 요소의 내용 출력하기
for i in title:
    print(i.string) # 요소 내용 꺼내오기