import pandas as pd
import json
import requests
import time
import datetime
import telegramBot

# 偽瀏覽器
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def converterNumber(num):
    numberLength = len(str(num))
    converterNumber = num
    if(numberLength > 12):
        converterNumber = str(round(num / 1000000000000, 2)) + '兆'
    elif(numberLength > 8 and numberLength <= 12):
        converterNumber = str(round(num / 100000000, 2)) + '億'
    elif(numberLength > 4 and numberLength <= 8):
        converterNumber = str(round(num / 10000, 2)) + '萬'
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
        date.strftime("%Y%m%d")+'&stockNo=' + stockNum

    res = requests.get(url, headers=headers)
    stockData = json.loads(res.text)

    if stockData['stat'] == 'OK':
        converter(stockData['data'])
        return stockData
    else:
        print(stockData['stat'])
        return []


def less_than_three(symbol):
    watchList = ['2330', '2337', '2454', '2377', '2308', '2382','2382','2892','2884','2886','2303']
    return symbol[0] in watchList


def getStockThreeBuySell(dateStr):
    
    url = 'https://www.twse.com.tw/fund/T86?response=json&date=' + dateStr +'&selectType=ALL'
    res = requests.get(url, headers=headers)
    stockData = json.loads(res.text)

    if stockData['stat'] == 'OK':
        fliterList = filter(less_than_three, stockData['data'])
        return list(fliterList)
    else:
        print(stockData['stat'])
        return []


def getStockPrice(dateStr):
    url = ' https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=' + dateStr +'&type=ALLBUT0999'
    res = requests.get(url, headers=headers)
    stockData = json.loads(res.text)

    if stockData['stat'] == 'OK':
        fliterList = list(filter(less_than_three, stockData['data9']))
        return sorted(fliterList, key = lambda s: float(s[10]), reverse = True)
    else:
        print(stockData['stat'])
        return []


def test():
    print('test')

if __name__ == '__main__':
    test()
