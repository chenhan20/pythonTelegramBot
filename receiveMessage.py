import telebot
from telebot import types
import configparser
import getDb
import announcement
import telegramBot

config = configparser.ConfigParser()
config.sections()
config.read('setting.ini')

token = config['DEFAULT']['TOKEN']
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start (message):
    fromUser = message.from_user
    print(fromUser.last_name + fromUser.first_name + '(' + str(fromUser.id) + ') : ' + message.text)
    bot.reply_to(message,  str.format("Hi! {}歡迎你使用SteveBot 服務 \n今日起將會收到全球股市資訊 若不想再收到 請輸入\n/end", fromUser.first_name))
    isNewUser = getDb.addUser(fromUser)
    if isNewUser:
        telegramBot.sendMessageForSteve('[ADMIN] new accounts name:' + fromUser.first_name)


@bot.message_handler(commands=['end'])
def end (message):
    fromUser = message.from_user
    print(fromUser.last_name + fromUser.first_name + '(' + str(fromUser.id) + ') : ' + message.text)
    bot.reply_to(message,  str.format("Thank! {} 感謝你的使用 已暫停所有訂閱通知 若想再收到 請輸入\n/start 或是個別訂閱", fromUser.first_name))
    getDb.removeUser(fromUser)

@bot.message_handler(commands=['startTW'])
def start (message):
    fromUser = message.from_user
    print(fromUser.last_name + fromUser.first_name + '(' + str(fromUser.id) + ') : ' + message.text)
    bot.reply_to(message,  str.format("Hi! {} \n今日起將會收到台股資訊 若不想再收到 請輸入\n/endTW", fromUser.first_name))
    getDb.enabledTw(fromUser, True)

@bot.message_handler(commands=['endTW'])
def end (message):
    fromUser = message.from_user
    print(fromUser.last_name + fromUser.first_name + '(' + str(fromUser.id) + ') : ' + message.text)
    bot.reply_to(message,  str.format("Thank you! {} 感謝你的使用 已暫停台股訂閱通知 若想再收到 請輸入\n/startTW 或是全部訂閱/start", fromUser.first_name))
    getDb.enabledTw(fromUser, False)

@bot.message_handler(commands=['startUS'])
def start (message):
    fromUser = message.from_user
    print(fromUser.last_name + fromUser.first_name + '(' + str(fromUser.id) + ') : ' + message.text)
    bot.reply_to(message,  str.format("Hi! {} \n今日起將會收到美股資訊 若不想再收到 請輸入\n/endUS", fromUser.first_name))
    getDb.enabledUs(fromUser, True)

@bot.message_handler(commands=['endUS'])
def end (message):
    fromUser = message.from_user
    print(fromUser.last_name + fromUser.first_name + '(' + str(fromUser.id) + ') : ' + message.text)
    bot.reply_to(message,  str.format("Thank you! {} 感謝你的使用 已暫停美股訂閱通知 若想再收到 請輸入\n/startUS 或是全部訂閱\n/start", fromUser.first_name))
    getDb.enabledUs(fromUser, False)

@bot.message_handler(commands=['startCrypto'])
def start (message):
    fromUser = message.from_user
    print(fromUser.last_name + fromUser.first_name + '(' + str(fromUser.id) + ') : ' + message.text)
    bot.reply_to(message,  str.format("Hi! {} \n今日起將會收到加密貨幣資訊 若不想再收到 請輸入\n/endCrypto", fromUser.first_name))
    getDb.enabledCrypto(fromUser, True)

@bot.message_handler(commands=['endCrypto'])
def end (message):
    fromUser = message.from_user
    print(fromUser.last_name + fromUser.first_name + '(' + str(fromUser.id) + ') : ' + message.text)
    bot.reply_to(message,  str.format("Thank you! {} 感謝你的使用 已暫停加密貨幣訂閱通知 若想再收到 請輸入\n/startCrypto 或是全部訂閱\n/start", fromUser.first_name))
    getDb.enabledCrypto(fromUser, False)
    
@bot.message_handler(commands=['announcement'])
def sendAnnouncement (message):
    fromUser = message.from_user
    if(fromUser.id == 919045167):
        announcementText = message.text.replace('/announcement ', '')
        announcement.send(announcementText)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    fromUser = message.from_user
    print(fromUser.last_name + fromUser.first_name + '(' + str(fromUser.id) + ') : ' + message.text)
    # TODO 預計要存到messageRecord table 紀錄訊息
	# bot.reply_to(message, message.text)

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