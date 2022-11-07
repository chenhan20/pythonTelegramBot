import telegram
import configparser
import getStockThree as three
import datetime
import time
import pandas as pd
# import dataframe_image as dfi
import sys

config = configparser.ConfigParser()
config.sections()
config.read('setting.ini')

token = config['DEFAULT']['TOKEN']
bot = telegram.Bot(token=token)
chatIdList = [919045167]  # 要放送給誰 之後要抓DB(account.telegram_user_id)
steveTelegramId = 919045167
dateStr = datetime.datetime.now().strftime("%Y%m%d")


def sendMessage(msg):
    try:
        for chat_id in chatIdList:
            print(msg)
            bot.sendMessage(chat_id, msg, parse_mode='html',
                            disable_web_page_preview=True)
    except Exception as error:
        print ("發送失敗 Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

def newSendMessage(msg, telegramId):
    try:
        bot.sendMessage(telegramId, msg, parse_mode='html',
                disable_web_page_preview=True)
        print('ID:'  + telegramId + ' success!')
    except Exception as error:
        print ("發送失敗 Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

def newSendAnnouncementMessage(msg, telegramId):
    try:
        bot.sendMessage(telegramId, msg, parse_mode='html',
                disable_web_page_preview=False)
    except Exception as error:
        print ("發送失敗 Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

def sendImage(image):
    for chat_id in chatIdList:
        bot.send_photo(chat_id=chat_id, photo=image)

def sendMessageForSteve(msg):
    try:
        print(msg)
        bot.sendMessage(steveTelegramId, msg, parse_mode='html',
                disable_web_page_preview=True)
    except Exception as error:
        print ("發送失敗 Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))


def sendFile(chat_id,file):
    try:
        bot.send_document(chat_id=chat_id,document=file)
    except Exception as error:
        print ("發送失敗 Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

