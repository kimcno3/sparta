import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# header : 브라우저에서 엔터를 눌러 요청한 것과 같은 효과를 내기 위해 사용, 대부분의 사이트는 크롤링하는 것을 막아두었기 때문에!!
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs :

    a_rank = tr.select_one('td:nth-child(1) > img')
    a_tag = tr.select_one('td.title > div > a')
    a_star = tr.select_one('td.point')

    if a_tag is not None:
        rank = a_rank['alt']
        title = a_tag.text
        star = a_star.text
        doc = {
            'title' : title,
            'rank' : rank,
            'star' : star
        }
        db.movies.insert_one(doc) // 반복문이니까 one으로 돌때마다 하나씩 insert

