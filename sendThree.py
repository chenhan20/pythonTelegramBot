import getStockThree as three
import datetime
import telegramBot
import getDb

dateStr = datetime.datetime.now().strftime("%Y%m%d")

def sendThree():
    threeData = three.getThree(dateStr)
    str = dateStr + '三大法人買賣超\n'
    if(len(threeData['data']) != 0):
        str = str + threeData['fields'][0] + \
            ' : ' + threeData['fields'][3] + '\n'
        for data in threeData['data']:
            tempStr = '<code>' + data[0] + '</code> : <b>' + data[3] + '</b>'
            str = str + tempStr + '\n'

        telegramIds = getDb.getTelegramIds()
        for id in telegramIds:
            telegramBot.newSendMessage(str, id)
    else:
        print(dateStr + '查無資料')

        
if __name__ == '__main__':
    sendThree()