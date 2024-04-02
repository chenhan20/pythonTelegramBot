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


async def sendMessage(msg):
    try:
        for chat_id in chatIdList:
            print(msg)
            await bot.sendMessage(chat_id, 
                                  msg, 
                                  parse_mode='html',
                                  disable_web_page_preview=True)
    except Exception as error:
        print("發送失敗 Oops! An exception has occurred:", error)
        print("Exception TYPE:", type(error))


async def newSendMessage(msg, telegramId):
    try:
        await bot.sendMessage(telegramId,
                              msg,
                              parse_mode='html',
                              disable_web_page_preview=True)
        print('ID:'  + telegramId + ' success!')
    except Exception as error:
        print("發送失敗 Oops! An exception has occurred:", error)
        print("Exception TYPE:", type(error))


async def newSendAnnouncementMessage(msg, telegramId):
    try:
        await bot.sendMessage(telegramId,
                              msg,
                              parse_mode='html',
                              disable_web_page_preview=False)
    except Exception as error:
        print("發送失敗 Oops! An exception has occurred:", error)
        print("Exception TYPE:", type(error))


async def sendImage(image):
    for chat_id in chatIdList:
        await bot.send_photo(chat_id=chat_id, photo=image)


async def sendMessageForSteve(msg):
    try:
        print(msg)
        await bot.sendMessage(steveTelegramId,
                              msg,
                              parse_mode='html',
                              disable_web_page_preview=True)
    except Exception as error:
        print("發送失敗 Oops! An exception has occurred:", error)
        print("Exception TYPE:", type(error))


async def sendFile(chat_id, file):
    try:
        await bot.send_document(chat_id=chat_id,
                                document=file)
    except Exception as error:
        print("發送失敗 Oops! An exception has occurred:", error)
        print("Exception TYPE:", type(error))

