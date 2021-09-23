#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk


def combobox_selected(event):
    mode_label.set(ddlText.get())


root = tk.Tk()
root.title('my window')
root.geometry('300x200')

ddlText = tk.StringVar()
ddlTYPE = ttk.Combobox(root, textvariable=ddlText, state='readonly')
ddlTYPE['values'] = ['尋找取代', '重新命名']
ddlTYPE.pack(pady=10)
ddlTYPE.current(1)

ddlTYPE.bind('<<ComboboxSelected>>', combobox_selected)

mode_label = tk.StringVar()
mylabel = tk.Label(root, textvariable=mode_label, height=5, font=('Arial', 16))
mylabel.pack()

root.mainloop()
