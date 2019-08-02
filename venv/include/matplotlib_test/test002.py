import sys
sys.path.append(r"/Users/hanzhiqiang/Desktop/WorkSpace/pythonWorkspace/python_test_0/venv/include/mysqljdbc")
import matplotlib.pyplot as plt
from scipy import special
import numpy as np
import mysqljdbc as mj
import matplotlib.pyplot as plt
import random
import pandas as pd


def plotdata(title, data):
    plt.plot(data)
    plt.legend(title)
    plt.show()


if __name__ == '__main__':
    a = 2.
    s = np.random.zipf(a, 1000)
    count, bins, ignored = plt.hist(s[s < 50], 50, density=True)
    x = np.arange(1., 50.)
    y = x ** (-a) / special.zetac(a)
    plt.plot(x, y / max(y), linewidth=2, color='r')
    plt.show()

    # data = mj.select("SELECT DATE_FORMAT(start_time,'%y-%M-%d'),count(1) from t_response where taskid_owner='99c916f528a24a7ba282de575ceb28b9' GROUP BY DATE_FORMAT(start_time,'%y-%M-%d') order by DATE_FORMAT(start_time,'%y-%M-%d')")
    # datalist_x = [a[0] for a in data]
    # datalist_y = [a[1] for a in data]
    # plt.plot(datalist_x, datalist_y)
    # plt.legend(['gsk'])
    # plt.xlabel('x轴')
    # plt.ylabel('y轴')
    # plt.show()

    fig, (ax_lst0, ax_lst1) = plt.subplots(1, 2)  # a figure with a 2x2 grid of Axes
    inidata = pd.DataFrame(np.random.rand(2, 50))
    # randomnum = [[x*random.random(), x*random.random()] for x in range(50)]
    randomnum = [[x * random.random(), x * random.random()] for x in inidata]
    # random.shuffle(randomnum)
    ax_lst0.plot([[x * random.random()] for x in inidata])
    ax_lst1.plot([[x * random.random()] for x in inidata])
    plt.legend(['legend1', 'legend2'])
    plt.title('title')
    ax_lst0.grid(True)
    plt.grid(True)
    plt.xlabel('xxx')
    plt.ylabel('yyy')
    for index, v in enumerate(randomnum):
        ax_lst0.scatter(index, v[0])
        ax_lst1.scatter(index, v[1])
    plt.show()

    x = np.arange(0, 10, 0.2)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.xlabel('xxx')
    plt.ylabel('yyy')
    plt.show()
