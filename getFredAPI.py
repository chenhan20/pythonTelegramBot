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
    watchList = ['SP500','DJIA','NASDAQCOM']
    resultList = []
    for watch in watchList:
        result = dict()
        watchLastInfo = fred.get_series_info(watch)
        watchLastIndex = fred.get_series(watch).tail(2)
        lastUpdateDate = watchLastInfo.observation_end
        percent = round((watchLastIndex[1] - watchLastIndex[0]) / watchLastIndex[0] * 100 , 2) 
        result['title'] = watch
        result['value'] = str(watchLastIndex[1])
        result['percent'] = converterPrefix(percent)
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
    converterValue = prefix + converterPercent + '%'
    return converterValue

def testFredAPI():
    fred = Fred(api_key=fredToken) 
    watchList = ['SP500','DJIA','NASDAQCOM']
    resultList = []
    for watch in watchList:
        result = dict()
        watchLastInfo = fred.get_series_info(watch)
        watchLastIndex = fred.get_series(watch).tail(2)
        lastUpdateDate = watchLastInfo.observation_end
        if(len(watchLastIndex)>1):
            percent = round((watchLastIndex[1] - watchLastIndex[0]) / watchLastIndex[0] * 100 , 2) 
            result['title'] = watch
            result['value'] = str(watchLastIndex[1])
            result['percent'] = converterPrefix(percent)
            result['lastUpdateDate'] = lastUpdateDate
            resultList.append(result)
    
    return resultList    

if __name__ == '__main__':
    print(testFredAPI())
    # print(testFredAPI())