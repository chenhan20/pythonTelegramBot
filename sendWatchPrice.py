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
    
    if not watchData.values:
        print('查無資料')
        return

    title = dateStr + ' - ROLEX'
    for key,watchList in watchData.items():
        tb1.add_row(['===============', '==============='])
        tb1.add_row(['======= ' + key, ' ======='])
        tb1.add_row(['===============', '==============='])
        try:
            for data in watchList:
                indexTitle = data['title'] + data['highlight']
                if data['price'] == 999999999999:
                    indexValue = '歡迎來電洽詢'
                else:
                    indexValue = '$' + format(data['price'],',')
                tb1.add_row([indexTitle, indexValue])
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
    tbStr = '' + title + '\n' + tb1.get_string() + ''
    print(tbStr)
    f= open("watchPrice.txt","w+", encoding='UTF-8')
    f.write(tbStr)
    f.close()
    sendIds = ['919045167','1471601802']
    # 測試用這個
    if isTest:
        for sendId in sendIds:
            file = open('watchPrice.txt', 'rb')
            telegramBot.sendFile(sendId,file)
            file.close()

if __name__ == '__main__':
    sendWatchPrice()
