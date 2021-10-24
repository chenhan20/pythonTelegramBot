import yfinance as yf

indexList = [
    {
        'name': '^DJI',
        'displayName' : '道瓊DJI'
    },
    {
        'name': '^GSPC',
        'displayName' : 'S&P500'
    },
    {
        'name': '^IXIC',
        'displayName' : '納斯達克'
    },
    {
        'name': '^SOX',
        'displayName' : '費城半導體'
    },
]

def getYfIndexData():
    # stocks = ['SQ','PLTR','TSLA','AAPL','AMD','APPS','BYND','PINS','GRMN','NKE','ORCL','FB','ZM','SPOT','NVDA','INTC','BRK-B','GOOG','UBER','TSM','UMC','MU','NFLX']
    indexs = ['^DJI','^GSPC','^IXIC','^SOX']
    resultList = []

    for indexObj in indexList:
        indexName = indexObj['name']
        result = dict()
        ticker = yf.Ticker(indexName)
        data = ticker.history()
        last_second_quote = data.tail(2)['Close'].iloc[0]
        last_quote = data.tail(1)['Close'].iloc[0]
        indexGap = round(last_quote - last_second_quote, 1)
        percent = round(indexGap / last_second_quote * 100 , 1) 
        result['title'] = indexObj['displayName']
        result['value'] = str(round(data.tail(1)['Close'].iloc[0],1))
        result['indexGap'] = converterPrefix(indexGap)
        converterPercent = str(percent).replace('+','').replace('-','')
        result['gapPercent'] = converterPercent + '%'
        result['lastUpdateDate'] = str(data.tail(1)['Close'].index.values[0])[:10] 
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


def test():

    for index in indexList:
        print(index['displayName'])

if __name__ == '__main__':
    # getYfDataOld(defaultStockList)
    # getYfData()
    test()
