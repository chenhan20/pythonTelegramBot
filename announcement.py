import telegramBot
import getDb

def send(str):
    # announcementStr = 'https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/p843x403/241166647_10215683700765483_5680142497233979819_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=825194&_nc_ohc=0AkAabSuzGkAX8zGYWu&_nc_ht=scontent-tpe1-1.xx&oh=89244fcc75066b3752e88216db72d881&oe=61626121'
    telegramIds = getDb.getTelegramIds()
    # telegramIds = ['1471601802', '1888409915', '1695874598', '1900252524','1918213496', '919045167']
    # telegramIds = ['919045167']
    str = '<b>推播訊息</b>:\n' + str
    for id in telegramIds:
        telegramBot.newSendAnnouncementMessage(str, id)


if __name__ == '__main__':
    send('https://news.cnyes.com/news/id/4730000')