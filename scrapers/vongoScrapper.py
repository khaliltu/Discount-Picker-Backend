import requests
from bs4 import BeautifulSoup as bs


def getProductsTags(link):
    site = requests.get(link)
    doc = bs(site.content, "html.parser")
    flashSales = doc.find("ul", {"id": "flashsales"})
    return flashSales.find_all("li")


def getDiscount(initialPrice, price):
    for i in range(len(initialPrice)):
        if not initialPrice[i].isdigit():
            for j in range(len(price)):
                if not price[j].isdigit():
                    discount = float(initialPrice[:i]) - float(price[:j])
                    return discount


def getProductItems(tag):
    initialPrice = tag.find("span", {"class": "old-price"}).text
    if "Ancien prix:" in initialPrice:
        initialPrice = initialPrice.replace("Ancien prix:", "").strip()
    price = tag.find("span", {"class": "price"}).text.strip()
    discount = getDiscount(initialPrice, price)
    name = tag.find("a", {"class": "product-name"}).text
    return name, price, initialPrice, discount


def getProductLinks(tag):
    productLink = tag.find("a", {"class": "product_img_link"}).attrs['href']
    productImageLink = tag.find(
        "a", {"class": "product_img_link"}).find("img").attrs["src"]
    return productLink, productImageLink


def getVongoProductsList(link):
    tags = getProductsTags(link)
    productsList = []
    for tag in tags:
        try:
            name, price, initialPrice, discount = getProductItems(tag)
            productLink, productImageLink = getProductLinks(tag)
            website = "VONGO"
            product = {"name": name, "price": price, "Initial Price": initialPrice, "Discount Amount": discount,
                       "Product link": productLink, "Image Link": productImageLink, "website": website}
            productsList.append(product)
        except:
            continue
    return productsList
