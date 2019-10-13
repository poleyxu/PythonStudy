#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
说明：把精密万用表的excel拷贝出来，只保留行号，电流值，秒数这3列，其他列都删除
A:行号，B：电流值，C:时间
'''

from openpyxl import load_workbook


wb = load_workbook('D:\defbuffer2.xlsx')
ws1 = wb.active


for i in range(1 , ws1.max_row):
    # 先计算电流值的持续时间：第2行的时间减去第一行的时间，是这个电流的持续时间
    d = ws1.cell(row=i+1, column = 3 ).value-ws1.cell(row=i, column = 3).value
    if d > 0:
        ws1.cell(row=i, column = 4).value = d
    else:
        # 解决跨秒问题
        ws1.cell(row=i, column=4).value = d+1

for i in range(1, ws1.max_row-1):
    # 把电流值与持续时间相乘，在转换为mAh存放到第5列
    ws1.cell(row=i, column=5).value=ws1.cell(row=i, column=2).value * ws1.cell(row=i + 1, column=4).value*1000/3600


wb.save('D:\defbuffer2.xlsx')