# pythonTelegramBot

### python Telegram Bot

#### 已完成功能

* bot 註冊(將資訊存入DB 並每日抓取發送)
* 發送每日收盤資訊(個股收盤價、三大法人買賣超、三大法人個股買賣超)

#### 未完成功能

* 根據不同USER 發送不同追蹤的股票資訊

*

#### 指令

* /start 開始訂閱機器人(會收到訊息)
* /end 取消訂閱機器人

```bash
pip install python-telegram-bot --upgrade
pip install configparser
pip install dataframe-image
pip install tabulate
pip install tabulate
pip install prettytable
pip install pyTelegramBotAPI
pip install fredapi
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
FRED_API_KEY=YOUR FRED API KEY 自己去fred網站辦帳號拿KEY
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

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>fileName</th>
      <th>Schedule說明</th>
      <th>執行時間</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>sendStockDayPrice.py</td>
      <td>個股收盤價</td>
      <td>每天14:00</td>
    </tr>
    <tr>
      <td>sendThree.py</td>
      <td> 三大法人買賣超</td>
      <td>每天15:00</td>
    </tr>
    <tr>
      <td>sendStockBuySell.py</td>
      <td>三大法人個股買賣超</td>
      <td>每天16:30</td>
    </tr>
    <tr>
      <td>sendFred.py</td>
      <td>美股三大指數收盤</td>
      <td>每天08:30</td>
    </tr>
  </tbody>
</table>

### 參考資料

* [telebot教學影片](https://youtu.be/NwBWW8cNCP4)

```
在裡面看到可以使用這種方法攔截接收訊息 就不用再做一個webhook了
@bot.message_handler(commands=['start'])
```

### Table語法

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
);

INSERT INTO public.system_parameter(name,value,update_on)
VALUES ('LAST_FRED_SEND_DATE', '0', now()) 
,('LAST_US_MARKET_SEND_DATE', '0', now())
,('LAST_US_STOCK_SEND_DATE', '0', now())
,('LAST_CRYPTO_SEND_DATE', '0', now())

update system_parameter set value = '0' where name = 'LAST_CRYPTO_SEND_DATE';
update system_parameter set value = '0' where name = 'LAST_US_MARKET_SEND_DATE';

update accounts set telegram_push_crypto_enabled
 = true where telegram_push_enabled = true;
 ```

### 已解決問題

* 有時三大法人資料會延遲 導致沒抓到資料 預計解法為 各個排成都要有一個當日有無發送成功的紀錄(未成功就要一直發)
    問題為不想一直跑排程

### 尚未開發完成功能
* 根據個人去區分follow_stock

