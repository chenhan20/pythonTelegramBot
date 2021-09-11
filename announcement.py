import telegramBot
import getDb

def announcement():
    announcementStr = '新增了訂閱功能輸入\n /start 開始訂閱 /end 結束訂閱 請有需要的用戶輸入/start'
    telegramIds = getDb.getTelegramIds()
    for id in telegramIds:
        telegramBot.newSendMessage(announcementStr, id)


if __name__ == '__main__':
    announcement()