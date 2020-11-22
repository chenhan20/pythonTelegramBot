import pandas as pd
import json
import requests 
import time 
import datetime
# 偽瀏覽器
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def converterNumber(num):
    numberLength = len(str(num))
    converterNumber =num
    if(numberLength > 12):
        converterNumber = str(round(num / 1000000000000,2)) + '兆'
    elif(numberLength > 8 and numberLength <= 12):
        converterNumber = str(round(num / 100000000,2)) + '億'
    elif(numberLength > 4 and numberLength <= 8):
        converterNumber = str(round(num / 10000,2)) + '萬'
    return converterNumber

def converter(data):
    for i in range(len(data)):
        for d in range(len(data[i])):
            result = data[i][d].replace(',','')
            if result.lstrip('-').isdigit():
                result = converterNumber(int(result))
            data[i][d] = result

def getThree(date):
    url = 'https://www.twse.com.tw/fund/BFI82U?response=json&dayDate='+ date +'&type=day'

    res = requests.get(url, headers=headers)
    stockData=json.loads(res.text)
    threeBuyDetail = {'data':[],'fields':[]}
    if stockData['stat']=='OK':
        converter(stockData['data'])
        # df = pd.DataFrame(stockData['data'],columns=stockData['fields'])
        # pd.set_option('display.unicode.ambiguous_as_wide', True)
        # pd.set_option('display.unicode.east_asian_width', True)
        # print(stockData['title'])
        # print('============================================================')
        # print(df)
        converter(stockData['data'])
        threeBuyDetail['data'] = stockData['data']
        threeBuyDetail['fields'] = stockData['fields']
    
    return threeBuyDetail

def getThreeBuyDetail(date, stockNum):
    # url = 'https://www.twse.com.tw/fund/T86?response=json&date=20201111&selectType=ALL'
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?date='+date.strftime("%Y%m%d")+'&stockNo=' + stockNum

    res = requests.get(url, headers=headers)
    stockData=json.loads(res.text)

    if stockData['stat']=='OK':
        converter(stockData['data'])
        return stockData
    else:
        print(stockData['stat'])
        return []


def test():
    threeData=[['自營商(自行買賣)', '24.41億', '24.66億', '-0.24億'], ['自營商(避險)', '51.79億', '52.62億', '-0.84億'], ['投信', '31.11億', '31.74億', '-0.63億'], ['外資及陸資(不含外資自營商)', '723.23億', '572.24億', '150.99億'], ['外資自營商', '1527.2萬', '1377.2萬', '150.0萬'], ['合計', '830.55億', '681.26億', '149.28億']]
    fields=['單位名稱', '買進金額', '賣出金額', '買賣差額']
    # 建立 DataFrame 物件
    student_df = pd.DataFrame(threeData,columns=fields)

    # 列出欄位資料型別等資訊
    # student_df.style.set_properties(**{'text-align': 'right'})
    student_df

if __name__ == '__main__':
    now = datetime.datetime.now()
    date = now - datetime.timedelta(days=1)
    print('Call it locally')

    test();