import getStockThree as three
import datetime
import telegramBot

dateStr = datetime.datetime.now().strftime("%Y%m%d")


def getStockThreeBuySell():
    threeStojckList = three.getStockThreeBuySell(dateStr)
    if(len(threeStojckList) != 0):
        str = dateStr + '三大法人個股買賣超\n'
        for stock in threeStojckList:
            stockName = stock[0] + '(' + stock[1]+ ')'
            buySell = converterNumber(stock[18])
            strTemp = stockName + buySell + '張\n'
            str = str + strTemp
        telegramBot.sendMessage('<pre>' + str.replace(' ', '') + '</pre>')
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