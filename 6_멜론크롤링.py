import urllib.request as req
from bs4 import BeautifulSoup


header = req.Request("https://www.melon.com/chart/index.htm", headers={"User-Agent": "Mozilla/5.0"})
code = req.urlopen(header)
soup = BeautifulSoup(code, "html.parser")
title = soup.select("div.ellipsis.rank01 > span > a")
name = soup.select("div.ellipsis.rank02 > span")
album = soup.select("div.ellipsis.rank03 > a")
img = soup.select("a.image_typeAll > img")

# for i in range(len(title)):
#     print(title[i].string, name[i].text, album[i].string, img[i].attrs["src"])