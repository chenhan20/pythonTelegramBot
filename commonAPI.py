import pandas as pd
import json
import requests
import time
import datetime
import telegramBot

# 偽瀏覽器
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def getWeekStartDate():
    
    url = 'https://www.twse.com.tw/fund/getTWT54UDWeekArray'
    res = requests.get(url, headers=headers)
    data = json.loads(res.text)

    if data['stat'] == 'OK':
        return data['date']
    else:
        print(data['stat'])
        return []



def test():
    getWeekStartDate()

if __name__ == '__main__':
    test()
