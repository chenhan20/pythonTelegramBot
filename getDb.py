import psycopg2
import configparser


config = configparser.ConfigParser()
config.sections()
config.read('setting.ini')

database = config['DEFAULT']['DATABASE']
user = config['DEFAULT']['USER']
password = config['DEFAULT']['PASSWORD']
host = config['DEFAULT']['HOST']
port = config['DEFAULT']['PORT']


def getFollowStock(userId):

    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    print("Opened database successfully")
    cur = conn.cursor()
    postgreSQL_select_Query = "select * from follow_stock where user_id = %s"
    cur.execute(postgreSQL_select_Query, (userId,))

    rows = cur.fetchall()
    stockCodeList = [];
    for row in rows:
        stockCodeList.append(row[2])
        
    return stockCodeList



def getTelegramIds():

    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    print("Opened database successfully")
    cur = conn.cursor()
    postgreSQL_select_Query = "select * from accounts where telegram_push_enabled = true "
    cur.execute(postgreSQL_select_Query)

    rows = cur.fetchall()
    ids = [];
    for row in rows:
        ids.append(row[5])
        
    return ids


def getDb():
    # print(getFollowStock(1))
    print(getTelegramIds())

if __name__ == '__main__':
    getDb()