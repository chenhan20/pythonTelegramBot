import getStockThree as three
import datetime
import telegramBot
import getDb
import prettytable as pt

dateStr = datetime.datetime.now().strftime("%Y%m%d")

def sendThree():
    threeData = three.getThree(dateStr)
    tb1 = pt.PrettyTable()
    tb1.set_style(pt.PLAIN_COLUMNS)
    title = '' + dateStr + '三大法人買賣超'
    if(len(threeData['data']) != 0):
        col1 = threeData['fields'][0]
        col2 = threeData['fields'][3]
        tb1.field_names = [col1,col2]
        tb1.align[col1] = "l"
        tb1.align[col2] = "r"
        for data in threeData['data']:
            if(data[0] != '合計'):
                name = data[0].replace("(", "").replace(")", "");
                dataCol_1 = name[0:5]
                dataCol_2 = data[3]
                tb1.add_row([dataCol_1, dataCol_2])
            else:
                name = data[0].replace("(", "").replace(")", "");
                dataCol_1 = name[0:5]
                dataCol_2 = data[3]
                totalBuy = data[1].replace("+", "").replace("-", "");
                totalSell = data[2].replace("+", "").replace("-", "");
                tb1.add_row(['***********','***********'])
                tb1.add_row(['Total Buy','Total Sell'])
                tb1.add_row([totalBuy,totalSell])
                tb1.add_row([dataCol_1, dataCol_2])
                tb1.add_row(['***********','***********'])
                
        tbStr = title +'\n<pre>' + tb1.get_string() + '</pre>'

        # 測試用這個 
        # telegramBot.newSendMessage(tbStr, '919045167')

        telegramIds = getDb.getTwTelegramIds()
        for id in telegramIds:
            telegramBot.newSendMessage(tbStr, id)
            
    else:
        print(dateStr + '查無資料')

        
if __name__ == '__main__':
    sendThree()