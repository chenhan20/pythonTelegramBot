import telegram
import configparser
import getStockThree as three
import datetime
import time
import pandas as pd
import dataframe_image as dfi

config = configparser.ConfigParser()
config.sections()
config.read('setting.ini')

token = config['DEFAULT']['TOKEN']
bot = telegram.Bot(token=token)
chatIdList = [919045167]  # 要放送給誰

dateStr = datetime.datetime.now().strftime("%Y%m%d")


def sendMessage(msg):
    for chat_id in chatIdList:
        print(msg)
        bot.sendMessage(chat_id, msg, parse_mode='html',
                        disable_web_page_preview=True)


def sendImage(image):
    for chat_id in chatIdList:
        bot.send_photo(chat_id=chat_id, photo=image)


def sendThree():
    threeData = getNewThree()
    str = dateStr + '三大法人買賣超\n'
    if(len(threeData['data']) != 0):
        str = str + threeData['fields'][0] + \
            ' : ' + threeData['fields'][3] + '\n'
        for three in threeData['data']:
            tempStr = three[0] + ' : ' + three[3]
            str = str + tempStr + '\n'
        sendMessage('<pre>' + str + '</pre>')
    else:
        print(dateStr + '查無資料')


def getNewThree():
    threeList = three.getThree(dateStr)
    return threeList
    
def getStockThreeBuySell():
    threeStojckList = three.getStockThreeBuySell(dateStr)
    if(len(threeStojckList) != 0):
        str = dateStr + '三大法人個股買賣超\n'
        for stock in threeStojckList:
            stockName = stock[0] + '(' + stock[1]+ ')'
            buySell = converterNumber(stock[18])
            strTemp = stockName + buySell + '張\n'
            str = str + strTemp
        sendMessage('<pre>' + str.replace(' ', '') + '</pre>')
    else:
        print(dateStr + '查無資料')
    

def converterNumber(number):
    converterNumber = round(int(number.replace(',', '')) / 1000 , 1)
    prefix = ':'
    if(converterNumber>0):
        prefix = '➕買超:'
    elif(converterNumber<0):
        prefix = '➖賣超:'
    converterNumber = str(converterNumber).replace('-','')
    return prefix + converterNumber


# converterNumber('-6,242,004')
# getStockThreeBuySell()
# sendThree()
