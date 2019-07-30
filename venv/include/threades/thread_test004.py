import concurrent.futures


def threadtest1(threadname):
    for i in range(100):
        time.sleep(1)
        print("test"+str(threadname)+str(i))


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(threadtest1, range(3))
