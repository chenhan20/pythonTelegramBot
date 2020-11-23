# pythonTelegramBot

-- python Telegram Bot --

功能:發送圖片給加入bot的會員(目前訊息OK)

```bash
pip install python-telegram-bot --upgrade
pip install configparser
pip install dataframe-image
pip install tabulate
```

## 需新建 setting.ini 內容為

```bash
[DEFAULT]
TOKEN = YOUR BOT TOKEN

```

## 若部屬至heroku

token改為這樣取 然後heroku要設定
Settings -> Config Vars -> 新增一個**key = TOKEN ,value = 你的TOKEN** 填寫自己bot的TOKEN

```bash
token = os.environ['TOKEN']
```
