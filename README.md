# pythonTelegramBot

### python Telegram Bot

#### 已完成功能
* bot 註冊(將資訊存入DB 並每日抓取發送) 
* 發送每日收盤資訊(個股收盤價、三大法人買賣超、三大法人個股買賣超)
#### 未完成功能
* 根據不同USER 發送不同追蹤的股票資訊


```bash
pip install python-telegram-bot --upgrade
pip install configparser
pip install dataframe-image
pip install tabulate
pip install tabulate
pip install prettytable

```

------------

### 需新建 setting.ini 內容為

```bash
[DEFAULT]
TOKEN = YOUR BOT TOKEN
DATABASE = YOUR BOT DATABASE
USER = YOUR BOT USER
PASSWORD = YOUR BOT PASSWORD
PORT = YOUR BOT PORT
```

------------

### 若部屬至heroku

token改為這樣取 然後heroku要設定
Settings -> Config Vars -> 新增一個**key = TOKEN ,value = 你的TOKEN** 填寫自己bot的TOKEN

heroku上面的是使用SSL連線 不需要那麼多資訊 只要Heroku上面的url就行(因為在同一包內)

``` base
token = os.environ['TOKEN']
databaseUrl = os.environ['DATABASE_URL']
```

------------

### 設定排程

heroku Scheduled 
*是使用UTC時間 記得要轉換*  
| name | 說明  | 時間 | 
|---|---|---|
| sendStockDayPrice.py  | 個股收盤價  | 設定下午兩點  | 
| sendThree.py  | 三大法人買賣超  | 設定下午三點  | 
| sendStockBuySell.py  |  三大法人個股買賣超 | 設定下午四點半  |


### 參考資料

- telebot教學影片[https://youtu.be/NwBWW8cNCP4]

 ```sql
INSERT INTO public.follow_stock(user_id,stock_code)
VALUES 
    (1, '2330'),
    (1, '2377'),
    (1, '2308'),
    (1, '2382'),
    (1, '2886'),
    (1, '2603'),
    (1, '2609'),
    (1, '2606'),
    (1, '2615');
 ```
