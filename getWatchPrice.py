import requests
from bs4 import BeautifulSoup
import time


def getWatchPrice():
    url = 'http://www.egps.com.tw/products.asp?subcat=350&type=open'
    response = requests.get(url)
    cookies = response.cookies
    response.encoding = 'big5'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    soup = BeautifulSoup(response.text, "html.parser")
    totalPage = len(soup.select('td.next_bg table tr td a')) - 5
    watchList = []
    # FirstPage 
    toWatchData(soup,watchList)
    for page in range(totalPage):
        response = requests.get('http://www.egps.com.tw/products.asp?index=' + str(page+2),headers=headers, cookies=cookies)
        response.encoding = 'big5'
        soup = BeautifulSoup(response.text, "html.parser")
        toWatchData(soup,watchList)
        print(page+2)
        time.sleep(30) # 增加間格 避免被鎖

    return watchList
    

def toWatchData(soup,watchList):
    watchTitleList = soup.find_all(attrs={"class":"a_table_list_txt"})
    watchPriceList = soup.select('span.shopping_Price')
    watchTitleHighlightList = soup.select('.a_table_list_txt font')
    if len(watchTitleList) == 0:
        return;
    for idx, title in enumerate(watchTitleList):
        try:    
            result = dict()
            price = str(watchPriceList[idx].getText())
            titleText = title.getText().replace('\r','').replace('\n','').replace('\t','').replace('ROLEX','').replace('rolex','').replace('勞力士','')
            result['title'] = titleText
            result['highlight'] = str(watchTitleHighlightList[idx].getText())
            result['price'] = price
            watchList.append(result)
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))



if __name__ == '__main__':
    print(getWatchPrice())  # 或是任何你想執行的函式
    # testNumber = ['aaa','bbb','ccc','ddd','eee']
    # for idx, x in enumerate(testNumber):
    #     print(idx, x)

        