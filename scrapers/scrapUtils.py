
import requests
from bs4 import BeautifulSoup as bs


def deleteBlank(stringList):
    for char in stringList:
        if char is "":
            stringList.pop(stringList.index(char))
    return stringList


def getDocument(link):
    try:
        site = requests.get(link)
        doc = bs(site.content, "html.parser")
        return doc
    except:
        return''
