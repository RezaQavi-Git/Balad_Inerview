import pandas as pd
import sqlite3
from sqlite3 import Error
import csv
import os
import re

def createConnection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def createTable(conn, dbName):
    conn.execute('''CREATE TABLE IF NOT EXISTS {}
          (key             TEXT    NOT NULL,
          value           TEXT    NOT NULL);'''.format(dbName))

def inertInToTable(conn, dbName, key, value):
    conn.execute('INSERT INTO {} VALUES (?, ?)'.format(dbName), (key, str(value) ) )
    conn.commit()

def selectWithKey(conn, dbName, key):
    cur = conn.cursor()
    cur.execute('SELECT * FROM {} WHERE key=:k'.format(dbName), {"k": key} )
    rows = cur.fetchall()
    return rows[0][1]

def deleteWithKey(conn, dbName, key):
    conn.execute('DELETE FROM {} WHERE key=:k'.format(dbName), {"k": key} )
    conn.commit()
    return

def findTables(conn):
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cur.fetchall()
    tableLists = []
    for row in rows:
        tableLists.append(row[0])

    return tableLists

def findMatchkeys(conn, dbName, key):
    cur = conn.cursor()
    cur.execute('SELECT * FROM {}'.format(dbName))
    rows = cur.fetchall()
    matchs = []
    for row in rows:
        x = re.search(key, row[0])
        if x:
            matchs.append(row[0])

    return matchs
def dumpDB(conn, dbName, path):
    cur = conn.cursor()
    cur.execute("select * from {}".format(dbName))
    filePath = path[:path.rfind('/')]
    # fileName = path[path.rfind('/'):]
    os.makedirs(filePath) 
    with open("{}.csv".format(path), "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)
    csv_file.close()
    return 

def loadDB(conn, path, dbName):
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS {} (key, value);".format(dbName)) # use your column names here
    with open('{}.csv'.format(path),'r') as file:
        dr = csv.DictReader(file)
        to_db = [(i['key'], i['value']) for i in dr]
    cur.executemany("INSERT INTO {} (key, value) VALUES (?, ?);".format(dbName), to_db)
    conn.commit()
    file.close()

    return