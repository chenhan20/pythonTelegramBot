import getStockThree as three
import datetime
import telegramBot
import getDb
import prettytable as pt
import time

dateStr = datetime.datetime.now().strftime("%Y%m%d")
dateStr= '20220415'
# 初始次數
executionsCount = 0
# 最多call五次(30分鐘) 都沒資料就不發了
maxExecutionsCount = 5


def sendThree(count):
    isTest = False
    count = count + 1
    threeData = three.getThree(dateStr)
    tb1 = pt.PrettyTable()
    tb1.set_style(pt.PLAIN_COLUMNS)
    title = '' + dateStr + '三大法人買賣超'
    if len(threeData['data']) != 0:
        col1 = threeData['fields'][0]
        col2 = threeData['fields'][3]
        tb1.field_names = [col1, col2]
        tb1.align[col1] = "l"
        tb1.align[col2] = "r"
        for data in threeData['data']:
            if data[0] != '合計':
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
                tb1.add_row(['***********', '***********'])
                tb1.add_row(['Total Buy', 'Total Sell'])
                tb1.add_row([totalBuy, totalSell])
                tb1.add_row([dataCol_1, dataCol_2])
                tb1.add_row(['***********', '***********'])

        tbStr = title + '\n<pre>' + tb1.get_string() + '</pre>'

        if isTest:
            # 測試用這個
            telegramBot.newSendMessage(tbStr, '919045167')
        else:
            telegramIds = getDb.getTwTelegramIds()
            for telegramId in telegramIds:
                telegramBot.newSendMessage(tbStr, telegramId)
    else:
        print(dateStr + '查無資料')
        if count < maxExecutionsCount:
            time.sleep(300)
            sendThree(count)


if __name__ == '__main__':
    sendThree(executionsCount)
