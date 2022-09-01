

from Services.scrapers.jumiaProductScrapper import getJumiaDetails
from Services.scrapers.tdiscountProductScraper import getTdiscountDetails
from Services.scrapers.ttechProductScrapper import getTTDetails
from Services.scrapers.vongoProductScrapper import getVongoDetails


def isSubString(substring, string):
    if ' ' in substring:
        substring = substring.split(" ")[0]
    if (substring.upper() in string) or (substring.lower() in string) or (substring.lower().capitalize() in string):
        return True
    return False


def most_2_frequent(ListDict):
    firstFrequent = most_frequent(ListDict)
    secondList = [i for i in ListDict if firstFrequent not in i]
    secondFrequent = most_frequent(secondList)
    return firstFrequent, secondFrequent


def most_frequent(ListDict):
    m = 1
    for i in ListDict:
        if list(i.values())[0] > m:
            m = list(i.values())[0]
            mx = list(i.keys())[0]
    return mx


def registerProductDetails(product):
    if (product["website"] == "JUMIA"):
        try:
            product["details"], product["key value details"] = getJumiaDetails(
                product["Product link"])
        except:
            pass
    if (product["website"] == "VONGO"):
        try:
            product["details"], product["key value details"] = getVongoDetails(
                product["Product link"])
        except:
            pass
    if (product["website"] == "TUNISIATECH"):
        try:
            product["details"], product["key value details"] = getTTDetails(
                product["Product link"])
        except:
            pass
    if (product["website"] == "TDISCOUNT"):
        try:
            product["details"] = getTdiscountDetails(
                product["Product link"])
            product["key value details"] = []
        except:
            pass
