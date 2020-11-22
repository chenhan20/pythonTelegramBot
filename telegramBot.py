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
chat_id = 919045167  #要放送給誰

def sendMessage(msg):
    bot.sendMessage(chat_id, msg, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

def sendImage(image):
    bot.send_photo(chat_id=chat_id, photo=image)

def sendThree():
    threeData = getNewThree()
    # sendMessage('asd')
    image = dfi.export(threeData,'three.png')

    dfi.convert
    print(type(image))
    


def getNewThree():
    fail = True
    date = datetime.datetime.now()
    while fail:
        dateStr=date.strftime("%Y%m%d")
        threeList = three.getThree('20201120')
        if(len(threeList['data'])!=0):
            df = pd.DataFrame(threeList['data'],columns=threeList['fields'])
            pd.set_option('display.unicode.ambiguous_as_wide', True)
            pd.set_option('display.unicode.east_asian_width', True)
            fail = False
            return df
            # print('========================='+ date.strftime("%Y%m%d")+ '=========================')
            # print(df)
        else:
            print(dateStr + '抓取失敗')
            time.sleep(3) # 五秒內只能call三次 否則會被鎖
            date = date - datetime.timedelta(days=1)

sendThree()