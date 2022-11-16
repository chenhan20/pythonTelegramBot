import requests
from bs4 import BeautifulSoup
import time

sleepTime = 30
watchStoreList = [
    {
        'storeCode': 'HS',
        'storeName': '鴻昇',
        'encoding': 'UTF-8',
        'url': 'http://www.999watch.com/product.asp?cat=47',
        'pageUrl': 'http://www.999watch.com/product.asp?index='
    },
    {
        'storeCode': 'EGPS',
        'storeName': '永生',
        'encoding': 'big5',
        'url': 'http://www.egps.com.tw/products.asp?subcat=350&type=open',
        'pageUrl': 'http://www.egps.com.tw/products.asp?index='
    },
    # {
    #     'storeCode': 'RD',
    #     'storeName': '名錶雷達站',
    #     'url': 'http://www.rdwatch.com.tw/product.asp?cat=47',
    #     'encoding': 'big5',
    # },
]


def getWatchPrice():
    watchDict = dict()
    for store in watchStoreList:
        if store['storeCode'] == 'EGPS':
            watchDict[store['storeCode']] = getEGPSWatchDate(store)
        elif store['storeCode'] == 'HS':
            watchDict[store['storeCode']] = getHSWatchDate(store)
        elif store['storeCode'] == 'RD':
            watchDict[store['storeCode']] = getRDWatchDate(store)
        else:
            continue
    return watchDict


def getEGPSWatchDate(store):
    response = requests.get(store['url'])
    if response.status_code != 200:
        return []
    cookies = response.cookies
    response.encoding = store['encoding']

    soup = BeautifulSoup(response.text, "html.parser")
    totalPage = len(soup.select('td.next_bg table tr td a')) - 4
    watchList = []
    # FirstPage
    toWatchData(soup, watchList)
    print(store['storeName'] + 'totalPage:' + str(totalPage))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    for page in range(2, totalPage+1):
        time.sleep(sleepTime)  # 增加間格 避免被鎖
        response = requests.get(
            store['pageUrl'] + str(page), headers=headers, cookies=cookies)
        if response.status_code != 200:
            continue
        response.encoding = store['encoding']
        soup = BeautifulSoup(response.text, "html.parser")
        toWatchData(soup, watchList)

    watchList = sorted(watchList, key=lambda d: d['price'], reverse=True)
    return watchList


def getHSWatchDate(store):
    response = requests.get(store['url'])
    if response.status_code != 200:
        return []
    cookies = response.cookies
    response.encoding = store['encoding']

    soup = BeautifulSoup(response.text, "html.parser")
    totalPage = len(soup.select('td.next_bg table tr td a')) - 4
    print(store['storeName'] + 'totalPage:' + str(totalPage))
    watchList = []
    # FirstPage
    toWatchData(soup, watchList)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    for page in range(2, totalPage+1):
        time.sleep(sleepTime)  # 增加間格 避免被鎖
        response = requests.get(
            store['pageUrl'] + str(page), headers=headers, cookies=cookies)
        if response.status_code != 200:
            continue
        response.encoding = store['encoding']
        soup = BeautifulSoup(response.text, "html.parser")
        toWatchData(soup, watchList)

    watchList = sorted(watchList, key=lambda d: d['price'], reverse=True)
    return watchList


def getRDWatchDate(store):
    response = requests.get(store['url'])
    if response.status_code != 200:
        return []
    cookies = response.cookies
    response.encoding = store['encoding']

    soup = BeautifulSoup(response.text, "html.parser")
    totalPage = len(soup.select('td.next_bg table tr td a')) - 4
    print(store['storeName'] + 'totalPage:' + str(totalPage))
    watchList = []
    # FirstPage
    toWatchData(soup, watchList)
    print(store['storeName'] + 'totalPage:' + str(totalPage))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    # for page in range(2, totalPage+1):
    #     time.sleep(sleepTime)  # 增加間格 避免被鎖
    #     response = requests.get(
    #         store['pageUrl'] + str(page), headers=headers, cookies=cookies)
    #     if response.status_code != 200:
    #         continue
    #     response.encoding = store['encoding']
    #     soup = BeautifulSoup(response.text, "html.parser")
    #     toWatchData(soup, watchList)

    watchList = sorted(watchList, key=lambda d: d['price'], reverse=True)
    return watchList


def toWatchData(soup, watchList):
    watchTitleList = soup.find_all(attrs={"class": "a_table_list_txt"})
    watchPriceList = soup.select('span.shopping_Price')
    watchTitleHighlightList = soup.select('.a_table_list_txt font')
    if len(watchTitleList) == 0:
        print('title = null')
        return
    for idx, title in enumerate(watchTitleList):
        try:
            result = dict()
            price = int(watchPriceList[idx].getText())
            titleText = title.getText().replace('\r', '').replace('\n', '').replace('\t', '').replace('ROLEX', '').replace(
                'rolex', '').replace('勞力士', '').replace('！', '').replace('∼', '').replace('  ', ' ').replace('夯', '')
            result['title'] = titleText
            result['highlight'] = str(watchTitleHighlightList[idx].getText())
            result['price'] = price
            watchList.append(result)
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))


if __name__ == '__main__':
    print(getWatchPrice())  # 或是任何你想執行的函式
