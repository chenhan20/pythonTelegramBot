import getStockThree as three
import datetime
import telegramBot

dateStr = datetime.datetime.now().strftime("%Y%m%d")


def getStockThreeBuySell():
    threeStockList = three.getStockThreeBuySell(dateStr)
    if(len(threeStockList) != 0):
        str = dateStr + '三大法人個股買賣超\n'
        for stock in threeStockList:
            stockName = '<code>' + stock[0] + '(' + stock[1]+ ')</code>'
            buySell = converterNumber(stock[18])
            strTemp = stockName + '<b>' + buySell + '張</b>\n'
            str = str + strTemp
        telegramBot.sendMessage(str.replace(' ', ''))
    else:
        print(dateStr + '查無資料')
    

def converterNumber(number):
    converterNumber = round(int(number.replace(',', '')) / 1000 , 1)
    prefix = ':'
    if(converterNumber>0):
        prefix = '➕買超:'
    elif(converterNumber<0):
        prefix = '➖賣超:'
    converterNumber = str(converterNumber).replace('-','')
    return prefix + converterNumber


if __name__ == '__main__':
    getStockThreeBuySell()