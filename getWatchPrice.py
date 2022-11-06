import requests
from bs4 import BeautifulSoup


def getWatchPrice():
    url = 'http://www.egps.com.tw/products.asp?subcat=350&type=open'
    response = requests.get(url)
    response.encoding = 'big5'
    soup = BeautifulSoup(response.text, "html.parser")
    watchTitleList = soup.find_all(attrs={"class":"a_table_list_txt"})
    watchPriceList = soup.select('span.shopping_Price')
    watchTitleHighlightList = soup.select('.a_table_list_txt font')
    watchList = []
    for idx, title in enumerate(watchTitleList):
        result = dict()
        price = str(watchPriceList[idx].getText())
        titleText = title.getText().replace('\r','').replace('\n','').replace('\t','').replace('ROLEX','').replace('rolex','').replace('勞力士','')
        result['title'] = titleText
        result['highlight'] = str(watchTitleHighlightList[idx].getText())
        result['price'] = price
        watchList.append(result)
    print(watchList)
    return watchList
    



if __name__ == '__main__':
    getWatchPrice()  # 或是任何你想執行的函式
    # testNumber = ['aaa','bbb','ccc','ddd','eee']
    # for idx, x in enumerate(testNumber):
    #     print(idx, x)

        