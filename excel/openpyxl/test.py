#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from openpyxl import load_workbook

# 读取excel文档，需要先在D盘创建一个test.xlsx文档
wb = load_workbook('D:\\temp\\test.xlsx')

# 返回一个列表， 存储excel表中所有的sheet工作表;
print(wb.sheetnames)
# 默认激活第1个工作表
ws1 = wb.active
print(ws1)
# 将第一行第一列的值设置为'abc'
ws1.cell(row=1, column=1).value = 'abc'
# 获取第2个工作表
ws2 = wb['test2']
# 将第一行第一列的值设置为'ABC'
ws2.cell(row=1, column=1).value = 'ABC'
print(ws2)

print(ws2['A1'].value)


cell = ws2['B3']
# 打印B5的行号和列号
print(cell.row, cell.column)

print(ws2.cell(row=3, column=2))
print(ws2.cell(row=3, column=2).value)
print(ws2.cell(row=3, column=2, value='www'))

# sheet的属性

print(ws2.max_column)
print(ws2.max_row)
print(ws2.title)
ws2.title = 'example'
print(ws2.title)
ws2.title = 'test2'
print(ws2.title)

# 打印存在的每一行和每一列的值，cell.value 单元格的值
for row in ws2.rows:
    for cell in row:
        print(cell.value, end='\t')
    print('\n')
# 方式一：数据可以直接分配到单元格中(可以输入公式)
ws2['B1'] = 42
# 方式二：可以附加行，从第一列开始附加(从最下方空白处，最左开始)(可以输入多行)
# ws2.append([1, 2, 3])

wb.save('D:\\temp\\test.xlsx')
