from bs4 import BeautifulSoup
import urllib.request as req

code = req.urlopen("https://finance.naver.com/marketindex/")

soup = BeautifulSoup(code, "html.parser")
# 1. css 선택자 더 자세히 작성하는 방법으로 원하는 것만 출력.
# price = soup.select("ul#exchangeList span.value")
# for i in price:
#     print(i.string)

# 2. 데이터 가공
# price = soup.select("span.value")
# cnt = 0
# for i in price:
#     print(i.string)
#     cnt += 1
#     if cnt == 4:
#         break

# 3. 데이터 가공2
price = soup.select("span.value")
for i in price:
    print(i.string)
    if price.index(i) == 3:
        break