import matplotlib.pyplot as plt


def plotdata(title, data):
    plt.plot(data)
    plt.legend(title)
    plt.show()


if __name__ == '__main__':
    data = [[10, 11], [14, 13], [12, 12], [9, 10], [4, 5], [5, 9]]
    title = ['t1', 't2']
    plotdata(title, data)
