import datetime
import pymssql

conn = pymssql.connect(
    host='yourhost',  # 位置
    user='youracct',  # DB帳號
    password='yourpassword',  # DB密碼
    database='yourDBname'  # DB name
)

cursor = conn.cursor()
strCREATE_TABLE = "IF NOT EXISTS(select * from sysobjects where name=\'MSSQLArchive\')\
CREATE TABLE MSSQLArchive( \
SEQ INT IDENTITY PRIMARY KEY,\
NAME VARCHAR(100) NOT NULL,\
RNAME VARCHAR(100) NOT NULL,\
NBR_TYPE VARCHAR(100) NOT NULL, \
PATH VARCHAR(100) NOT NULL, \
SEASON VARCHAR(10), \
EPISODE VARCHAR(10) NOT NULL,\
EPISODE_LIST VARCHAR(300),\
EXT VARCHAR(50) NOT NULL,\
CC VARCHAR(1) NOT NULL,\
TAG VARCHAR(500),\
MNT_DT datetime)"

cursor.execute(strCREATE_TABLE)
try:
    conn.commit()
    print('CREATE TABLE SUCCESS')
except:
    print('CREATE TABLE ERROR')


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


try:
    strttt = "INSERT INTO MSSQLArchive ( NAME, RNAME, NBR_TYPE,PATH,SEASON,EPISODE,EPISODE_LIST,EXT,CC,TAG,MNT_DT) VALUES ('" + \
        dict['NAME']+"','" + dict['RNAME']+"','"+dict['NBR_TYPE'] + "','" + dict['PATH']+"','" + dict['SEASON']+"','"+dict['EPISODE'] + \
        "','" + dict['EPISODE_LIST'] + "','"+dict['EXT']+"','" + \
        dict['CC']+"','" + dict['TAG']+"','"+str(dict['MNT_DT'])+"')"
    cursor.execute(strttt)
    conn.commit()
    print('insert data to MSSQL success ...')
except:
    print('寫入SQL資料錯誤')


cursor.close()
conn.close()
