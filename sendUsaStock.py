import getYfinance as yFinanceApi
import datetime
from datetime import timedelta, date
import telegramBot
import getDb
import prettytable as pt

def sendUsaStock():
    usaData = yFinanceApi.getYfStockData()
    lastSendDate = getDb.getLastSendDate('LAST_US_STOCK_SEND_DATE')
    newUpdateDate = usaData[0]['lastUpdateDate']
    tb1 = pt.PrettyTable()
    tb1.set_style(pt.PLAIN_COLUMNS)
    
    if(lastSendDate != newUpdateDate):
        title = str(newUpdateDate) + '美股個股收盤價'
        col1 = '股票名稱'
        col2 = '昨收'
        tb1.field_names = [col1,col2]
        tb1.align[col1] = "l"
        tb1.align[col2] = "l"
        for data in usaData:
            indexTitle = data['title'][:6]
            indexValue = data['value'] + '('+  data['indexGap'] + ' | ' +  data['gapPercent'] + ')'
            tb1.add_row([indexTitle , indexValue])

        tbStr = '<b>' +  title +'</b>\n' + tb1.get_string() + ''
        # 測試用這個 
        # telegramBot.newSendMessage(tbStr, '919045167')

        telegramIds = getDb.getUsTelegramIds()
        for id in telegramIds:
            telegramBot.newSendMessage(tbStr, id)
            
        getDb.updateLastSendDate(usaData[0]['lastUpdateDate'], 'LAST_US_STOCK_SEND_DATE')

    else:
        print('已發送過')

        
if __name__ == '__main__':
    sendUsaStock()