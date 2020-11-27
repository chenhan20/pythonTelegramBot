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


sendThree()
