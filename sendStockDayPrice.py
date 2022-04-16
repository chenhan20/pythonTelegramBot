import getStockThree as three
import datetime
import telegramBot
import getDb
import time
import converterUtils

dateStr = datetime.datetime.now().strftime("%Y%m%d")


# 最多call五次(30分鐘) 都沒資料就不發了
maxExecutionsCount = 5


def sendStockDayPrice(count):
    isTest = False
    count = count + 1
    stockDayData = three.getStockDayDetail(dateStr)
    stockPriceList = stockDayData['stockPriceList']
    dayList = stockDayData['dayList']
    upDown = stockDayData['upDown']
    dayTotal = stockDayData['dayTotal']
    if len(stockPriceList) != 0:
        upList = []
        downList = []
        noneList = []
        sendStr = dateStr + '收盤資訊\n'
        for stock in stockPriceList:
            prefix = stock[9]
            if prefix == '<p style= color:red>+</p>':
                upList.append(stock)
            elif prefix == '<p style= color:green>-</p>':
                downList.append(stock)
            else:
                noneList.append(stock)

        sendStr = sendStr + converterDayTotal(dayTotal)
        sendStr = sendStr + converterDayList(dayList)
        sendStr = sendStr + converterUpDown(upDown)
        sendStr = sendStr + converterStockList('-📈📈📈漲📈📈📈- ', upList)
        sendStr = sendStr + converterStockList('-〽〽〽跌〽〽〽- ', downList)
        sendStr = sendStr + converterStockList('-💨💨無變化💨💨- ', noneList)

        if isTest:
            # 測試用這個
            telegramBot.newSendMessage(sendStr, '919045167')
        else:
            telegramIds = getDb.getTwTelegramIds()
            for telegramId in telegramIds:
                telegramBot.newSendMessage(sendStr, telegramId)
    else:
        print(dateStr + '查無資料')
        if count < maxExecutionsCount:
            time.sleep(300)
            sendStockDayPrice(count)


def converterPrefix(prefix):
    prefixEmoji = ''
    if prefix.find('color:red') != -1:
        prefixEmoji = '🔺'
    elif prefix.find('color:green') != -1:
        prefixEmoji = '🔻'
    return prefixEmoji


def converterStockList(title, stockList):
    converterStr = ''
    if len(stockList) > 0:
        converterStr += '<code>' + title + '</code>\n'
        for stock in stockList:
            stockName = '<a href="https://www.wantgoo.com/stock/' + stock[0] + '">' + stock[0] + stock[
                1] + '</a>'
            price = stock[8].replace(',', '')
            chgPrefix = converterPrefix(stock[9])
            chg = stock[10]
            chgPercent = float(chg) / float(price) * 100
            chgText = '(' + chgPrefix + chg + ' | {:.2f}%'.format(chgPercent) + ')'
            strTemp = stockName + ':<b>' + price + '</b>' + chgText
            converterStr = converterStr + strTemp + '\n'
    return converterStr


def converterDayTotal(dayTotal):
    converterStr = ''
    if len(dayTotal) > 0:
        for stock in dayTotal:
            stockName = '🔸🔸總成交量🔸🔸'
            price = converterUtils.converterNumber(stock[1])
            strTemp = stockName + ':<b>' + price + '</b>'
            converterStr = converterStr + strTemp + '\n'
    return converterStr


def converterDayList(dayList):
    converterStr = ''
    if len(dayList) > 0:
        for stock in dayList:
            stockName = '<a href="https://www.wantgoo.com/stock/0000">加權指數</a>'
            chgPrefix = converterPrefix(stock[2])
            price = stock[1]
            chg = stock[3]
            chgPercent = float(stock[4])
            chgText = '(' + chgPrefix + chg + ' | {:.2f}%'.format(chgPercent) + ')'
            strTemp = stockName + ':<b>' + price + '</b>' + chgText
            converterStr = converterStr + strTemp + '\n'
    return converterStr


def converterUpDown(upDown):
    converterStr = ''
    if len(upDown) > 0:
        for stock in upDown:
            stockName = '<a href="https://www.wantgoo.com/stock/advance-decline-line">' + stock[0] + '</a>:'
            converterStr += stockName + '<b>' + stock[2] + '</b>' + '家\n'

    return converterStr


if __name__ == '__main__':
    sendStockDayPrice(0)
    # sendStockDayPriceForUser()
