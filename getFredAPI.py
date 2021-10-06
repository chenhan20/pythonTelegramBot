from fredapi import Fred
import configparser
import datetime
from datetime import timedelta

config = configparser.ConfigParser()
config.sections()
config.read('setting.ini')


fredToken = config['DEFAULT']['FRED_API_KEY']

def getFredAPI():
    fred = Fred(api_key=fredToken) 
    #'NASDAQCOM' 更新時間太慢 暫時不發
    watchList = ['SP500','DJIA']
    resultList = []
    for watch in watchList:
        result = dict()
        watchLastInfo = fred.get_series_info(watch)
        watchLastIndex = fred.get_series(watch).tail(2)
        lastUpdateDate = watchLastInfo.observation_end
        indexGap = round(watchLastIndex[1] - watchLastIndex[0], 2)
        percent = round(indexGap / watchLastIndex[0] * 100 , 2) 
        result['title'] = watch
        result['value'] = str(watchLastIndex[1])
        result['indexGap'] = converterPrefix(indexGap)
        converterPercent = str(percent).replace('+','').replace('-','')
        result['gapPercent'] = converterPercent + '%'
        result['lastUpdateDate'] = lastUpdateDate
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
    converterValue = prefix + converterPercent
    return converterValue

if __name__ == '__main__':
    print(getFredAPI())