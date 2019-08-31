#!/usr/bin/env python3

from openpyxl import Workbook
from openpyxl import load_workbook

#wb = Workbook()
wb = load_workbook(filename = 'data/test_spreadshhet.xlsx')
# grab the active worksheet
ws = wb.active

#ws = wb[0]
print(ws['A1'].value)
#print (ws.cell(range="A1:B2").value)


for row in ws.iter_rows():
    print ("New row")
    for col in row:
      print (col.value)

range=ws['A1':'C3'] 

#t=tuple(range)

#print(t)

#print (t[2][0].value)

# Data can be assigned directly to cells
# ws['A1'] = 42

# # Rows can also be appended
# ws.append([1, 2, 3, 4])

# # Python types will automatically be converted
# import datetime
# ws['A2'] = datetime.datetime.now()

# # Save the file
# wb.save("sample.xlsx")