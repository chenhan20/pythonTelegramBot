import getStockThree as three
import datetime
import telegramBot

dateStr = datetime.datetime.now().strftime("%Y%m%d")


def sendStockDayPrice():
    stockDayData = three.getStockDayDetail(dateStr)
    stockPriceList = stockDayData['stockPriceLsit']
    dayList = stockDayData['dayList']
    upDown = stockDayData['upDown']
    if(len(stockPriceList) != 0):
        upList = []
        downList = []
        noneList = []
        sendStr = dateStr + '收盤資訊\n'
        for stock in stockPriceList:
            prefix = stock[9]
            if(prefix == '<p style= color:red>+</p>'):
                upList.append(stock)
            elif(prefix == '<p style= color:green>-</p>'):
                downList.append(stock)
            else:
                noneList.append(stock)

        sendStr = sendStr + converterDayList(dayList)
        sendStr = sendStr + converterupDown(upDown)
        sendStr = sendStr + converterStockList('-📈📈📈漲📈📈📈- ', upList)
        sendStr = sendStr + converterStockList('-〽〽〽跌〽〽〽- ', downList)
        sendStr = sendStr + converterStockList('-💨💨無變化💨💨- ', noneList)
        telegramBot.sendMessage(sendStr)
    else:
        print(dateStr + '查無資料')


def converterPrefix(prefix):
    converterPrefix = ''
    if(prefix.find('color:red')!=-1):
        converterPrefix = '🔺'
    elif(prefix.find('color:green')!=-1):
        converterPrefix = '🔻'
    return converterPrefix


def converterStockList(title, stockList):
    str = ''
    if(len(stockList) > 0):
        str += '<code>' + title + '</code>\n'
        for stock in stockList:
            stockName = '<a href="https://www.wantgoo.com/stock/' + stock[0] +'">' + stock[0] + stock[1] + '</a>'
            price = stock[8].replace(',', '')
            chgPrefix = converterPrefix(stock[9])
            chg = stock[10]
            chgPercent = float(chg) / float(price) * 100
            chgText = '(' + chgPrefix + chg + ' | {:.2f}%'.format(chgPercent) + ')'
            strTemp = stockName + ':<b>' + price + '</b>' + chgText
            str = str + strTemp + '\n'
    return str
    
def converterDayList(dayList):
    str = ''
    if(len(dayList) > 0):
        for stock in dayList:
            stockName = '<a href="https://www.wantgoo.com/stock/0000">加權指數</a>'
            chgPrefix = converterPrefix(stock[2])
            price = stock[1]
            chg = stock[3]
            chgPercent = float(stock[4])
            chgText = '(' + chgPrefix + chg + ' | {:.2f}%'.format(chgPercent) + ')'
            strTemp = stockName + ':<b>' + price  + '</b>' + chgText
            str = str + strTemp + '\n'
    return str

def converterupDown(upDown):
    str = ''
    if(len(upDown) > 0):
        for stock in upDown:
            stockName = '<a href="https://www.wantgoo.com/stock/advance-decline-line">' + stock[0] + '</a>:'
            str += stockName + '<b>' + stock[2]  + '</b>' + '家\n'

    return str


if __name__ == '__main__':
    sendStockDayPrice()
