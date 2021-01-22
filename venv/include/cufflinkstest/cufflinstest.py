import cufflinks as cf
import threading as td
import time


def printInfo(func):
    def wrapper(*args, **kwargs):
        print("start测试测试_%s_%s" % (args, kwargs))
        aa = func(*args, **kwargs)
        print("end测试测试_%s_%s" % (args, kwargs))
        return aa
    return wrapper


@printInfo
def printNum(threadname, num):
    print("test_%s_%s" % (threadname, num))


def threadtest(threadname):
    for i in range(10):
        time.sleep(1)
        printNum(threadname, i)


if __name__ == '__main__':
    threads = list()
    for i in range(2):
        thread1 = td.Thread(target=threadtest, args=('tt'+str(i),))
        thread1.start()
        threads.append(thread1)

    # 等待子线程结束后再执行主线程
    for index, thread in enumerate(threads):
        thread.join()

    print("主线程end")

