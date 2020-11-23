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
chatIdList = [919045167]  #要放送給誰

dateStr=datetime.datetime.now().strftime("%Y%m%d")

def sendMessage(msg):
    for chat_id in chatIdList:
        print(msg)
        bot.sendMessage(chat_id, msg, parse_mode='html',disable_web_page_preview=True)

def sendImage(image):
    for chat_id in chatIdList:
        bot.send_photo(chat_id=chat_id, photo=image)

def sendThree():
    threeData = getNewThree()
    str = dateStr + '三大法人買賣超\n'
    if(len(threeData)!=0):
        for three in threeData:
            tempStr = " ".join(three)
            str = str + tempStr + '\n'
        sendMessage('<pre>' + str + '</pre>')

def getNewThree():
    fail = True
    while fail:
        threeList = three.getThree('20201124')
        return threeList['data']

sendThree()