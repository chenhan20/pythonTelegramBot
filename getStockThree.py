import pandas as pd
import json
import requests
import time
import datetime
import telegramBot
import getDb

# 偽瀏覽器
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def getHolding():
    # 持股資料 懶得寫資料庫 先這樣弄就好==
    holdingList = [{'symbol': '2330', 'shares': 450, 'avgCost': 403.73}
        , {'symbol': '2337', 'shares': 1000, 'avgCost': 39.07}
        , {'symbol': '2609', 'shares': 425, 'avgCost': 24.32}
        , {'symbol': '2454', 'shares': 50, 'avgCost': 877.14}
        , {'symbol': '2379', 'shares': 30, 'avgCost': 495.4}
        , {'symbol': '2303', 'shares': 100, 'avgCost': 47.74}
        , {'symbol': '2308', 'shares': 25, 'avgCost': 220.07}
        , {'symbol': '2892', 'shares': 575, 'avgCost': 21.7}
        , {'symbol': '2886', 'shares': 668, 'avgCost': 29.93}
        , {'symbol': '2884', 'shares': 481, 'avgCost': 25.85}
        , {'symbol': '2382', 'shares': 62, 'avgCost': 77.59}
        , {'symbol': '2377', 'shares': 101, 'avgCost': 111.85}
        , {'symbol': '0056', 'shares': 267, 'avgCost': 30.64}]
    return holdingList


def converterNumber(num):
    prefix = '+';
    if (num < 0):
        prefix = '-'
    absNum = abs(num)
    numberLength = len(str(absNum))
    converterNumber = num
    if (numberLength > 12):
        converterNumber = str(round(absNum / 1000000000000, 2)) + '兆'
    elif (numberLength > 8 and numberLength <= 12):
        converterNumber = str(round(absNum / 100000000, 2)) + '億'
    elif (numberLength > 4 and numberLength <= 8):
        converterNumber = str(round(absNum / 10000, 2)) + '萬'
    converterNumber = prefix + converterNumber
    return converterNumber


def converter(data):
    for i in range(len(data)):
        for d in range(len(data[i])):
            result = data[i][d].replace(',', '')
            if result.lstrip('-').isdigit():
                result = converterNumber(int(result))
            data[i][d] = result


def getThree(date):
    url = 'https://www.twse.com.tw/fund/BFI82U?response=json&dayDate=' + date + '&type=day'

    res = requests.get(url, headers=headers)
    stockData = json.loads(res.text)
    threeBuyDetail = {'data': [], 'fields': []}
    if stockData['stat'] == 'OK':
        converter(stockData['data'])
        threeBuyDetail['data'] = stockData['data']
        threeBuyDetail['fields'] = stockData['fields']

    return threeBuyDetail


def getThreeBuyDetail(date, stockNum):
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?date=' + \
          date.strftime("%Y%m%d") + '&stockNo=' + stockNum

    res = requests.get(url, headers=headers)
    stockData = json.loads(res.text)

    if stockData['stat'] == 'OK':
        converter(stockData['data'])
        return stockData
    else:
        print(stockData['stat'])
        return []


def follow_stock_code(userId):
    # userId先給1 之後再看怎麼抓發送者
    watchList = getDb.getFollowStock(userId)
    return watchList


watchList = follow_stock_code(1)


def less_than_three(symbol):
    return symbol[0] in watchList


def less_than_total(symbol):
    watchList = ['總計(1~15)']
    return symbol[0] in watchList


def less_than_day(symbol):
    watchList = ['發行量加權股價指數']
    return symbol[0] in watchList


def less_than_updown(symbol):
    watchList = ['上漲(漲停)', '下跌(跌停)']
    return symbol[0] in watchList


def getDayStockThreeBuySell(dateStr):
    url = 'https://www.twse.com.tw/fund/T86?response=json&date=' + dateStr + '&selectType=ALL'
    res = requests.get(url, headers=headers)
    stockData = json.loads(res.text)

    if stockData['stat'] == 'OK':
        filterList = filter(less_than_three, stockData['data'])
        return list(filterList)
    else:
        print(stockData['stat'])
        return []


def getWeekStockThreeBuySell(dateStr):
    url = 'https://www.twse.com.tw/fund/TWT54U?response=json&date=' + dateStr + '&selectType=ALL'
    res = requests.get(url, headers=headers)
    stockData = json.loads(res.text)

    if stockData['stat'] == 'OK':
        filterList = filter(less_than_three, stockData['data'])
        return list(filterList)
    else:
        print(stockData['stat'])
        return []


def getStockDayDetail(dateStr):
    url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=' + dateStr + '&type=ALL'
    res = requests.get(url, headers=headers)
    stockData = json.loads(res.text)
    dayData = {}

    if stockData['stat'] == 'OK':
        filterList = list(filter(less_than_three, stockData['data9']))
        dayList = list(filter(less_than_day, stockData['data1']))
        upDown = list(filter(less_than_updown, stockData['data8']))
        dayTotal = list(filter(less_than_total, stockData['data7']))
        dayData['stockPriceList'] = sorted(filterList, key=lambda s: float(s[10]), reverse=True)
        dayData['dayList'] = dayList
        dayData['upDown'] = upDown
        dayData['dayTotal'] = dayTotal
    else:
        print(stockData['stat'])

    return dayData


def test():
    converterNumber(1123456789999)


if __name__ == '__main__':
    test()
