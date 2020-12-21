import getStockThree as three
import datetime
import telegramBot

dateStr = datetime.datetime.now().strftime("%Y%m%d")


def sendStockDayPrice():
    stockPriceList = three.getStockPrice('20201221')
    if(len(stockPriceList) != 0):
        str = dateStr + '個股收盤\n'
        for stock in stockPriceList:
            stockName = '<code>' + stock[0] + '(' + stock[1]+ ')</code>'
            price = stock[8]
            chgPrefix = converterPrefix(stock[9])
            chg = stock[10]
            chgPercent = float(chg) / float(price) * 100
            strTemp = stockName + '：<b>' + price + '</b>[' + chgPrefix + chg  +'][{:.2f}%'.format(chgPercent) +']\n'
            str = str + strTemp
        telegramBot.sendMessage(str.replace('', ''))
    else:
        print(dateStr + '查無資料')
    

def converterPrefix(prefix):
    converterPrefix = ''
    if(prefix=='<p style= color:red>+</p>'):
        converterPrefix='🔺'
    elif(prefix=='<p style= color:green>-</p>'):
        converterPrefix='🔻'
    return converterPrefix
        

if __name__ == '__main__':
    # chg = "9.0"
    # price = "708.00"
    
    print("go")
    # print(float(price))
    # print('percent: {:.2f}%'.format(float(chg)/float(price)*100))
    sendStockDayPrice()