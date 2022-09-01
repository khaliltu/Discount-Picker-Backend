import json
from random import sample
from bson.json_util import dumps
from models.UserHistoryModel import UserHistoryModel


class UserHistoryService():
    def add(product, email):
        history = {}
        history["email"] = email
        history["clickNumber"] = 1
        history["favoriteCategories"] = [{product["category"]:1}]
        history["favoriteSellers"] = [{product["website"]:1}]
        history["priceMean"] = product["price"]
        return UserHistoryModel.add(history)

    def find(email):
        return UserHistoryModel.find(email)

    def update(product, email):
        userHistory = UserHistoryModel.find(email)
        userHistory = dumps(userHistory)
        userHistory = json.loads(userHistory)[0]
        updateList(userHistory["favoriteCategories"], product["category"])
        updateList(userHistory["favoriteSellers"], product["website"])
        updatePriceMean(userHistory, product)
        return UserHistoryModel.update(userHistory)

    def getRecommandations(email, products):
        try:
            userHistory = UserHistoryModel.find(email)
            userHistory = dumps(userHistory)
            userHistory = json.loads(userHistory)[0]
            favoriteCategories, favoriteSellers = getKeyItems(userHistory)
            recommandedProducts = [product for product in products if (
                product["category"] in favoriteCategories) or (product["website"] in favoriteSellers)]
            recommandedProducts = get_closest(
                recommandedProducts, userHistory["priceMean"])
            return recommandedProducts
        except:
            return sample(products, 3)


def updatePriceMean(userHistory, product):
    priceMean = userHistory['priceMean']
    priceMean = (priceMean * userHistory["clickNumber"])+product["price"]
    userHistory["clickNumber"] = userHistory["clickNumber"]+1
    priceMean = priceMean/userHistory['clickNumber']
    userHistory["priceMean"] = priceMean


def updateList(itemList, itemString):
    for item in itemList:
        if itemString in item:
            item[itemString] += 1
            break
    else:
        itemList.append({itemString: 1})


def getKeyItems(userHistory):
    userHistory["favoriteCategories"].sort(
        key=lambda x: list(x.values())[0], reverse=True)
    userHistory["favoriteSellers"].sort(
        key=lambda x: list(x.values())[0], reverse=True)
    favoriteCategories = []
    favoriteSellers = []
    if len(userHistory["favoriteCategories"]) > 1:
        favoriteCategories = userHistory["favoriteCategories"][0:2]
    else:
        favoriteCategories.append(userHistory["favoriteCategories"][0])
    if len(userHistory["favoriteSellers"]) > 1:
        favoriteSellers = userHistory["favoriteSellers"][0:2]
    else:
        favoriteSellers.append(userHistory["favoriteSellers"][0])
    favoriteCategories = [list(item.keys())[0] for item in favoriteCategories]
    favoriteSellers = [list(item.keys())[0] for item in favoriteSellers]
    return favoriteCategories, favoriteSellers


def get_closest(productsList, priceMean):
    productsList.sort(key=lambda x: abs(x['price']-priceMean))
    if len(productsList) < 3:
        return productsList
    elif len(productsList) < 9:
        return sample(productsList, 3)
    else:
        return sample(productsList[0:9], 4)
