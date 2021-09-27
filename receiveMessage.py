import telebot
from telebot import types
import configparser
import getDb
import announcement

config = configparser.ConfigParser()
config.sections()
config.read('setting.ini')

token = config['DEFAULT']['TOKEN']
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start (message):
    fromUser = message.from_user
    print(fromUser)
    bot.reply_to(message,  str.format("Hi! {}歡迎你使用SteveBot 服務 \n今日起將會收到股市資訊 若不想在收到 請輸入/end", fromUser.first_name))
    getDb.addUser(fromUser)

@bot.message_handler(commands=['end'])
def end (message):
    fromUser = message.from_user
    print(fromUser)
    bot.reply_to(message,  str.format("Hi! {}已暫停訂閱通知 若想在收到 請輸入/start", fromUser.first_name))
    getDb.removeUser(fromUser)

@bot.message_handler(commands=['announcement'])
def sendAnnouncement (message):
    fromUser = message.from_user
    if(fromUser.id == 919045167):
        announcementText = message.text.replace('/announcement ', '')
        announcement.send(announcementText)

# 手機板可以看到下方會有框可以選 之後來看要怎樣應用
@bot.message_handler(commands=['test'])
def test (message):
    print(message)
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('a')
    itembtnv = types.KeyboardButton('v')
    itembtnc = types.KeyboardButton('c')
    itembtnd = types.KeyboardButton('d')
    itembtne = types.KeyboardButton('e')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd, itembtne)
    bot.send_message(message.from_user.id, "Choose one letter:", reply_markup=markup)

if __name__ == '__main__':
    print('機器人已啟動')
    bot.polling()