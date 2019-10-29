#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 打印数字 0 - 9
for x in range(10):
    print(x)

# 计算1-10的整数之和，可以用一个sum变量做累加：
sum1 = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum1 = sum1 + x
print(sum1)

# 计算1-100的整数之和,range(101)就可以生成0-100的整数序列
sum2 = 0
for y in range(101):
    sum2 = sum2 + y
print(sum2)

# 循环是while循环,计算100以内所有奇数之和
sum3 = 0
n = 99
while n > 0:
    sum3 = sum3 + n
    n = n - 2
print(sum3)

# 利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
i = 0
for i in range(len(L)):
    print("Hello,", L[i]+'!')

# 如果要提前结束循环，可以用break语句：
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break   # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# 如果我们想只打印奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue    # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
