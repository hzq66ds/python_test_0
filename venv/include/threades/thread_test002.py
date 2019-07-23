import threadpool
import time


def openfileandwrite(filepath, data):
    f = open(filepath, 'a')
    f.write(data)
    f.close()


def openfileandwritelines(filepath, data):
    f = open(filepath, 'a')
    f.writelines([data, '\n'])
    f.close()


def openfileandread(filepath):
    f = open(filepath, 'r')
    print(f.read())
    f.close()


def openfileandreadlines(filepath):
    f = open(filepath, 'r')
    print(f.readlines())
    f.close()


def withopenfile(filepath):
    with open(filepath, 'r+') as f:
        f.writelines(['hello\n', 'word\n'])
        print('withopenfile:', f.readlines())


if __name__ == '__main__':
    # openfileandwrite('b.txt', 'hello')
    # openfileandread('b.txt')
    # openfileandreadlines('b.txt')
    withopenfile('b.txt')
