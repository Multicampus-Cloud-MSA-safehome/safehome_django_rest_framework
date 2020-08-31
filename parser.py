import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urljoin
import django


# 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytest.settings")

# 장고를 가져와 장고 프로젝트를 사용할 수 있는 환경을 만들기
django.setup()

from newscrawl.models import NewsData

def parse_news():
    search_keyword = '서울시 안전'
    base = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_keyword}'

    req= requests.get(base)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_title = soup.select('a._sp_each_title') # 제목, 링크
    my_contents = soup.select('ul.type01 dl > dd:nth-child(3)') # 내용

    data = {}

    for idx, i in enumerate(my_title[:5]):
        title = i['title']
        link = urljoin(base, i['href'])
        contents = my_contents[idx].text
        
        data[title] = (link, contents)
        
    return data


if __name__ == '__main__':
    NewsData.objects.all().delete() # 객체 전체 삭제
    news_data_dict = parse_news() # 현재시간 뉴스 받아옴
    print(len(news_data_dict))

    for t, l in news_data_dict.items(): # 객체 저장
        NewsData(title=t, link=l[0], contents=l[1]).save()