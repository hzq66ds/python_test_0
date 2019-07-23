#!/usr/bin/python
# -*- coding: UTF-8 -*-

print("abcdefghijk"[2: 5] + "  " + "abcdefghijk"[2: 5] * 3)
print("----------------------------------------------------")
print("hello\nworld")
print("----------------------------------------------------")
print(r"hello\nworld")
print("----------------------------------------------------")
print(len("aaaaaaaaA"))
print("----------------------------------------------------")
print("aa", "bb", "cc")
print("dd", "ee", "ff")
print("----------------------------------------------------")
print("aa", "bb", "cc", ";")
print("dd", "ee", "ff")
print("----------------------------------------------------")
a, b, c = 1, 2, "runoob"
print(a, b, c)
print(type(a), type(b), type(c))
print(isinstance(a, str), type(b), type(c))
print("----------------------------------------------------")
print(type(True))


tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(tinydict.keys())
print(tinydict.values())
print(tinydict.items())

for item in tinydict.items():
    print(item,item.__contains__("name"))

print('-----------------------------------------------------')
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素
print('-----------------------------------------------------')

if __name__ == "__main__":
    print('程序自身在运行')
else:
    print('我来自另一模块')
