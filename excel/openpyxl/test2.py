#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from openpyxl import load_workbook

# 读取excel文档，需要先在D盘创建一个test.xlsx文档
wb = load_workbook('D:\\test.xlsx')
# 方式一：插入到最后(default)
# ws1 = wb.create_sheet("Mysheet")
# 方式二：插入到最开始的位置
# ws2 = wb.create_sheet("Mysheet2", 0)

# 方式一
ws1 = wb['Mysheet']
wb.remove(ws1)
# 方式二
# del wb["Mysheet2"]
wb.save('D:\\test.xlsx')
