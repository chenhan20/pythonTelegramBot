import asyncio
import getStockThree as three
import datetime
import telegramBot
import getDb
import prettytable as pt
import time

dateStr = datetime.datetime.now().strftime("%Y%m%d")
# 最多call五次(30分鐘) 都沒資料就不發了
maxExecutionsCount = 5


async def getDayStockThreeBuySell(count):
    isTest = False
    count = count + 1
    threeStockList = three.getDayStockThreeBuySell(dateStr)
    if len(threeStockList) != 0:
        formatted_str = ""
        col1 = dateStr
        col2 = '三大法人個股買賣超'
        formatted_str += f"{col1} {' ' * (20 - len(col1))} {col2}\n"
        formatted_str += '-' * 50 + '\n'
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
        formatted_str += converterBuySellList('😺買超😺', overbuyList)
        formatted_str += converterBuySellList('🙀賣超🙀', overSellList)
        formatted_str += converterBuySellList('無變化', noneList)
        tbStr = '<pre>' + formatted_str + '</pre>'
        print(tbStr)
        if isTest:
            # 測試用這個
            await telegramBot.newSendMessage(tbStr, '919045167')
        else:
            telegramIds = getDb.getTwTelegramIds()
            for telegramId in telegramIds:
                await telegramBot.newSendMessage(tbStr, telegramId)
    else:
        print(dateStr + '查無資料')
        if count < maxExecutionsCount:
            time.sleep(300)
            await getDayStockThreeBuySell(count)


def converterBuySellList(title, stockList):
    formatted_str = ""
    if len(stockList) > 0:
        formatted_str += f"<code>{title}</code>\n"
        formatted_str += '-' * 20 + '\n'
        for stock in stockList:
            stockName = f"<code>{stock[0]}-{stock[1]}</code>".replace(' ', '')
            buySell = converterNumber(stock[18])
            buySellText = f"<b>{buySell}張</b>".replace(' ', '')
            formatted_str += f"{stockName} {' ' * (20 - len(stockName))} {buySellText}\n"
    return formatted_str

    # if len(stockList) > 0:
    #     tb1.add_row(['<code>' + title + '</code>', ''])
    #     tb1.add_row(['------------------', ''])
    #     for stock in stockList:
    #         stockName = '<code>' + stock[0] + '-' + stock[1] + '</code>'
    #         stockName = stockName.replace(' ', '')
    #         buySell = converterNumber(stock[18])
    #         buySellText = '<b>' + buySell + '張</b>'
    #         buySellText = buySellText.replace(' ', '')
    #         tb1.add_row([stockName, buySellText])


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
    asyncio.run(getDayStockThreeBuySell(0))

