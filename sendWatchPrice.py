import datetime
from datetime import timedelta, date
import telegramBot
import prettytable as pt
import getWatchPrice as watchPrice
import openpyxl
import json



now = datetime.datetime.now()

def sendWatchPrice():
    isTest = True
    watchData = watchPrice.getWatchPrice()
    
    if not watchData.values:
        print('查無資料')
        return
    
    # txt暫時不開
    # toTxt(watchData.items())
    toExcel(watchData.items())
    toJSON(watchData)
    
    sendIds = ['919045167','1471601802']
    # 測試用這個
    if isTest:
        for sendId in sendIds:
            file = open('watchPrice.xlsx', 'rb')
            telegramBot.sendFile(sendId,file)
            file.close()
            # txt暫時不開
            # file = open('watchPrice.txt', 'rb')
            # telegramBot.sendFile(sendId,file)
            # file.close()
            # JSON暫時不開
            # file = open('watchPrice.json', 'rb')
            # telegramBot.sendFile(sendId,file)
            # file.close()

def toExcel(watchData):
    workbook = openpyxl.Workbook()
    sheetIndex = 0
    for key,watchList in watchData:
        textMaxLength = 0
        if sheetIndex != 0:
            workbook.create_sheet(key)
        sheet = workbook.worksheets[sheetIndex]
        sheet.title = key
        sheet['A1'].value = '價格'
        sheet['B1'].value = '名稱'
        for idx, data in enumerate(watchList):
            excelStartRow = idx+2
            indexTitle = data['title'] + data['highlight']
            if data['price'] == 999999999999:
                indexValue = '歡迎來電洽詢'
            else:
                indexValue = '$' + format(data['price'],',')
            sheet['A'+str(excelStartRow)] = indexValue
            sheet['B'+str(excelStartRow)] = indexTitle
            if(len(indexTitle) > textMaxLength):
                textMaxLength = len(indexTitle)
        sheet.column_dimensions['A'].width = textMaxLength * 1.5
        sheet.column_dimensions['B'].width = 15
        
        sheetIndex = sheetIndex+1
        
    # 儲存檔案
    workbook.save('watchPrice.xlsx')
    
    
def toJSON(watchData):
    # 儲存檔案
    # Writing to sample.json
    with open("watchPrice.json", "w", encoding='utf-8') as outfile:
        json.dump(watchData, outfile, ensure_ascii=False, indent=4)
    
    
def toTxt(watchData):
    tb1 = pt.PrettyTable()
    tb1.set_style(pt.PLAIN_COLUMNS)
    col1 = '名稱'
    col2 = '價格'
    tb1.field_names = [col1,col2]
    tb1.align[col1] = "l"
    tb1.align[col2] = "l"
    dateStr=now.strftime("%Y%m%d")
    title = dateStr + ' - ROLEX'
    
    for key,watchList in watchData:
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
    f= open("watchPrice.txt","w+", encoding='UTF-8')
    f.write(tbStr)
    f.close()
    
    
if __name__ == '__main__':
    sendWatchPrice()
