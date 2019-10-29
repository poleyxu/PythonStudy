#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
age = int(input('Input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

year = int(input("输入出生年份："))
if year > 2000:
    print("你是00后啊")
else:
    print("你是00前啊")

height = 1.75
weight = 80.5
BMI = height/weight
if BMI < 18.5:
    print("过轻")
elif 18.5 <= BMI <= 25:
    print("正常")
elif 25 < BMI <= 28:
    print("过重")
elif 28 < BMI <= 32:
    print("肥胖")
elif BMI > 32:
    print("过于肥胖")
