import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbstars

# 영화 정보 #
def get_url_movie():
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver', headers=headers)
  soup = BeautifulSoup(data.text, 'html.parser')
  trs = soup.select('#old_content > table > tbody > tr')

  urls2 = []
  for tr in trs:
    a = tr.select_one('td.title > div > a')
    if a is not None:
      base_url = 'https://movie.naver.com/'
      url2 = base_url + a['href']
      #base_url에서 해당 영화의 정보를 알고 싶으면 링크를 클릭해서 볼 수 있는데,
      #그 링크는 base_url에 추가되는 링크라서 a태그에 있는 링크를 더한다.
      
      urls2.append(url2)
      
  return urls2

# 출처 url로부터 영화들의 사진, 이름, 최근작 정보를 가져오고 저장한다.
def insert_movie(url2):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get(url2, headers=headers)
  soup = BeautifulSoup(data.text, 'html.parser')

  name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a').text
  type = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p').text
  actor = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p').text

  doc = {
    'name': name,
    'type': type,
    'actor': actor,
    'url': url2,
  }

  db.movies.insert_one(doc)
  print('완료!', name)
  # insert_all문으로 insert_star가 for문을 돌면서 배우를 한 명씩 가져오고,
  # 가져오기가 완료된 대상의 이름을 볼 수 있다.
  
# 영화 배우 정보 #
# DB에 저장할 영화인들의 출처 url을 가져옵니다.
def get_urls():
  headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get('https://movie.naver.com/movie/sdb/rank/rpeople.nhn', headers=headers)
  soup = BeautifulSoup(data.text, 'html.parser')
  trs = soup.select('#old_content > table > tbody > tr')

  urls = []
  for tr in trs:
    a = tr.select_one('td.title > a')
    if a is not None:
      base_url = 'https://movie.naver.com/'
      url = base_url + a['href']
      #base_url에서 해당 배우의 정보를 알고 싶으면 링크를 클릭해서 볼 수 있는데,
      #그 링크는 base_url에 추가되는 링크라서 a태그에 있는 링크를 더한다.
      
      urls.append(url)
      
  return urls

# 출처 url로부터 영화인들의 사진, 이름, 최근작 정보를 가져오고 저장한다.
def insert_star(url):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get(url, headers=headers)

  soup = BeautifulSoup(data.text, 'html.parser')

  name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
  img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
  recent_work = soup.select_one(
    '#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text

  doc = {
    'name': name,
    'img_url': img_url,
    'recent': recent_work,
    'url': url,
    'like': 0
  }

  db.mystar.insert_one(doc)
  print('완료!', name)
  # insert_all문으로 insert_star가 for문을 돌면서 배우를 한 명씩 가져오고,
  # 가져오기가 완료된 대상의 이름을 볼 수 있다.


# 기존 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
  db.mystar.drop()  
  # 기존의 mystar 내용을 모두 지워준 후에 넣기(갱신을 위함)
  urls = get_urls()
  
  db.movies.drop()  
  # 기존의 movies 내용을 모두 지워준 후에 넣기(갱신을 위함)
  urls2 = get_url_movie()
  
  for url2 in urls2:
    insert_movie(url2)
    
  for url in urls:
    insert_star(url)


### 실행하기
insert_all()



