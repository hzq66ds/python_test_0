#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
import calendar
import keyword

#dir(math)
#dir(keyword)

#print(keyword.kwlist)

print("abcdefghijk"[2: 5] * 3)

num_0 = 0
if num_0 == 0:
    print(True)
    num_0 += 1
else:
    print(False)
    if num_0 == 0:
        print(True)
    else:
        print(False)


nums = {1, 2, 3, 4, 5}
for n in nums:
    print(n)
while len(nums) > 0:
    print(nums.pop())

print("pop之后的长度", len(nums))


for l in 'Python':     # 第一个实例
    print('当前字母 :', l)

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index], range(len(fruits)))

print(len(fruits))


hello_world = 'hello world'
str_0 = 'len of (%s) is %d' % (hello_world, len(hello_world))
print(str_0)

print(hello_world.capitalize())
print(hello_world.center(13))

cal = calendar.month(2018, 9)
print("以下输出2018年9月份的日历:")
print(cal)

print(calendar.month(tuple(calendar.nextmonth(2018, 9))[0], tuple(calendar.nextmonth(2018, 9))[1]))


def print_me(str_name):
    print(str_name)
    return


print_me("自定义方法")

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
print()
list0 = [1, 2, 3, 4, 5, 6]
print([i*2 for i in list0])
print([[i*2, i*3] for i in list0])
# range()
print(range(1, 6, 2))

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')