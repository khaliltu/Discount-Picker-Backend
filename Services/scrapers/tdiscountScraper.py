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
            productlink = article.find("a").attrs['href']
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
            doc = requests.get(productlink)
            htmlDoc = bs(doc.content, "html.parser")
            ol = htmlDoc.find("ol")
            spans = ol.find_all("span", {"itemprop": "name"})
            for span in spans:
                if span.text == "Accueil":
                    i = spans.index(span)+1
                    break
            cat = spans[i].text
            product = {"name": name, "price": price, "Initial Price": oldPrice, "Discount Amount": discount,
                       "Product link": productlink, "Image Link": imageLink, "category": cat, "website": website}
            productsList.append(product)
        except:
            continue
    return productsList
