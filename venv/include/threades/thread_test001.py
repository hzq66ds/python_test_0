import threadpool
import time


# 为线程定义一个函数
def print_time(threadName):
    count = 0
    while count < 5:
        time.sleep(2)
        count += 1
        print('%s: %s' % (threadName, time.ctime(time.time())))


if __name__ == '__main__':
    print(1)
    pool = threadpool.ThreadPool(2)
    # 创建两个线程
    threadlist = ['Thread-1', 'Thread-2']
    requests = threadpool.makeRequests(print_time, threadlist)
    
    [pool.putRequest(req) for req in requests]
    pool.wait()
    print(2)
