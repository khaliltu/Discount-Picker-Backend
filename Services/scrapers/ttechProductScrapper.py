import requests
from bs4 import BeautifulSoup as bs

from Services.scrapers.scrapUtils import deleteBlank, getDocument


def fetchKeyValueDetails(doc):
    desc = doc.find("div", {"class": "product-description-short"})
    kvDetails = desc.find_all('li')
    details = desc.find_all('p')
    kvDetails = [kvDetail.text for kvDetail in kvDetails]
    details = [detail.text for detail in details]
    for i in range(len(kvDetails)):
        if "\xa0" in kvDetails[i]:
            kvDetails[i] = kvDetails[i].replace("\xa0", "")
    for i in range(len(details)):
        if "\xa0" in details[i]:
            details[i] = details[i].replace("\xa0", "")
    return details, kvDetails


def getTTDetails(link):
    doc = getDocument(link)
    details, kvDetails = fetchKeyValueDetails(doc)
    kvDetails = deleteBlank(kvDetails)
    details = deleteBlank(details)
    return details, kvDetails
