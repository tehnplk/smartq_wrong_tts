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
    db = con_db()
    cur = db.cursor()
    for mydict in data:
        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
        columns = columns + ",`d_update`"

        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
        values = values + ",now()"

        sql = "INSERT IGNORE INTO %s ( %s ) VALUES ( %s );" % ('smartq_fname', columns, values)
        cur.execute(sql)
        print(sql)

    db.commit()
    db.close()
    print('FNAME OK.....')


def sync_lname():
    print(">>>>LNAME Start<<<<")
    api = f"{API}/lname"
    resp = requests.get(api)
    data = resp.json()
    db = con_db()
    cur = db.cursor()
    for mydict in data:
        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
        columns = columns + ",`d_update`"

        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
        values = values + ",now()"

        sql = "INSERT IGNORE INTO %s ( %s ) VALUES ( %s );" % ('smartq_lname', columns, values)
        cur.execute(sql)
        print(sql)

    db.commit()
    db.close()
    print('LNAME OK...')


if __name__ == '__main__':
    API = "http://www.smartqplk.com:5000"
    sync_fname()
    print('.......')
    sync_lname()
