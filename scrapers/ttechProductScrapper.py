import requests
from bs4 import BeautifulSoup as bs

from scrapers.scrapUtils import deleteBlank, getDocument


def fetchKeyValueDetails(doc):
    desc = doc.find("div", {"id": "product-description-short-2234"})
    kvDetails = desc.find_all('li')
    kvDetails = [kvDetail.text for kvDetail in kvDetails]
    for i in range(len(kvDetails)):
        if "\xa0" in kvDetails[i]:
            kvDetails[i] = kvDetails[i].replace("\xa0", "")
    return kvDetails


def getTTDetails(link):
    doc = getDocument(link)
    kvDetails = fetchKeyValueDetails(doc)
    kvDetails = deleteBlank(kvDetails)
    return kvDetails
