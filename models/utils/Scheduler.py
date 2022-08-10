from models.ProductModel import ProductModel
from scrapers.scraper import getJumiaPromos, getTTPromos, getVongoPromos
import os


def scrapDaily():
    ProductModel.deleteAll()
    getJumiaPromos(os.environ["JUMIA_PROMOS_LINK"])
    getTTPromos(os.environ["TUNISIA_TECH_LINK"])
    getVongoPromos(os.environ["VONGO_LINK"])
