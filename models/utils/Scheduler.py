from Services.scrapers.scraper import getJumiaPromos, getTTPromos, getTdiscountPromos, getVongoPromos
import os

from models.ProductModel import ProductModel


def scrapDaily():
    ProductModel.deleteAll()
    getJumiaPromos(os.environ["JUMIA_PROMOS_LINK"])
    getTTPromos(os.environ["TUNISIA_TECH_LINK"])
    getVongoPromos(os.environ["VONGO_LINK"])
    getTdiscountPromos(os.environ["TDISCOUNT_PROMOS_LINK"])
