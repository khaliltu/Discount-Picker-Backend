import requests
from bs4 import BeautifulSoup as bs

from Services.scrapers.scrapUtils import deleteBlank, getDocument


def fetchDetails(doc):
    details = doc.find("div", {"id": "producttab-description"})
    details = [detail.text for detail in details.find_all("p")]
    return details


def fetchKeyValueDetails(doc):
    desc = doc.find("div", {"id": "short_description_block"})
    kvDetails = [li.text for li in desc.find_all("li")]
    for i in range(len(kvDetails)):
        if "\xa0" in kvDetails[i]:
            kvDetails[i] = kvDetails[i].replace("\xa0", "")
    return kvDetails


def getVongoDetails(link):
    doc = getDocument(link)
    details, kvDetails = fetchDetails(doc), fetchKeyValueDetails(doc)
    deleteBlank(details)
    deleteBlank(kvDetails)
    return details, kvDetails
