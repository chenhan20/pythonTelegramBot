import getStockThree as three
import datetime
import telegramBot

dateStr = datetime.datetime.now().strftime("%Y%m%d")


def getStockThreeBuySell():
    threeStockList = three.getStockThreeBuySell(dateStr)
    if(len(threeStockList) != 0):
        sendStr = dateStr + '- 三大法人個股買賣超\n'
        overbuyList = []
        overSellList = []
        noneList = []
        for stock in threeStockList:
            buySellNum = round(int(stock[18].replace(',', '')) / 1000 , 1)
            if(buySellNum>0):
                overbuyList.append(stock)
            elif(buySellNum<0):
                overSellList.append(stock)
            else:
                noneList.append(stock)
        if(len(overbuyList) > 0):
            sendStr = sendStr + converterBuySellList('　　😁買超😁', overbuyList)
        if(len(overSellList) > 0):
            sendStr = sendStr + converterBuySellList('　　😥賣超😥', overSellList)
        if(len(noneList) > 0):
            sendStr = sendStr + converterBuySellList('　　😑無變化😑', noneList)
        telegramBot.sendMessage(sendStr.replace(' ', ''))
    else:
        print(dateStr + '查無資料')
    

def converterBuySellList(title, stockList):
    str = '<code>' + title + '</code>\n'
    for stock in stockList:
        stockName = '<code>' + stock[0] + '(' + stock[1]+ ')</code>'
        buySell = converterNumber(stock[18])
        strTemp = stockName + '<b>' + buySell + '張</b>\n'
        str = str + strTemp
    return str


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