#! /usr/bin/python3

from flask import Flask, json, jsonify

import mysql.connector

app = Flask(__name__)


def con_db():
    db = mysql.connector.connect(
        host='localhost',
        user='sa',
        passwd='qazwsxedcr112233',
        db='smartq_tts',
        port=3306
    )
    return db


@app.route('/')
def hello():
    return "SmartQ wrong tts is running."


@app.route('/fname')
def fname():
    db = con_db()
    cur = db.cursor()
    sql = """select id , tts from smartq_fname"""
    cur.execute(sql)
    row_headers = [x[0] for x in cur.description]  # this will extract row headers
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


@app.route('/lname')
def lname():
    db = con_db()
    cur = db.cursor()
    sql = """select id , tts from smartq_lname"""
    cur.execute(sql)
    row_headers = [x[0] for x in cur.description]  # this will extract row headers
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
