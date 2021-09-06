import getStockThree as three
import datetime
import telegramBot
import getDb
import prettytable as pt

dateStr = datetime.datetime.now().strftime("%Y%m%d")


def getDayStockThreeBuySell():
    threeStockList = three.getDayStockThreeBuySell(dateStr)
    if(len(threeStockList) != 0):
        title = dateStr + '- 三大法人個股買賣超\n'
        tb1 = pt.PrettyTable()  
        tb1.set_style(pt.PLAIN_COLUMNS)
        col1 = 'Stock-代碼'
        col2 = '買賣超張數'
        tb1.field_names = [col1,col2]
        tb1.align[col1] = "l"
        tb1.align[col2] = "r"
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
        converterBuySellList('****買超****', overbuyList, tb1)
        converterBuySellList('****賣超****', overSellList, tb1)
        converterBuySellList('****無變化****', noneList, tb1)
        tbStr = title +'<pre>' + tb1.get_string() + '</pre>'
        telegramBot.sendMessage(tbStr)
    else:
        print(dateStr + '查無資料')
    

def converterBuySellList(title, stockList, tb1):
    if(len(stockList) > 0):
        tb1.add_row(['<code>' + title + '</code>', ''])
        for stock in stockList:
            stockName = '<code>' + stock[0] + '-' + stock[1]+ '</code>'
            stockName = stockName.replace(' ','')
            buySell = converterNumber(stock[18])
            buySellText = '<b>' + buySell + '張</b>'
            tb1.add_row([stockName, buySellText])


def converterNumber(number):
    converterNumber = round(int(number.replace(',', '')) / 1000 , 1)
    prefix = ''
    if(converterNumber>0):
        prefix = '➕'
    elif(converterNumber<0):
        prefix = '➖'
    converterNumber = str(converterNumber).replace('-','')
    return prefix + converterNumber


if __name__ == '__main__':
    getDayStockThreeBuySell()