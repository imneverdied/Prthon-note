import openpyxl
# pip install openpyxl
from openpyxl import Workbook


excel = Workbook()
sheet = excel.active  # 建立一個工作中表


def createTable(columnA, columnB, columnC, columnD):
    # 欄位名稱定義
    sheet['A1'] = columnA
    sheet['B1'] = columnB
    sheet['C1'] = columnC
    sheet['D1'] = columnD


def insert2Table(dataA, dataB, dataC, dataD):
    資料A = dataA
    資料B = dataB
    資料C = dataC
    資料D = dataD
    sheet.append([資料A, 資料B, 資料C, 資料D])


def OutExcel():
    try:
        excel.save('測試.xlsx')
        print('產出sample.xlsx')
    except:
        print('excel產出錯誤')


createTable('飛機', '車子', '船', '大象')
insert2Table(111, 222, 333, 444)
OutExcel()
