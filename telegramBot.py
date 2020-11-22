import telegram

bot = telegram.Bot(token='')
chat_id = 919045167



def sendMessage(msg):
    bot.sendMessage(chat_id, msg, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)




