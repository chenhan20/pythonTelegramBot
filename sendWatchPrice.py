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
    col1 = '名稱'
    col2 = '價格'
    tb1.field_names = [col1,col2]
    tb1.align[col1] = "l"
    tb1.align[col2] = "l"
    dateStr=now.strftime("%Y%m%d")

    title = dateStr + '永生ROLEX報價'
    for data in watchData:
        indexTitle = data['title'][:30] + data['highlight']
        indexValue = '$' + data['price'] + ''
        tb1.add_row([indexTitle, indexValue])
    tbStr = '' + title + '\n' + tb1.get_string() + ''
    f= open("watchPrice.txt","w+")
    f.write(tbStr)
    f.close()
    file = open('watchPrice.txt', 'rb')
    if isTest:
        # 測試用這個
        telegramBot.sendFile('919045167',file)
        telegramBot.sendFile('1471601802',file)
    file.close()


if __name__ == '__main__':
    sendWatchPrice()
