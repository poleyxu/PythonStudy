#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time:        2019/10/16 21:54
# @Author:      poley
# @Email:       poleyxu@gmail.com
# @File :       def_func2.py
# @Description: 
"""


def power(x):
    return x*x


print(power(5))
print(power(-5))


# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power2(4))
print(power2(2, 3))


def reg(name, gender):
    print("name：", name)
    print("gender:", gender)


print(reg("poley", "g"))


def reg2(name, gender, age=6, city='beijing'):
    print("name:", name)
    print("gender:", gender)
    print("age:", age)
    print("city:", city)


print(reg2("poley", "g1"))
print(reg2("jack", "g2", 7, ))
print(reg2("xu", "g3", city="hefei"))
