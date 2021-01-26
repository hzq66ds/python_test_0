import time
import os


def printTime(func):
    def wrapper(*args, **kwargs):
        print(time.ctime())
        return func(*args, **kwargs)

    return wrapper


@printTime
def printHello(name, age=12):
    print("hello %s" % name)
    print(age)


def fun(num):
    if num > 1:
        raise myEx('Invalid level')


class myEx(BaseException):
    def __init__(self, args):
        self.args = args


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printMsg(self):
        print("name:", self.name, "  age:", self.age)


if __name__ == "__main__":
    printHello('printHello')
    a_fun = lambda a, b: a + b
    print(a_fun(1, 2))

    f = open("test_2.py")
    print(f.read())
    f.close()

    with open("test_2.py") as fi:
        print(fi.read())

    print(os.getcwd())
    try:
        fun(1)
    except myEx:
        print("Exception")
    else:
        print("Exception111")

    c = MyClass('zhang', 15)
    c.printMsg()
