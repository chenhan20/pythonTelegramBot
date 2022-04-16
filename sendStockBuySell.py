import getStockThree as three
import datetime
import telegramBot
import getDb
import prettytable as pt
import time

dateStr = datetime.datetime.now().strftime("%Y%m%d")
dateStr = '20220415'
# 最多call五次(30分鐘) 都沒資料就不發了
maxExecutionsCount = 5


def getDayStockThreeBuySell(count):
    isTest = False
    count = count + 1
    threeStockList = three.getDayStockThreeBuySell(dateStr)
    if len(threeStockList) != 0:
        tb1 = pt.PrettyTable()
        tb1.set_style(pt.PLAIN_COLUMNS)
        col1 = dateStr
        col2 = '三大法人個股買賣超'
        tb1.field_names = [col1, col2]
        tb1.align[col1] = "l"
        tb1.align[col2] = "r"
        overbuyList = []
        overSellList = []
        noneList = []
        for stock in threeStockList:
            buySellNum = round(int(stock[18].replace(',', '')) / 1000, 1)
            if buySellNum > 0:
                overbuyList.append(stock)
            elif buySellNum < 0:
                overSellList.append(stock)
            else:
                noneList.append(stock)
        converterBuySellList('😺買超😺', overbuyList, tb1)
        converterBuySellList('🙀賣超🙀', overSellList, tb1)
        converterBuySellList('無變化', noneList, tb1)
        tbStr = '<pre>' + tb1.get_string() + '</pre>'

        if isTest:
            # 測試用這個
            telegramBot.newSendMessage(tbStr, '919045167')
        else:
            telegramIds = getDb.getTwTelegramIds()
            for telegramId in telegramIds:
                telegramBot.newSendMessage(tbStr, telegramId)
    else:
        print(dateStr + '查無資料')
        if count < maxExecutionsCount:
            time.sleep(300)
            getDayStockThreeBuySell(count)


def converterBuySellList(title, stockList, tb1):
    if len(stockList) > 0:
        tb1.add_row(['<code>' + title + '</code>', ''])
        tb1.add_row(['------------------', ''])
        for stock in stockList:
            stockName = '<code>' + stock[0] + '-' + stock[1] + '</code>'
            stockName = stockName.replace(' ', '')
            buySell = converterNumber(stock[18])
            buySellText = '<b>' + buySell + '張</b>'
            buySellText = buySellText.replace(' ', '')
            tb1.add_row([stockName, buySellText])


def converterNumber(number):
    converterNum = round(int(number.replace(',', '')) / 1000, 1)
    prefix = ''
    if converterNum > 0:
        prefix = '➕'
    elif converterNum < 0:
        prefix = '➖'
    converterNum = str(converterNum).replace('-', '')
    return prefix + converterNum


if __name__ == '__main__':
    getDayStockThreeBuySell(0)
