import tkinter as tk

# 讀取輸入值輸出txt


def onOK():
    # 更新Label
    print("--> {}".format(entry.get()))
    try:
        with open(format(entry.get()) + ".txt", "w", encoding="UTF-8") as f:  # 產出輸入之txt
            f.write(format(entry.get()))
        tk.Label.configure(label, text='已產出 '+format(entry.get())+'.txt')
    except:
        tk.Label.configure(label, text='產出 '+format(entry.get())+'.txt 錯誤!')

    label.pack()


window = tk.Tk()
window.title('Change Label and out put txt')
window.geometry("300x100+250+150")

# 標示文字
label = tk.Label(window, text='Type and click')
label.pack()

# 輸入欄位
entry = tk.Entry(window,     # 輸入欄位所在視窗
                 width=20)  # 輸入欄位的寬度
entry.pack()

# 按鈕
button = tk.Button(window, text="OK", command=onOK)
button.pack()

window.mainloop()
