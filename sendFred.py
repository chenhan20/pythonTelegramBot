import getFredAPI as fredApi
import datetime
from datetime import timedelta, date
import telegramBot
import getDb
import prettytable as pt

yesterdayDate = date.today()  - timedelta(days=1)
# yesterdayDate = datetime.date(2021, 10, 2) - timedelta(days=1)

def sendFred():
    fredData = fredApi.getFredAPI(yesterdayDate)
    tb1 = pt.PrettyTable()
    tb1.set_style(pt.PLAIN_COLUMNS)
    title = str(yesterdayDate) + '美股指數收盤價'
    
    if(len(fredData) != 0):
        print(fredData)
        col1 = '指數名稱'
        col2 = '昨收'
        tb1.field_names = [col1,col2]
        tb1.align[col1] = "l"
        tb1.align[col2] = "r"
        for data in fredData:
            indexTitle = data['title']
            indexValue = data['value'] + '(' +  data['percent'] + ')'
            tb1.add_row([indexTitle, indexValue])

        tbStr = '<b>' +  title +'</b>\n<pre>' + tb1.get_string() + '</pre>'

        # print(tbStr)
        # 測試用這個 
        # telegramBot.newSendMessage(tbStr, '919045167')

        telegramIds = getDb.getUsTelegramIds()
        for id in telegramIds:
            telegramBot.newSendMessage(tbStr, id)
            
    else:
        print(str(yesterdayDate) + '查無資料')

        
if __name__ == '__main__':
    sendFred()