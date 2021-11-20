import requests
import bs4

res = requests.get("http://quotes.toscrape.com/")
# print(res)
# print(res.text)

soup = bs4.BeautifulSoup(res.text,'lxml')
# print(soup.select(".author"))

authors = set() 
for name in soup.select(".author"):
    authors.add(name.text)

print(authors)