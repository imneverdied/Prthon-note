import os

try:
    os.system("netsh wlan connect name=SMD-4G-02")
    print('SMD-4G-02連接成功')
except:
    print('SMD-4G-02連接失敗')

os.system("pause")
#
