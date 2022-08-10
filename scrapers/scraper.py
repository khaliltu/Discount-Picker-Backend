from models.ProductModel import ProductModel
from scrapers.jumiaScraper import getProducts, getProductsLinks
from scrapers.tunisiaTechScraper import getTTProductsList
from scrapers.vongoScrapper import getVongoProductsList


def getJumiaPromos(link):
    try:
        products = getProducts(link)
        insertProducts(products)
    except:
        pass


def getTTPromos(link):
    try:
        products = getTTProductsList(link)
        insertProducts(products)
    except:
        pass


def getVongoPromos(link):
    try:
        products = getVongoProductsList(link)
        insertProducts(products)
    except:
        pass


def insertProducts(products):
    ProductModel.insert(products)
