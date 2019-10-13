#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
"""

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates ==', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
# 要删除list末尾的元素，用pop()方法：
classmates.pop()
print('classmates =', classmates)
# 往list中追加元素到末尾
classmates.append('poley')
print('classmates =', classmates)
# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'xu')
print('classmates =', classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(2)
print('classmates =', classmates)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[0]='Sarah'
print('classmates =', classmates)
# list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
print(L[0], L[1], L[2])
# list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2][0])
# 要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s[2][1])
print(p[1])
L = []
print(len(L))
