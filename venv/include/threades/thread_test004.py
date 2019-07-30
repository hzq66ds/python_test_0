from concurrent import futures
import time
import threading


def test(num):
    return time.ctime(), num


def threadtest(threadname):
    with threading.Lock():
        for i in range(100):
            time.sleep(1)
            print("test" + str(threadname) + str(i))


if __name__ == '__main__':
    # with futures.ThreadPoolExecutor(max_workers=1) as executor:
    #     future = executor.submit(test, 1)
    #     print(future.result())

    # with futures.ThreadPoolExecutor(max_workers=1) as executor:
    #     for future in executor.map(test, range(3)):
    #         print(future)

    with futures.ProcessPoolExecutor(max_workers=3) as executor:
        executor.map(threadtest, range(3))
