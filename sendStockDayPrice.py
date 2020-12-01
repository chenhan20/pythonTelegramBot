import getStockThree as three
import datetime
import telegramBot

dateStr = datetime.datetime.now().strftime("%Y%m%d")


def sendStockDayPrice():
    stockPriceList = three.getStockPrice(dateStr)
    if(len(stockPriceList) != 0):
        str = dateStr + '個股收盤\n'
        for stock in stockPriceList:
            stockName = '<code>' + stock[0] + '(' + stock[1]+ ')</code>'
            price = stock[8]
            chgPrefix = converterPrefix(stock[9])
            chg = stock[10]
            strTemp = stockName + '：<b>' + price + '</b>(' + chgPrefix + chg  +')\n'
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
    sendStockDayPrice()