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

dateStr = datetime.datetime.now().strftime("%Y%m%d")


def sendMessage(msg):
    for chat_id in chatIdList:
        print(msg)
        bot.sendMessage(chat_id, msg, parse_mode='html',
                        disable_web_page_preview=True)

def newSendMessage(msg, telegramId):
    print('ID:'  + telegramId + 'msg:' + msg)
    bot.sendMessage(telegramId, msg, parse_mode='html',
            disable_web_page_preview=True)

def newSendAnnouncementMessage(msg, telegramId):
    bot.sendMessage(telegramId, msg, parse_mode='html',
            disable_web_page_preview=False)

def sendImage(image):
    for chat_id in chatIdList:
        bot.send_photo(chat_id=chat_id, photo=image)

