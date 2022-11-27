import requests
import bs4
from fake_headers import Headers
from pprint import pprint

header = Headers(browser="chrome", os="win",  headers=True)
header = header.generate()

url = "https://habr.com/ru/all/"

KEYWORDS = ['IT', 'SQL', 'DevOps', 'Python']
articles_fin = {}
response = requests.get(url, headers=header)
soup = bs4.BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all("article")
for article in articles:
    habr_article = article.find_all(class_="tm-article-snippet tm-article-snippet")
    habr_article = [habr_article.text.strip() for habr_article in habr_article]
    for  habr_art in  habr_article:
        for habr_art in habr_art.split():
            if habr_art in KEYWORDS:
                article_habr = []
                href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                url_art = f"{url}{href}"
                title = article.find("h2").find('span').text
                data = article.find(class_="tm-article-snippet__datetime-published").find('time').attrs["title"]
                article_habr = [url_art, title, data]
                articles_fin[url_art] = article_habr

pprint(articles_fin)

