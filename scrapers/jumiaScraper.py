import requests
from bs4 import BeautifulSoup as bs


def getProductsLinks(link):
    flashSales = requests.get(link)
    doc = bs(flashSales.text, "html.parser")
    links = doc.find_all("a")
    links = [link for link in links if 'href' in link.attrs and ".html" in link.attrs["href"]
             and "TND" in link.text]
    return links


def extractInfos(tag):
    text = tag.text
    items = text.split("TND")
    name = items[0]
    name = name.strip()
    price = ""
    for i in name[::-1]:
        if i.isdigit() or i == ".":
            price += i
        else:
            break
    price = price[::-1]
    name = tag.attrs["data-name"]
    intialPrice = items[1]
    price = str(float(price))
    discount = items[2].split("%")[0]
    category = tag.attrs["data-category"]
    brand = tag.attrs["data-brand"]
    return name, price, intialPrice, discount, category, brand


def getProductLink(tag):
    return "https://www.jumia.com.tn"+tag.attrs["href"]


def getImageLink(tag):
    return tag.img.attrs['data-src']


def getProducts(link):
    links = getProductsLinks(link)
    flashSales = []
    for link in links:
        try:
            name, price, initialPrice, discount, category, brand = extractInfos(
                link)
            product = {"name": name, "price": price, "Initial Price": initialPrice, "Discount Percentage": discount,
                       "Product link": getProductLink(link), "Image Link": getImageLink(link), "category": category,
                       "brand": brand, "website": "JUMIA"}
            flashSales.append(product)
        except:
            continue
    return flashSales
