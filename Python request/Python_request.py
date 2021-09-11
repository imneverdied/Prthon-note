import requests


# #  GET web
# r = requests.get('https://www.google.com.tw/')
# print(r.status_code)

# if r.status_code == requests.codes.ok:
#     print("OK")

#     # #HTML
#     # print(r.text)


my_data = '<AAA>111<AAA> \n<BBB>222<BBB>\n<CCC>333<CCC>\n'

# 將資料加入 POST 請求中
r = requests.post('http://localhost:8081/', data=my_data)

if r.status_code == requests.codes.ok:
    print(r.status_code, 'OK')
    # 輸出網頁 HTML 原始碼
    print(r.text)
    
input("=========================")
