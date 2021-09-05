import sqlite3  # import sqlite3 DB
from sqlite3.dbapi2 import Date
import threading
import os
import datetime

db_locker = threading.Semaphore(1)
db_path = os.path.join("", 'SqliteArchive.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS SqliteArchive ('
               'SEQ INT IDENTITY PRIMARY KEY,'
               'NAME VARCHAR(100) NOT NULL,'
               'RNAME VARCHAR(100) NOT NULL,'
               'NBR_TYPE VARCHAR(100) NOT NULL, '
               'PATH VARCHAR(100) NOT NULL, '
               'SEASON VARCHAR(10), '
               'EPISODE VARCHAR(10) NOT NULL,'
               'EPISODE_LIST VARCHAR(300),'
               'EXT VARCHAR(50) NOT NULL,'
               'CC VARCHAR(1) NOT NULL,'
               'TAG VARCHAR(500),'
               "[MNT_DT] TimeStamp NOT NULL DEFAULT (datetime('now','localtime')))")
print('CREATE TABLE IF NOT EXISTS SqliteArchive...')
conn.commit()
conn.close()


db_locker.acquire()
# insert new data
dict = {
    'NAME': 'test name',
    'RNAME': 'test name',
    'NBR_TYPE': '1',
    'PATH': 'D://one//',
    'SEASON':  '1',
    'EPISODE': '9',
    'EPISODE_LIST':  '1,2,3,4,5,5.5,6,7,8',
    'EXT':  '.mp4',
    'CC':  '1',
    'TAG': 'test,test name',
    'MNT_DT': datetime.date.today()}

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO SqliteArchive ( SEQ, NAME, RNAME, NBR_TYPE,PATH,SEASON,EPISODE,EPISODE_LIST,EXT,CC,TAG,MNT_DT) VALUES ( (SELECT IFNULL(MAX (SEQ), 0) FROM SqliteArchive)+1 ,:NAME, :RNAME, :NBR_TYPE, :PATH, :SEASON, :EPISODE, :EPISODE_LIST, :EXT, :CC, :TAG, :MNT_DT)",
                   dict)  # 寫入SQLLite
    print('insert data to SQLite  ...')
except sqlite3.IntegrityError as e:
    print('寫入SQLite資料重複:' + 'SEQ' + ' 資料已存在 ' + str(e))

cursor.close()
conn.commit()
conn.close()
db_locker.release()
