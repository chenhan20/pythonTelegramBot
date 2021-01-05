import getStockThree as three
import datetime
import telegramBot

dateStr = datetime.datetime.now().strftime("%Y%m%d")


def sendStockDayPrice():
    stockPriceList = three.getStockPrice(dateStr)
    if(len(stockPriceList) != 0):
        upList = []
        downList = []
        noneList = []
        sendStr = dateStr + '個股收盤\n'
        for stock in stockPriceList:
            prefix = stock[9]
            if(prefix == '<p style= color:red>+</p>'):
                upList.append(stock)
            elif(prefix == '<p style= color:green>-</p>'):
                downList.append(stock)
            else:
                noneList.append(stock)

        sendStr = sendStr + converterStockList('- 📈📈📈漲📈📈📈 - ', upList)
        sendStr = sendStr + converterStockList('- 〽〽〽跌〽〽〽 - ', downList)
        sendStr = sendStr + converterStockList('- 💨💨無變化💨💨 - ', noneList)
        telegramBot.sendMessage(sendStr)
    else:
        print(dateStr + '查無資料')


def converterPrefix(prefix):
    converterPrefix = ''
    if(prefix == '<p style= color:red>+</p>'):
        converterPrefix = '🔺'
    elif(prefix == '<p style= color:green>-</p>'):
        converterPrefix = '🔻'
    return converterPrefix


def converterStockList(title, stockList):
    str = ''
    if(len(stockList) > 0):
        str += '<code>' + title + '</code>\n'
        for stock in stockList:
            stockName = '<a href="https://www.wantgoo.com/stock/' + stock[0] +'">' + stock[0] + stock[1] + '</a>'
            price = stock[8]
            chgPrefix = converterPrefix(stock[9])
            chg = stock[10]
            chgPercent = float(chg) / float(price) * 100
            chgText = '(' + chgPrefix + chg + ' | {:.2f}%'.format(chgPercent) + ')'
            strTemp = stockName + ':<b>' + price + '</b>' + chgText
            str = str + strTemp + '\n'
    return str


if __name__ == '__main__':
    sendStockDayPrice()
