import getYfinance as yFinanceApi
import datetime
from datetime import timedelta, date
import telegramBot
import getDb
import prettytable as pt

def sendYfinance():
    fredData = yFinanceApi.getYfIndexData()
    lastSendDate = getDb.getLastSendDate('LAST_US_MARKET_SEND_DATE')
    newUpdateDate = fredData[0]['lastUpdateDate']
    tb1 = pt.PrettyTable()
    tb1.set_style(pt.PLAIN_COLUMNS)
    
    if(lastSendDate != newUpdateDate):
        title = str(newUpdateDate) + '美股指數收盤價'
        col1 = '指數名稱'
        col2 = '昨收'
        tb1.field_names = [col1,col2]
        tb1.align[col1] = "l"
        tb1.align[col2] = "l"
        for data in fredData:
            indexTitle = data['title'][:6]
            indexValue = data['value'] + '('+  data['indexGap'] + ' | ' +  data['gapPercent'] + ')'
            tb1.add_row([indexTitle , indexValue])

        tbStr = '<b>' +  title +'</b>\n' + tb1.get_string() + ''
        # print(tbStr)
        # 測試用這個 
        # telegramBot.newSendMessage(tbStr, '919045167')

        telegramIds = getDb.getUsTelegramIds()
        for id in telegramIds:
            telegramBot.newSendMessage(tbStr, id)

        getDb.updateLastSendDate(fredData[0]['lastUpdateDate'], 'LAST_US_MARKET_SEND_DATE')

    else:
        print('已發送過')

        
if __name__ == '__main__':
    sendYfinance()