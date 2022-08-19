import requests
from bs4 import BeautifulSoup as bs


def getArticles(link):
    site = requests.get(link)
    doc = bs(site.content, "html.parser")
    articles = doc.find_all('article', {"class": "product-miniature"})
    return articles


def getTdiscountProductsList(link):
    articles = getArticles(link)
    productsList = []
    for article in articles:
        try:
            name = article.find("h2", {"class": "product-title"}).text
            link = article.find("a").attrs['href']
            price = article.find("span", {"class": "price"}).text.split("\xa0")[
                0].replace(",", ".")
            price = float(price)
            oldPrice = oldPrice = article.find(
                "span", {"class": "regular-price"}).text.split("\xa0")[0].replace(",", ".")
            oldPrice = float(oldPrice)
            discount = round(oldPrice - price)
            img = article.find("div", {"class": "product-image"})
            imageLink = img.find("img").attrs["src"]
            website = 'TDISCOUNT'
            product = {"name": name, "price": price, "Initial Price": oldPrice, "Discount Amount": discount,
                       "Product link": link, "Image Link": imageLink, "website": website}
            productsList.append(product)
        except:
            continue
    return productsList
