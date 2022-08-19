from models.ProductModel import ProductModel
from Services.scrapers.jumiaScraper import getProducts
from .tdiscountScraper import getTdiscountProductsList
from Services.scrapers.tunisiaTechScraper import getTTProductsList
from Services.scrapers.vongoScrapper import getVongoProductsList


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


def getTdiscountPromos(link):
    try:
        products = getTdiscountProductsList(link)
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
