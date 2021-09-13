import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()

prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
#options.binary_location = '/usr/bin/chromium-browser'
options.add_argument("--headless")  # 不開啟實體瀏覽器背景執行
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')


base_url = "https://mis.twse.com.tw/stock/etf_nav.jsp?ex=tse"

browser = webdriver.Chrome(options=options,
                           executable_path='chromedriver')
browser.get(base_url)
print('網頁讀取中..')
time.sleep(3)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
div = soup.select_one("div#content")
table = pd.read_html(str(div))
frames = [table[0], table[1], table[3], table[5]]
result = pd.concat(frames, ignore_index=True)


# print(frames[0])

print('資料處理中..')
with open("ETF.txt", "w", encoding="UTF-8") as f:  # 產出輸入之txt
    f.write(str(frames[0]))


df = result[['ETF代號/名稱', '成交價',
             '投信或總代理人預估淨值(註2)', '預估折溢價幅度(註3)']]

df.columns = ['名稱', '市價', '估淨值', '估折溢價幅度']

# 溢價大於0.5%
premium = df[df["估折溢價幅度"] > "0.5%"].sort_values(
    by="估折溢價幅度", ascending=False).head(10)

# 折價小於-3%
discount = df[df["估折溢價幅度"] <
              "-3%"].sort_values(by="估折溢價幅度", ascending=False).head(10)


with open("premium_ETF.txt", "w", encoding="UTF-8") as f:  # 產出輸入之txt
    f.write(str(premium))


with open("discount_ETF.txt", "w", encoding="UTF-8") as f:  # 產出輸入之txt
    f.write(str(discount))


browser.quit()

print('完成...5秒後自動關閉')
time.sleep(5)
