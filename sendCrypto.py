import asyncio

import getYfinance as yFinanceApi
import telegramBot
import getDb
import prettytable as pt


async def sendCrypto():
    isTest = False
    cryptoData = yFinanceApi.getCryptoData()
    lastSendDate = getDb.getLastSendDate('LAST_CRYPTO_SEND_DATE')
    newUpdateDate = cryptoData[0]['lastUpdateDate']
    tb1 = pt.PrettyTable()
    tb1.set_style(pt.PLAIN_COLUMNS)

    if lastSendDate != newUpdateDate or isTest:
        title = str(newUpdateDate) + '加密貨幣價格'
        col1 = '貨幣名稱'
        col2 = '價格'
        tb1.field_names = [col1, col2]
        tb1.align[col1] = "l"
        tb1.align[col2] = "l"
        for data in cryptoData:
            indexTitle = data['title'][:6]
            indexValue = data['value'] + '(' + data['indexGap'] + ' | ' + data['gapPercent'] + ')'
            tb1.add_row([indexTitle, indexValue])

        tbStr = '<b>' + title + '</b>\n' + tb1.get_string() + ''

        if isTest:
            # 測試用這個
            await telegramBot.newSendMessage(tbStr, '919045167')
        else:
            telegramIds = getDb.getCryptoTelegramIds()
            for sendId in telegramIds:
                await telegramBot.newSendMessage(tbStr, sendId)
            getDb.updateLastSendDate(cryptoData[0]['lastUpdateDate'], 'LAST_CRYPTO_SEND_DATE')
    else:
        print('已發送過')


if __name__ == '__main__':
    asyncio.run(sendCrypto())

