import telebot
import configparser
import getDb

config = configparser.ConfigParser()
config.sections()
config.read('setting.ini')

token = config['DEFAULT']['TOKEN']
bot = telebot.TeleBot(token)
chatIdList = [919045167]  # 要放送給誰 之後要抓DB(account.telegram_user_id)

@bot.message_handler(commands=['start'])
def start (message):
    fromUser = message.from_user
    print(fromUser)
    bot.reply_to(message,  str.format("Hi! {}歡迎你使用SteveBot 服務 \n今日起將會收到股市資訊 若不想在收到 請輸入/end", fromUser.username))
    getDb.addUser(fromUser)

@bot.message_handler(commands=['end'])
def start (message):
    fromUser = message.from_user
    print(fromUser)
    bot.reply_to(message,  str.format("Hi! {}已暫停訂閱通知 若想在收到 請輸入/start", fromUser.username))
    getDb.removeUser(fromUser)

if __name__ == '__main__':
    bot.polling()