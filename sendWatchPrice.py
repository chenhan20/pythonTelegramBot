import datetime
from datetime import timedelta, date
import telegramBot
import prettytable as pt
import getWatchPrice as watchPrice

now = datetime.datetime.now()

def sendWatchPrice():
    isTest = True
    watchData = watchPrice.getWatchPrice()
    
    tb1 = pt.PrettyTable()
    tb1.set_style(pt.PLAIN_COLUMNS)
    dateStr=now.strftime("%Y%m%d")
    title = dateStr + '永生ROLEX報價'
    col1 = '名稱'
    col2 = '價格'
    tb1.field_names = [col1,col2]
    tb1.align[col1] = "l"
    tb1.align[col2] = "l"
    for data in watchData:
        indexTitle = data['title'][:25] + data['highlight']
        indexValue = '$' + data['price']
        tb1.add_row([indexTitle, indexValue])
    tbStr = '<b>' + title + '</b>\n' + tb1.get_string() + ''
    if isTest:
        # 測試用這個
        telegramBot.newSendMessage(tbStr, '919045167')
        telegramBot.newSendMessage(tbStr, '1471601802')


if __name__ == '__main__':
    sendWatchPrice()
