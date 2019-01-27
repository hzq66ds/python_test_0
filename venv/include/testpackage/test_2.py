list = [1, 2, 3, 4, 5, 6]
for x in list:
    print(x, end=";")
print(list[0], list[1])
list[1] = 10
print(list[1])
print(list[4:6])
list = list + list
print(3 in list)



def sum(num1, num2):
    return num1+num2

lambdasum = lambda num1,num2:num1+num2


print(sum(1,2))
print(lambdasum(1,3))

vec = [2, 4, 6]
veccoppy = [3*x for x in vec]
print(veccoppy)

veccoppy0 = [[x, x**2] for x in vec]
print(veccoppy0)

veccoppy1 = [3*x for x in vec if x > 3]
print(veccoppy1)

print(11 in range(10))
print(11 > 10)
print(11 < 10)

# 打开一个文件
f = open("/Users/hanzhiqiang/Desktop/foo.txt", "w+")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
value = ('www.runoob.com', 14)
s = str(value)
f.write(s)

# 关闭打开的文件
f.close()

f1 = open("/Users/hanzhiqiang/Desktop/foo.txt", "r+")

#print(f1.read())

#str = f1.readline()
#print(str)
for x in f1.readlines():
    print(x)
# 关闭打开的文件
f1.close()

f2 = open("/Users/hanzhiqiang/Desktop/foo.txt", "r+")

for x in f2.read():
    print(f2.tell())
    print(x, end = "")
# 关闭打开的文件
f2.close()


f3 = open("/Users/hanzhiqiang/Desktop/foo.txt", "r+")

for x in f3:
    print(x, end = "")
f3.seek(1,0)
print(f3.tell())
# 关闭打开的文件
f3.close()