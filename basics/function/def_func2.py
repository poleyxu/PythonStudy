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
# 只有与默认参数不符的学生才需要提供额外的信息：
print(reg2("jack", "g2", 7, ))
# 只有与默认参数不符的学生才需要提供额外的信息：
print(reg2("xu", "g3", city="hefei"))


def add_end(l1=[]):
    l1.append('END')
    return l1


#  调用一次，增加一个END，Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
#  每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#  定义默认参数要牢记一点：默认参数必须指向不变对象！
print(add_end())
print(add_end())
print(add_end())
print(add_end())


# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end2(l2=None):
    if l2 is None:
        l2 = []
    l2.append('END')
    return l2


print(add_end2())
print(add_end2())
print(add_end2())
