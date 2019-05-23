import requests as url
from bs4 import BeautifulSoup as bs
#
#A simple web crawler
#
def spider(max_pages):
    page = 1
    while page <= max_pages:
        wURL = 'https://yts.am/browse-movies?page='+str(page)
        sourceCode = url.get(wURL)
        text = sourceCode.text
        soup = bs(text)
        for link in soup.findAll('a',{'class':'browse-movie-title'}):
            href = link.get('href')
            title = link.string
            print(title,'==>',href)
        page += 1
spider(2)
