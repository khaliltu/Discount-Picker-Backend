import requests
from bs4 import BeautifulSoup as bs

from Services.scrapers.scrapUtils import deleteBlank


def getInfoSection(link):
    site = requests.get(link)
    doc = bs(site.content, "html.parser")
    secs = doc.find_all("section")
    sec = [section for section in secs if "Fiche technique" in section.text][0]
    return sec


def fetchDetails(infoSection):
    li_s = infoSection.find("div", {"class": "markup -pam"})
    listDetails = li_s.find_all("li")
    listDetails = [li.text for li in listDetails]
    return listDetails


def fetchKeyValuesDetails(infoSection):
    li_kv = infoSection.find("ul", {"class": "-pvs -mvxs -phm -lsn"})
    listkvDetails = li_kv.find_all("li")
    listkvDetails = [li.text for li in listkvDetails]
    return listkvDetails


def getJumiaDetails(link):
    section = getInfoSection(link)
    details, kvDetails = fetchDetails(section), fetchKeyValuesDetails(section)
    deleteBlank(details)
    deleteBlank(kvDetails)
    return details, kvDetails
