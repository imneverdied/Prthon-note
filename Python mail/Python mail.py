import tkinter as tk
import smtplib
import email.message
import time


# 建立訊息物件


def mail():
    msg = email.message.EmailMessage()
    mail_from_address = format(mail_from_acct_Entry.get())
    mail_from_password = format(mail_from_password_Entry.get())
    mail_to_address = format(Mail_To_Entry.get())

    msg["From"] = mail_from_address
    msg["To"] = mail_to_address
    msg["Subject"] = time.strftime(
        "%Y年%m月%d日", time.localtime()) + format(Mail_Subject_Entry.get())

    send_msg = format(Mail_message.get("1.0", 'end-1c'))
    send_msg = send_msg.replace('\n', '<br>')
    # 寄送郵件主要內容
    # msg.set_content("測試郵件純文字內容") #純文字信件內容
    msg.add_alternative(send_msg,
                        subtype="html")  # HTML信件內容

    # 連線到SMTP Sevver
    # 可以從網路上找到主機名稱和連線埠
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # 建立gmail連驗
    server.login(mail_from_address, mail_from_password)

    try:
        server.send_message(msg)
        tk.Label.configure(label, text='已寄出email: ' +
                           format(Mail_Subject_Entry.get()))
        label.grid(column=1, row=2, ipadx=5, pady=5, sticky=tk.W+tk.N)
    except:
        tk.Label.configure(label, text='error: mail to:[' + format(
            Mail_To_Entry.get()) + '] Subject:[' + format(Mail_Subject_Entry.get()) + ']')
        label.grid(column=1, row=2, ipadx=5,
                   pady=5, sticky=tk.W+tk.N)
    server.close()  # 發送完成後關閉連線


window = tk.Tk()
window.title('Python mail')
window.geometry("300x300+250+150")

# 標示文字
label = tk.Label(window, text='Python mail')
label.grid(column=1, row=3, ipadx=5, pady=5, sticky=tk.W+tk.N)
# label.pack()

Menu_p = tk.Menu(window)
window.configure(menu=Menu_p)

# 視窗主畫面
Mail_To = tk.Label(window,
                   text="Mail to:")
Mail_To.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)

Mail_Subject = tk.Label(window,
                        text="Subject:")
Mail_Subject.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.S)

Mail_To_Entry = tk.Entry(window, width=30)
Mail_Subject_Entry = tk.Entry(window, width=30)

Mail_To_Entry.grid(column=1, row=0, padx=10, pady=5, sticky=tk.N)
Mail_Subject_Entry.grid(column=1, row=1, padx=10,
                        pady=5, sticky=tk.S)


Mail_body = tk.Label(window,
                     text="Body:")
Mail_body.grid(column=0, row=2, ipadx=5, pady=5, sticky=tk.NW)

Mail_message = tk.Text(window, width=30, height=10)
Mail_message.grid(column=1, row=2, padx=10,
                  pady=5, sticky=tk.W)


SendButton = tk.Button(window, text='Send', command=mail)
SendButton.grid(column=0, row=3, pady=10, sticky=tk.W)


# 登入窗

mail_from = tk.Toplevel(window)
mail_from.title('Acct login')
window.configure(menu=mail_from)

mail_from_acct_E = tk.Label(mail_from,
                            text="acct:")
mail_from_acct_E.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)

mail_from_password_E = tk.Label(mail_from,
                                text="password:")
mail_from_password_E.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.S)

mail_from_acct_Entry = tk.Entry(mail_from, width=30)
mail_from_password_Entry = tk.Entry(mail_from, width=30)

mail_from_acct_Entry.grid(column=1, row=0, padx=10, pady=5, sticky=tk.N)
mail_from_password_Entry.grid(column=1, row=1, padx=10,
                              pady=5, sticky=tk.S)

window.mainloop()
