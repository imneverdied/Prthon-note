import os

try:
    os.system("ipconfig")
except:
    print('CMD指令執行失敗')

os.system("pause")
