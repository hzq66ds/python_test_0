import time

def printtime(func):
    def wrapper(*args, **kwargs):
        print(time.ctime())
        return func(*args, **kwargs)
    return wrapper

@printtime
def printhello(name):
    print("hello %s" % name)

if __name__=="__main__":
    printhello("zhangsan")
    aa = '共33538条数据 当前:1/1677页'
    for dt_min in range(int(aa[aa.index('/')+1:aa.index('页')])):
        print(dt_min)