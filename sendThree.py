import getStockThree as three
import datetime
import telegramBot
import getDb

dateStr = datetime.datetime.now().strftime("%Y%m%d")

def sendThree():
    threeData = three.getThree(dateStr)
    str = '<b>' + dateStr + '三大法人買賣超</b>\n'
    if(len(threeData['data']) != 0):
        str = str + threeData['fields'][0] + \
            ' : ' + threeData['fields'][3] + '\n'
        for data in threeData['data']:
            tempStr = ''
            if(data[0] != '合計'):
                tempStr += '<code>' + data[0] + '</code> : <b>' + data[3] + '</b>'
            else:
                tempStr += '--------------------------------------'
                tempStr += '\n<b>總買</b><code>' + data[1] + '</code>  <b>總賣</b><code>' + data[2] + '</code>'
                tempStr += '\n--------------------'
                tempStr += '\n| <code>' + data[0] + '</code> : <b>' + data[3] + '</b> |'
                tempStr += '\n--------------------'
                
            str = str + tempStr + '\n'
            
        # print(str)
        # 測試用這個 
        # telegramBot.newSendMessage(str, '919045167')

        telegramIds = getDb.getTelegramIds()
        for id in telegramIds:
            telegramBot.newSendMessage(str, id)
            
    else:
        print(dateStr + '查無資料')

        
if __name__ == '__main__':
    sendThree()