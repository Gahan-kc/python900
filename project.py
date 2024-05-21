url = "https://books.toscrape.com/"
import requests
html = requests.get(url).content
html
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"html.parser")
soup
soup.find_all('li',{'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
first_21 = soup.find_all('li',{'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
len(first_21)
first = first_21[0]
first
first.find("a")['href']
first.find('h3').find('a')['title']
first.find('p',{"class": "price_color"})
first.find('p',{"class": "price_color"}).text
first.find("p",{"class_": "instock availability"})
import re
regex = re.compile("star-rating(.*)")
first.find("p",{"class_": regex})
first.find("p",{"class": regex})['class']
def clean_screap(book):
    info = {}

    info['title'] = book.find("h3").find("a")['title']
    info['price'] = book.find("p",{'class': "price_color"}).text
    if "in stock" in first.find("p",{"class":"instock availability"}).text:
        info['in_stock'] = True
    else:
        info["in_stock"] = False

    info['stars'] = book.find("p",{"class":regex})['class'][-1]
    info["url"] = "http://books.toscrape.com/" + book.find("a")["href"]
    return info
book_dicts = [clean_screap(book) for book in first_21]
book_dicts
import pandas as pd
df = pd.DataFrame(book_dicts)
df.to_csv("data.csv" index=False)