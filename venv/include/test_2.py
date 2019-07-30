import time


def printtime(func):
    def wrapper(*args, **kwargs):
        print(time.ctime())
        return func(*args, **kwargs)
    return wrapper


@printtime
def printhello(name):
    print("hello %s" % name)


if __name__ == "__main__":
    printhello("zhangsan")
