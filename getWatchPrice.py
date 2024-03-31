import requests
from bs4 import BeautifulSoup
import time

sleepTime = 30
singlePage = True
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

watchStoreList = [
    {
        'storeCode': 'HS',
        'storeName': '鴻昇',
        'encoding': 'UTF-8',
        'url': 'https://www.999watch.com/product.asp?cat=47',
        'pageUrl': 'https://www.999watch.com/product.asp?index='
    },
    {
        'storeCode': 'EGPS',
        'storeName': '永生',
        'encoding': 'big5',
        'url': 'https://www.egps.com.tw/products.asp?subcat=350',
        'pageUrl': 'https://www.egps.com.tw/products.asp?index='
    },
    {
        'storeCode': 'RD',
        'storeName': '名錶雷達站',
        'url': 'https://www.rdwatch.com.tw/product.asp?cat=47',
        'pageUrl': 'https://www.rdwatch.com.tw/index.asp?index=',
        'encoding': 'UTF-8',
    },
]


def getWatchPrice():
    watchDict = dict()
    for store in watchStoreList:
        if store['storeCode'] == 'EGPS':
            watchDict[store['storeCode'] + '-' + store['storeName']] = getEGPSWatchDate(store)
        elif store['storeCode'] == 'HS':
            watchDict[store['storeCode'] + '-' + store['storeName']] = getHSWatchDate(store)
        elif store['storeCode'] == 'RD':
            watchDict[store['storeCode'] + '-' + store['storeName']] = getRDWatchDate(store)
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
    if not singlePage:
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
    watchList = []
    # FirstPage
    toWatchData(soup, watchList)

    if not singlePage:
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
    totalPage = 10 # 放棄抓頁數了 呼叫不到就直接break就好
    watchList = []
    # FirstPage
    toRDWatchData(soup, watchList)

    if not singlePage:
        for page in range(2, totalPage+1):
            time.sleep(sleepTime)  # 增加間格 避免被鎖
            response = requests.get(
                store['pageUrl'] + str(page), headers=headers, cookies=cookies)
            if response.status_code != 200:
                continue
            response.encoding = store['encoding']
            soup = BeautifulSoup(response.text, "html.parser")
            toRDWatchData(soup, watchList)

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
            titleText = replaceTitle(title.getText())
            result['title'] = titleText
            # result['highlight'] = str(watchTitleHighlightList[idx].getText())
            result['highlight'] = ''
            result['price'] = price
            watchList.append(result)
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))

def toRDWatchData(soup, watchList):
    watchTitleList = soup.select('a.a_table_list_txt span')
    watchPriceList = soup.select('span.shopping_Price span')
    watchTitleHighlightList = soup.select('a.a_table_list_txt font')
    noPriceCount = 0
    if len(watchTitleList) == 0:
        print('title = null')
        return
    for idx, title in enumerate(watchTitleList):
        try:
            result = dict()
            if len(title.find_parent('a').find_parent('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').select('span.shopping_Price span')) == 0 :
                price = 999999999999
                noPriceCount +=1
            else:
                price = int(watchPriceList[idx - noPriceCount].getText())
            titleText = replaceTitle(title.getText())
            if titleText in '手工微雕錶節':
                continue
            result['title'] = titleText
            result['highlight'] = ''
            result['price'] = price
            watchList.append(result)
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))

def replaceTitle(title):
    return title.replace('\r', '').replace('\n', '').replace('\t', '').replace('Rolex', '').replace('ROLEX', '').replace(
                'rolex', '').replace('勞力士', '').replace('！', '').replace('∼', '').replace('  ', ' ').replace('夯', '').replace(
                    '此錶歡迎各路錶友以 PP、AP、RM、 來店交換，本店將以最高價評估','(接受交換)')


if __name__ == '__main__':
    getWatchPrice()  # 或是任何你想執行的函式
