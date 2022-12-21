import requests
import time
import telegramBot

sleepTime = 30
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

def callWikiUpdate(type):
    text1 = ''
    if type == 'single':
        text1 = '====官司結果====\n' + '*贊助抽獎遭控賄選：\n'+ '2016年3月23日，[[臺灣臺北地方檢察署|臺北地方檢察署]]認定刑事部分罪證不足，處分不起訴。<ref>{{Cite news|url=https://www.chinatimes.com/realtimenews/20160323002827-260402?chdtv|title=聯歡晚會提供腳踏車摸彩 蔣萬安被控賄選不起訴|author=陳志賢|work=中國時報|date=2016-03-23|archiveurl=https://web.archive.org/web/20160323051058/http://www.chinatimes.com/realtimenews/20160323002827-260402|archivedate=2022-07-25}}</ref>。\n' + '*遭控當選無效：\n' + '2016年5月30日，[[臺灣臺北地方法院|臺北地方法院]]駁回民事部份當選無效之訴，判決蔣萬安勝訴，認定當選有效。<ref name="auto">{{cite web|author=游凱翔|url=http://appweb.cna.com.tw/webm/menu/asoc/201605300110.aspx|title=遭對手提告當選無效 蔣萬安一審勝訴|publisher=中央社|date=2016-05-30|access-date=2016-05-31|archive-url=https://web.archive.org/web/20160630161829/http://appweb.cna.com.tw/webm/menu/asoc/201605300110.aspx|archive-date=2016-06-30|dead-url=no}}</ref>\n'
    else:
        text1 = '====官司結果====\n' + '*贊助抽獎遭控賄選：\n'+ '2016年3月23日，[[臺灣臺北地方檢察署|臺北地方檢察署]]認定刑事部分罪證不足，處分不起訴<ref>{{Cite news|url=https://www.chinatimes.com/realtimenews/20160323002827-260402?chdtv|title=聯歡晚會提供腳踏車摸彩 蔣萬安被控賄選不起訴|author=陳志賢|work=中國時報|date=2016-03-23|archiveurl=https://web.archive.org/web/20160323051058/http://www.chinatimes.com/realtimenews/20160323002827-260402|archivedate=2022-07-25}}</ref>。\n' + '*遭控當選無效：\n' + '2016年5月30日，[[臺灣臺北地方法院|臺北地方法院]]駁回民事部份當選無效之訴，判決蔣萬安勝訴，認定當選有效。<ref name="auto">{{cite web|author=游凱翔|url=http://appweb.cna.com.tw/webm/menu/asoc/201605300110.aspx|title=遭對手提告當選無效 蔣萬安一審勝訴|publisher=中央社|date=2016-05-30|access-date=2016-05-31|archive-url=https://web.archive.org/web/20160630161829/http://appweb.cna.com.tw/webm/menu/asoc/201605300110.aspx|archive-date=2016-06-30|dead-url=no}}</ref>\n'

    updateData = {
        'action': 'edit',
        'format':'json',
        'errorformat':'html',
        'errorlang':'zh-tw',
        'errorsuselocal':'1',
        'formatversion':'2',
        'title':'蔣萬安',
        'summary':'/* 官司結果 */',
        'text':text1,
        'section':'6',
        'token':'+\\'
    }

    response = requests.post('https://zh.m.wikipedia.org/w/api.php',headers=headers,data=updateData)
    if response.status_code != 200:
        telegramBot.newSendMessage(type + '更新失敗', '919045167')
    else
        telegramBot.newSendMessage(type '成功', '919045167')
    time.sleep(sleepTime)  # 增加間格 避免被鎖



if __name__ == '__main__':
    print(callWikiUpdate('single'))  # 或是任何你想執行的函式
    # testNumber = ['aaa','bbb','ccc','ddd','eee']
    # for idx, x in enumerate(testNumber):
    #     print(idx, x)

        