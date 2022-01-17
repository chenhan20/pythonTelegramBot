import yfinance as yf

indexList = [
    {
        'name': '^DJI',
        'displayName': '道瓊DJI'
    },
    {
        'name': '^GSPC',
        'displayName': 'S&P500'
    },
    {
        'name': '^IXIC',
        'displayName': '納斯達克'
    },
    {
        'name': '^SOX',
        'displayName': '費城半導體'
    },
]


def getYfIndexData():
    resultList = []

    for indexObj in indexList:
        indexName = indexObj['name']
        result = dict()
        ticker = yf.Ticker(indexName)
        data = ticker.history()
        last_second_quote = data.tail(2)['Close'].iloc[0]
        last_quote = data.tail(1)['Close'].iloc[0]
        indexGap = round(last_quote - last_second_quote, 1)
        percent = round(indexGap / last_second_quote * 100, 1)
        result['title'] = indexObj['displayName']
        result['value'] = str(round(data.tail(1)['Close'].iloc[0], 1))
        result['indexGap'] = converterPrefix(indexGap)
        converterPercent = str(percent).replace('+', '').replace('-', '')
        result['gapPercent'] = converterPercent + '%'
        result['lastUpdateDate'] = str(data.tail(1)['Close'].index.values[0])[:10]
        resultList.append(result)

    return resultList


def getYfStockData():
    stocks = ['PLTR', 'TSLA', 'AAPL', 'AMD', 'APPS', 'NVDA', 'NFLX', 'INTC']
    resultList = []

    for name in stocks:
        try:
            ticker = yf.Ticker(name)
            result = dict()
            data = ticker.history()
            last_second_quote = data.tail(2)['Close'].iloc[0]
            last_quote = data.tail(1)['Close'].iloc[0]
            indexGap = round(last_quote - last_second_quote, 1)
            percent = round(indexGap / last_second_quote * 100, 1)
            result['title'] = name
            result['value'] = str(round(data.tail(1)['Close'].iloc[0], 1))
            result['indexGap'] = converterPrefix(indexGap)
            converterPercent = str(percent).replace('+', '').replace('-', '')
            result['percent'] = percent
            result['gapPercent'] = converterPercent + '%'
            result['lastUpdateDate'] = str(data.tail(1)['Close'].index.values[0])[:10]
            resultList.append(result)
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
            break

    resultList = sorted(resultList, key=lambda d: d['percent'], reverse=True)

    return resultList


def getCryptoData():
    cryptoNames = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'CAKE-USD', 'SOL-USD', 'AVAX-USD', 'CRO-USD', 'FTT-USD']
    resultList = []

    for cryptoName in cryptoNames:
        try:
            ticker = yf.Ticker(cryptoName)
            result = dict()
            data = ticker.history()
            last_second_quote = data.tail(2)['Close'].iloc[0]
            last_quote = data.tail(1)['Close'].iloc[0]
            indexGap = round(last_quote - last_second_quote, 2)
            percent = round(indexGap / last_second_quote * 100, 2)
            result['title'] = cryptoName.replace('-USD', '')
            result['value'] = str(round(data.tail(1)['Close'].iloc[0], 2))
            result['indexGap'] = converterPrefix(indexGap)
            converterPercent = str(percent).replace('+', '').replace('-', '')
            result['percent'] = percent
            result['gapPercent'] = converterPercent + '%'
            result['lastUpdateDate'] = str(data.tail(1)['Close'].index.values[0])[:10]
            resultList.append(result)
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
            break

    resultList = sorted(resultList, key=lambda d: d['percent'], reverse=True)

    # for result in resultList:
    #     print(result)

    return resultList


def converterPrefix(percent):
    converterPercent = str(percent).replace('+', '').replace('-', '')
    converterValue = ''
    prefix = ''
    if percent > 0:
        prefix = '🔺'
    elif percent < 0:
        prefix = '🔻'
    converterValue = prefix + converterPercent
    return converterValue


def test():
    for index in indexList:
        print(index['displayName'])


if __name__ == '__main__':
    # getYfDataOld(defaultStockList)
    # getYfData()
    print(getCryptoData())
    # print(getYfStockData())
