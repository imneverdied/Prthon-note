import os
import threading
import tkinter
from tkinter import Label, ttk
from tkinter.constants import E, N, NE, W
from typing import Reversible
import tkinter.messagebox
import time
import sqlite3  # import sqlite3 DB
from sqlite3.dbapi2 import Date

db_path = os.path.join("", 'ReNameLog.db')


def CreateDatabase_CreateTable():

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS ReNameLog ('
                   'BEFORE_NAME VARCHAR(100),'
                   'NEW_NAME VARCHAR(100))')
    print('CREATE TABLE IF NOT EXISTS ReNameLog...')
    conn.commit()
    conn.close()


def InsertData(dict):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO ReNameLog ( BEFORE_NAME, NEW_NAME) VALUES ( :BEFORE_NAME, :NEW_NAME)",
                       dict)  # 寫入SQLLite
        print('insert data to SQLite ReNameLog  ...')
    except sqlite3.IntegrityError as e:
        print('寫入SQLite資料重複:' + str(e))

    cursor.close()
    conn.commit()
    conn.close()


def ReNameT():
    # 'C:\\Users\\fydra\\Desktop\\python\\'+folderName  # 路徑名
    path = format(Input_path.get())

    if path == '':
        print('錯誤:路徑為空')
        with open("Python_Window_Rename_log.txt", "a", encoding="UTF-8") as f:  # 寫入log
            f.write(time.strftime("%Y/%m/%d %H:%M:%S",
                    time.localtime()) + ' 錯誤:路徑為空\n')
        PopMessage('錯誤:路徑為空')

        return

    try:
        files = os.listdir(path)
    except Exception as e:
        print(e)
        print('錯誤:取得路徑資料失敗' + e)
        with open("Python_Window_Rename_log.txt", "a", encoding="UTF-8") as f:  # 寫入log
            f.write(time.strftime("%Y/%m/%d %H:%M:%S",
                    time.localtime()) + ' 錯誤:取得路徑資料失敗\n')
        PopMessage('錯誤:取得路徑資料失敗')

        return

    n = len(files)-1  # 反向插入

    x = Table.get_children()  # 清空Table
    for item in x:
        Table.delete(item)

    for i in files:

        EXT_H = files[n].rindex('.')  # 取出附檔名處理 選擇最後出的'.'
        EXT_T = len(files[n])
        EXT = files[n][EXT_H-EXT_T:]
        EP_H = files[n].index('[')
        EP_T = files[n].index(']')
        EP = files[n][EP_H + 1:EP_T]
        Pnewname = format(NewName.get()) + '['+str(EP)+']' + EXT  # 印出新名

        print(files[n]+' > ' + Pnewname)  # 印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
        Table.insert("", 0, text="", values=(files[n], Pnewname))  # 插入資料，
        n = n-1


def ReName():
    # 'C:\\Users\\fydra\\Desktop\\python\\'+folderName  # 路徑名
    path = format(Input_path.get())

    if path == '':
        print('錯誤:路徑為空')
        with open("Python_Window_Rename_log.txt", "a", encoding="UTF-8") as f:  # 寫入log
            f.write(time.strftime("%Y/%m/%d %H:%M:%S",
                    time.localtime()) + ' 錯誤:路徑為空\n')
        PopMessage('錯誤:路徑為空')

        return

    try:
        files = os.listdir(path)
    except Exception as e:
        print('錯誤:取得路徑資料失敗 ' + e)
        with open("Python_Window_Rename_log.txt", "a", encoding="UTF-8") as f:  # 寫入log
            f.write(time.strftime("%Y/%m/%d %H:%M:%S",
                    time.localtime()) + ' 錯誤:取得路徑資料失敗\n')
        PopMessage('錯誤:取得路徑資料失敗')

        return

    path = format(Input_path.get())

    n = len(files)-1  # 反向插入

    x = Table.get_children()  # 清空Table
    for item in x:
        Table.delete(item)

    # main 開始
    db_locker = threading.Semaphore(1)

    CreateDatabase_CreateTable()

    db_locker.acquire()

    for i in files:

        EXT_H = files[n].rindex('.')  # 取出附檔名處理 選擇最後出的'.'
        EXT_T = len(files[n])
        EXT = files[n][EXT_H-EXT_T:]
        EP_H = files[n].index('[')
        EP_T = files[n].index(']')
        EP = files[n][EP_H + 1:EP_T]
        oldname = path + '\\' + files[n]
        newname = path + '\\' + \
            format(NewName.get()) + '['+str(EP)+']' + EXT  # 印出新名
        Pnewname = format(NewName.get()) + '['+str(EP)+']' + EXT  # 印出新名

        os.rename(oldname, newname)

        # insert new data ReNameLog
        dict = {
            'BEFORE_NAME': files[n],
            'NEW_NAME': Pnewname}

        InsertData(dict)
        # insert new data to ReNameLog
        print(files[n]+' > ' + Pnewname)  # 印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
        Table.insert("", 0, text="", values=(files[n], Pnewname))  # 插入資料，
        n = n-1
        ReNameT()  # 轉換成功後刷新LIST

    db_locker.release()


def PopMessage(msg):
    tkinter.messagebox.showinfo(title='錯誤!',  # 視窗標題
                                message=msg)   # 訊息內容


window = tkinter.Tk()
window.title('批量更名 Renamer')
window.geometry('+800+350')
Label_path = tkinter.Label(window, text='路徑')
# 輸入欄位
Input_path = tkinter.Entry(window,   # 輸入欄位所在視窗
                           width=30)  # 輸入欄位的寬度

Label_NewName = tkinter.Label(window, text='新名稱')
NewName = tkinter.Entry(window,   # 輸入欄位所在視窗
                        width=25)  # 輸入欄位的寬度

columns = ("目前名稱", "新名稱")
# table定義
Table = ttk.Treeview(window, height=10, show="headings", columns=columns)  # 表格
Table.column("目前名稱", width=150)  # 表示列,不顯示
Table.column("新名稱", width=150)
Table.heading("目前名稱", text="目前名稱")  # 顯示錶頭
Table.heading("新名稱", text="新名稱")
# table定義


# 按鈕
試算按鈕 = tkinter.Button(window, text="試算", command=ReNameT)
轉換按鈕 = tkinter.Button(window, text="轉換", command=ReName)


# grid版面調整區域
Label_path.grid(row=0, column=0, sticky=W, padx=0, pady=2)  # 路徑文字
Label_NewName.grid(row=1, column=0, sticky=W, padx=0, pady=2)  # 新名文字
Input_path.grid(row=0, column=0, sticky=W, padx=30,  pady=2)  # 路徑INPUTBOX
NewName.grid(row=1, column=0, sticky=W, padx=40, pady=2)  # 新名INPUTBOX
試算按鈕.grid(row=1, column=0, sticky=E, padx=45, pady=2)  # 試算按鈕
轉換按鈕.grid(row=1, column=0, sticky=E, padx=5, pady=2)  # 轉換按鈕
Table.grid(row=2, column=0, sticky=W, pady=2)  # 資料表
# grid版面調整區域


window.mainloop()
