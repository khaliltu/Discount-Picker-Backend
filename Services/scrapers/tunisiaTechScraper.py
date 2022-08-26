import requests
from bs4 import BeautifulSoup as bs


def getProductsTags(link):
    site = requests.get(link)
    doc = bs(site.content, "html.parser")
    articles = doc.find_all('article')
    return articles


def getProductInfos(tag):
    product = tag.text
    product = product.replace("\n", "xxx")
    product = product.replace("\xa0", " ")
    items = product.split("xxx")
    items = [item.strip() for item in items if item != '']
    return items


def getProductPrices(product):
    priceList = [price.replace("TND", "")
                 for price in product if 'TND' in price]
    for i in range(len(priceList)):
        if "Promo !" in priceList[i]:
            priceList[i] = priceList[i].replace("Promo !", '')
            break
    priceList = [float(price.replace(",", ".").strip()) for price in priceList]
    return tuple(priceList)


def getProductName(product):
    for item in product:
        if 'TND' in item:
            continue
        return item


def getProductLinks(tag):
    links = tag.find_all('link')
    hrefs = [link.attrs['href'] for link in links]
    return tuple(hrefs)


def getTTProductsList(link):
    productsList = []
    articles = getProductsTags(link)
    for article in articles:
        info = getProductInfos(article)
        try:
            discount, price, initialPrice = getProductPrices(info)
        except:
            continue
        name = getProductName(info)
        productLink, imageLink = getProductLinks(article)
        doc = requests.get(productLink)
        htmlDoc = bs(doc.content, "html.parser")
        spans = htmlDoc.find_all("span", {"itemprop": "name"})
        for span in spans:
            if span.text == "Accueil":
                i = spans.index(span)+1
                break
        cat = spans[i].text
        product = {"name": name, "price": price, "Initial Price": initialPrice,
                   "Discount Amount": discount, "Product link": productLink,
                   "Image Link": imageLink, "category": cat, "website": "TUNISIATECH"}
        productsList.append(product)
    return productsList
