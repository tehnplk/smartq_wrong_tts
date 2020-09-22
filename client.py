import requests
import mysql.connector


def con_db():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='112233',
        db='his',
        port=3306
    )
    return db


def sync_fname():
    print(">>>>FNAME Start<<<<")
    api = f"{API}/fname"
    resp = requests.get(api)
    data = resp.json()
    for mydict in data:
        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
        sql = "INSERT IGNORE INTO %s ( %s ) VALUES ( %s );" % ('smartq_fname', columns, values)
        db = con_db()
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
        print(sql)
    print('FNAME OK.....')


def sync_lname():
    print(">>>>LNAME Start<<<<")
    api = f"{API}/lname"
    resp = requests.get(api)
    data = resp.json()
    for mydict in data:
        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
        sql = "INSERT IGNORE INTO %s ( %s ) VALUES ( %s );" % ('smartq_lname', columns, values)
        db = con_db()
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
        print(sql)
    print('LNAME OK...')


if __name__ == '__main__':
    API = "http://www.smartqplk.com:5000"
    sync_fname()
    print('.......')
    sync_lname()