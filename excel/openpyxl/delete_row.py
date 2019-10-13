import openpyxl
def deleterows(sheet,row_num):
  for row in range(row_num, sheet.max_row):
    for column in range(sheet.max_column):
      sheet[row][column].value = sheet[row + 1][column].value
  for cell in list(sheet.rows)[sheet.max_row - 1]:
    cell.value = None

if __name__=="__main__":
  wb = openpyxl.load_workbook('testbook1.xlsx')
  sheet =wb.active
  deleterows(sheet,1)
  wb.save('testbook2.xlsx')