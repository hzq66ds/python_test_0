import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd


if __name__ == '__main__':
    inidata = pd.DataFrame(np.random.rand(2, 50))
    # randomnum = [[x*random.random(), x*random.random()] for x in range(50)]
    randomnum = [[x*random.random(), x*random.random()] for x in inidata]
    # random.shuffle(randomnum)
    print(randomnum)
    plt.plot(randomnum)
    plt.legend(['legend1', 'legend2'])
    plt.title('title')
    plt.grid(False)
    for index, v in enumerate(randomnum):
        plt.scatter(index, v[0])
        plt.scatter(index, v[1])
    plt.show()

    fig = plt.figure()  # an empty figure with no axes
    fig.suptitle('No axes on this figure')  # Add a title so we know which it is

    fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
    plt.show()
