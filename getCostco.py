import asyncio
import requests
import json
import prettytable as pt
import datetime
import telegramBot

url = 'https://www.costco.com.tw/rest/v2/taiwan/products/search?fields=FULL&query=&pageSize=100&category=hot-buys&lang=zh_TW&curr=TWD'
now = datetime.datetime.now()


async def getData():
    response = requests.get(url)
    if response.status_code != 200:
        return []

    costcoData = json.loads(response.text)
    products = costcoData['products']
    data_list = []
    # 印出所有商品資訊
    for product in products:
        coupon = product.get('couponDiscount')
        if coupon is not None:
            try:
                data_list.append({
                    'title': product['name'],
                    'price': product['basePrice']['formattedValue'],
                    'discount': coupon['discountValue'],
                    'result': product['basePrice']['value'] - coupon['discountValue']
                })
            except Exception as e:
                continue

    toTxt(data_list)

    sendIds = ['919045167','1471601802']
    for sendId in sendIds:
        file = open('costcoPrice.txt', 'rb')
        await telegramBot.sendFile(sendId, file)


def toTxt(costcoData):
    tb1 = pt.PrettyTable()
    tb1.set_style(pt.PLAIN_COLUMNS)
    col1 = '名稱'
    col2 = '價格 | 折扣 | 結果'
    tb1.field_names = [col1, col2]
    tb1.align[col1] = "l"
    tb1.align[col2] = "l"
    dateStr = now.strftime("%Y%m%d")
    // TEST COMMIT
    title = f'{dateStr} - COSTCO 特價商品'

    for data in costcoData:
        try:
            indexTitle = data['title']
            indexValue = f"{data['price']} | {data['discount']} | {data['result']}"
            tb1.add_row([indexTitle, indexValue])
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    tbStr = f'{title}\n{tb1.get_string()}'
    with open("costcoPrice.txt", "w+", encoding='UTF-8') as f:
        f.write(tbStr)


if __name__ == '__main__':
    asyncio.run(getData())
