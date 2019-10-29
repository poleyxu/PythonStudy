#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = abs(100)
y = abs(-20)
z = abs(12.34)
print(x, y, z)
print('max(1, 2, 3, -5) =', max(1, 2, 3, -5))
print('min(1, 2, 3, -1) =', min(1, 2, 3, -1))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))

n1 = 255
n2 = 1000

# 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
print(hex(n1))
print(hex(n2))

print(int('123'))
print(int(12.34))
print(str(1.23))
print(str(123))
print(bool(1))
print(bool(0))
print(float('12.34'))