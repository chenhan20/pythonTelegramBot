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
    try:
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
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))



def getTelegramIds():
    try:
            
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        print("Opened database successfully")
        cur = conn.cursor()
        postgreSQL_select_Query = "select * from accounts where telegram_push_enabled = true "
        cur.execute(postgreSQL_select_Query)

        rows = cur.fetchall()
        ids = [];
        for row in rows:
            ids.append(row[4])
            
        return ids
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

# 台股有訂閱的ID
def getTwTelegramIds():
    try:
            
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        print("Opened database successfully")
        cur = conn.cursor()
        postgreSQL_select_Query = "select * from accounts where telegram_push_tw_enabled = true "
        cur.execute(postgreSQL_select_Query)

        rows = cur.fetchall()
        ids = [];
        for row in rows:
            ids.append(row[4])
            
        return ids
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

# 美股有訂閱的ID
def getUsTelegramIds():
    try:
            
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        print("Opened database successfully")
        cur = conn.cursor()
        postgreSQL_select_Query = "select * from accounts where telegram_push_us_enabled = true "
        cur.execute(postgreSQL_select_Query)

        rows = cur.fetchall()
        ids = [];
        for row in rows:
            ids.append(row[4])
            
        return ids
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

def getAccount(userId):
    try:
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cur = conn.cursor()
        postgreSQL_select_Query = 'select * from accounts where telegram_user_id = (%s) '
        cur.execute(postgreSQL_select_Query,(str(userId),))

        rows = cur.fetchall()
        account = []
        for row in rows:
            account.append(row)
        return account
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))


# def getUserDetail():
#     try:
        
#         conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
#         print("Opened database successfully")
#         cur = conn.cursor()
#         postgreSQL_select_Query = 'SELECT a.user_id, b.* from accounts a '
#         postgreSQL_select_Query += ' left join follow_stock b on a.user_id = b.user_id' 
#         postgreSQL_select_Query += ' where a.telegram_push_enabled = true '

#         cur.execute(postgreSQL_select_Query)
#         rows = cur.fetchall()
#         data = dict()
#         ids = [];
#         for row in rows:
#             print(row[0])
#             # row[0]
#             # ids.append(row[5])
            
    #     return ids
    # except Exception as error:
    #     print ("Oops! An exception has occured:", error)
    #     print ("Exception TYPE:", type(error))

def addUser(fromUser):
    try:
        account = getAccount(fromUser.id)
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cur = conn.cursor()
        if(len(account) == 0 ):
            print('new accounts')
            sql = 'INSERT INTO accounts(username, created_on, last_login, telegram_user_id, telegram_push_enabled, telegram_push_tw_enabled, telegram_push_us_enabled)' 
            sql += ' VALUES (%s, now(), now(), %s, true, true, true)'
            cur.execute(sql, (fromUser.first_name, fromUser.id))
        else:
            print('old accounts')
            sql = 'UPDATE accounts SET telegram_push_enabled = True, telegram_push_tw_enabled = True, telegram_push_us_enabled = True, last_login = now() WHERE telegram_user_id = (%s)' 
            cur.execute(sql, (str(fromUser.id),))

        conn.commit()       

    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

def removeUser(fromUser):
    try:
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cur = conn.cursor()
        sql = 'UPDATE accounts SET telegram_push_enabled = False, telegram_push_tw_enabled = False, telegram_push_us_enabled = False, last_login = now() WHERE telegram_user_id = (%s)' 
        cur.execute(sql, (str(fromUser.id),))
        conn.commit()       

    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

def enabledTw(fromUser, enabled):
    try:
        account = getAccount(fromUser.id)
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cur = conn.cursor()
        if(len(account) == 0 ):
            print('new accounts')
            sql = 'INSERT INTO accounts(username, created_on, last_login, telegram_user_id, telegram_push_enabled, telegram_push_tw_enabled, telegram_push_us_enabled)' 
            sql += ' VALUES (%s, now(), now(), %s, true, true, true)'
            cur.execute(sql, (fromUser.first_name, fromUser.id))
        else:
            print('old accounts')
            sql = 'UPDATE accounts SET telegram_push_tw_enabled = %s, last_login = now() WHERE telegram_user_id = (%s)' 
            cur.execute(sql, (enabled, str(fromUser.id),))
        conn.commit()       

    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

def enabledUs(fromUser, enabled):
    try:
        account = getAccount(fromUser.id)
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cur = conn.cursor()
        if(len(account) == 0 ):
            print('new accounts')
            sql = 'INSERT INTO accounts(username, created_on, last_login, telegram_user_id, telegram_push_enabled, telegram_push_tw_enabled, telegram_push_us_enabled)' 
            sql += ' VALUES (%s, now(), now(), %s, true, true, true)'
            cur.execute(sql, (fromUser.first_name, fromUser.id))
        else:
            print('old accounts')
            sql = 'UPDATE accounts SET telegram_push_us_enabled = %s, last_login = now() WHERE telegram_user_id = (%s)' 
            cur.execute(sql, (enabled, str(fromUser.id),))
        conn.commit()       

    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))


def getLastSendDate(sendType):
    try:
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        print("Opened database successfully")
        cur = conn.cursor()
        postgreSQL_select_Query = "select * from system_parameter where name = %s"
        cur.execute(postgreSQL_select_Query, (sendType,))
        rows = cur.fetchall()
        value = ''
        for row in rows:
            value = row[2]
            
        return value
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))


def updateLastSendDate(lastSendDate,sendType):
    try:
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cur = conn.cursor()
        sql = 'UPDATE system_parameter SET value = %s, update_on = now() WHERE name = (%s)' 
        cur.execute(sql, (lastSendDate, str(sendType),))
        conn.commit()       
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

def getDb():
    # print(getFollowStock(1))
    # print(getTelegramIds())
    # print(getTwTelegramIds())
    # print(getAccount())
    print(getLastSendDate('LAST_FRED_SEND_DATE'))

if __name__ == '__main__':
    getDb()