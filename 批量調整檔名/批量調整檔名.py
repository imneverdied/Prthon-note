import os
import threading
import tkinter
from tkinter import Label, ttk
from tkinter.constants import E, N, NE, W
from typing import Reversible
import tkinter.messagebox
import time


def ReNameT():
    # 'C:\\Users\\fydra\\Desktop\\python\\'+folderName  # 路徑名
    path = format(路徑INPUT.get())

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
        Pnewname = files[n].replace(
            format(NewName.get()), format(ReplaceName.get()))   # 印出新名

        print(files[n]+' > ' + Pnewname)  # 印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
        Table.insert("", 0, text="", values=(files[n], Pnewname))  # 插入資料，
        n = n-1


def ReName():

    path = format(路徑INPUT.get())

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

    path = format(路徑INPUT.get())

    n = len(files)-1  # 反向插入

    x = Table.get_children()  # 清空Table
    for item in x:
        Table.delete(item)

    # main 開始

    for i in files:
        oldname = path + '\\' + files[n]
        newname = path + '\\' + \
            files[n].replace(format(NewName.get()),
                             format(ReplaceName.get()))   # 印出新名
        Pnewname = files[n].replace(
            format(NewName.get()), format(ReplaceName.get()))   # 印出新名

        os.rename(oldname, newname)

        # insert new data to ReNameLog
        print(files[n]+' > ' + Pnewname)  # 印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
        Table.insert("", 0, text="", values=(files[n], Pnewname))  # 插入資料，
        n = n-1
        ReNameT()  # 轉換成功後刷新LIST


def PopMessage(msg):
    tkinter.messagebox.showinfo(title='錯誤!',  # 視窗標題
                                message=msg)   # 訊息內容


def combobox_selected(event):
    window.title('Renamer '+ddlText.get() + ' 模式')


def 重新命名試算():
    path = format(路徑INPUT.get())

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
        dot = files[n].rindex('.')
        EEXT = files[n][dot:]
        Pnewname = format(NewName.get()) + '[' + str(n+1) + ']' + EEXT  # 印出新名

        print(files[n]+' > ' + Pnewname)  # 印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
        Table.insert("", 0, text="", values=(files[n], Pnewname))  # 插入資料，
        n = n-1


def 重新命名轉換():
    path = format(路徑INPUT.get())

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
        dot = files[n].rindex('.')
        EEXT = files[n][dot:]
        oldname = path + '\\' + files[n]
        newname = path + '\\' + \
            format(NewName.get()) + '[' + str(n+1) + ']' + EEXT  # 印出新名

        Pnewname = format(NewName.get()) + '[' + str(n+1) + ']' + EEXT  # 印出新名
        os.rename(oldname, newname)

        # insert new data to ReNameLog
        print(files[n]+' > ' + Pnewname)  # 印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
        Table.insert("", 0, text="", values=(files[n], Pnewname))  # 插入資料，
        n = n-1
        重新命名試算()  # 轉換成功後刷新LIST


def 試算model():
    if(format(ddlText.get()) == '尋找取代'):
        ReNameT()
    else:
        重新命名試算()


def 轉換model():
    if(format(ddlText.get()) == '尋找取代'):
        ReName()
    else:
        重新命名轉換()


window = tkinter.Tk()
window.title('Renamer')
window.geometry('+800+350')

路徑文字 = tkinter.Label(window, text='路徑')
# 下拉選單
ddlText = tkinter.StringVar()
模式選擇 = ttk.Combobox(window, textvariable=ddlText, state='readonly', width=10)
模式選擇['values'] = ['重新命名', '尋找取代']
模式選擇.current(1)
模式選擇.bind('<<ComboboxSelected>>', combobox_selected)
# 下拉選單
# 輸入欄位
路徑INPUT = tkinter.Entry(window,   # 輸入欄位所在視窗
                        width=30)  # 輸入欄位的寬度
新名文字 = tkinter.Label(window, text='尋找')
NewName = tkinter.Entry(window,   # 輸入欄位所在視窗
                        width=25)  # 輸入欄位的寬度
取代文字 = tkinter.Label(window, text='取代')

ReplaceName = tkinter.Entry(window,   # 輸入欄位所在視窗
                            width=25)  # 輸入欄位的寬度
# 輸入欄位

# table定義
columns = ("目前名稱", "尋找")
Table = ttk.Treeview(window, height=10, show="headings", columns=columns)  # 表格
Table.column("目前名稱", width=150)  # 表示列,不顯示
Table.column("尋找", width=150)
Table.heading("目前名稱", text="目前名稱")  # 顯示錶頭
Table.heading("尋找", text="尋找")
# table定義


# 按鈕
試算按鈕 = tkinter.Button(window, text="試算", command=試算model)
轉換按鈕 = tkinter.Button(window, text="轉換", command=轉換model)
# 按鈕

# grid版面調整區域
路徑文字.grid(row=0, column=0, sticky=W, padx=0, pady=2)  # 路徑文字
新名文字.grid(row=1, column=0, sticky=W, padx=0, pady=2)  # 新名文字
取代文字.grid(row=2, column=0, sticky=W, padx=0, pady=2)  # 新名文字
路徑INPUT.grid(row=0, column=0, sticky=W, padx=30,  pady=2)  # 路徑INPUTBOX
NewName.grid(row=1, column=0, sticky=W, padx=30, pady=2)  # 新名INPUTBOX
ReplaceName.grid(row=2, column=0, sticky=W, padx=30, pady=2)  # 新名INPUTBOX
試算按鈕.grid(row=1, column=0, sticky=E, padx=45, pady=2)  # 試算按鈕
轉換按鈕.grid(row=1, column=0, sticky=E, padx=5, pady=2)  # 轉換按鈕
模式選擇.grid(row=2, column=0, sticky=E, padx=0, pady=2)
Table.grid(row=3, column=0, sticky=W, pady=2)  # 資料表
# grid版面調整區域


window.mainloop()
