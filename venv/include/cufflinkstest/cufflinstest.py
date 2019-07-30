import cufflinks as cf
import threading as td
import time


def threadtest(threadname):
    for i in range(100):
        time.sleep(1)
        print("test"+threadname+str(i))


if __name__ == '__main__':
    threads = list()
    for i in range(2):
        thread1 = td.Thread(target=threadtest, args=('tt'+str(i),))
        thread1.start()
        threads.append(thread1)

    for index, thread in enumerate(threads):
        thread.join()
