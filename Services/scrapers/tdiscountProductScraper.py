import requests
from bs4 import BeautifulSoup as bs


def getTdiscountDetails(link):
    site = requests.get(link)
    doc = bs(site.content, 'html.parser')
    des = doc.find('div', {'class': "product-short-description"})
    details = des.find_all('li')
    details = [detail.text.replace('\xa0', '') for detail in details]
    print(details)
    return details
