import tkinter as tk


def onOK():
    # 更新Label
    print("--> {}".format(entry.get()))
    tk.Label.configure(label, text=format(entry.get()))
    label.pack()


window = tk.Tk()
window.title('Change Label')
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
