from fredapi import Fred
import configparser
import datetime
from datetime import timedelta

config = configparser.ConfigParser()
config.sections()
config.read('setting.ini')


fredToken = config['DEFAULT']['FRED_API_KEY']

def getFredAPI():
    fred = Fred(api_key=fredToken)  # 替換成輸入你的api key
    #那斯達克少一天資料== 不知道為啥
    #邏輯 當天早上八點跑 now.date - 1天 去抓資料 抓地到就發 抓不到就不發 暫時先醬
    watchList = ['SP500','DJIA','NASDAQCOM']
    resultList = []
    for watch in watchList:
        result = dict()
        watchLastIndex = fred.get_series(watch).tail(2)
        # print(watchLastIndex)
        if(len(watchLastIndex)>1):
            percent = round((watchLastIndex[1] - watchLastIndex[0]) / watchLastIndex[0] * 100 , 2) 
            result['title'] = watch
            result['value'] = str(watchLastIndex[1])
            result['percent'] = converterPrefix(percent)
            resultList.append(result)
    
    return resultList

def converterPrefix(percent):
    converterPercent = str(percent).replace('+','').replace('-','')
    converterValue = ''
    prefix = ''
    if(percent>0):
        prefix = '🔺'
    elif(percent < 0):
        prefix = '🔻'
    converterValue = prefix + converterPercent + '%'
    return converterValue

def testFredAPI():
    fred = Fred(api_key=fredToken)  # 替換成輸入你的api key
    watchLastIndex = fred.get_series('SP500')
    print(type(watchLastIndex))
    print(watchLastIndex.tail(2))


    

if __name__ == '__main__':
    yesterdayDate = datetime.date(2021, 10, 4)
    print(getFredAPI(yesterdayDate))
    # print(testFredAPI())