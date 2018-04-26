import matplotlib.pyplot as plt
import numpy as np


def dgp(times=100, pause=0.01, random=False, fit=False):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    x_dgp = np.random.uniform(0, 1, times) * 10
    if random is True:
        y_dgp = np.array(list(map(lambda l: -2 + 0.4 * l + np.random.normal(), x_dgp)))
    else:
        y_dgp = np.array(list(map(lambda l: -2 + 0.4 * l, x_dgp)))

    x_fit = np.arange(0, 10, 0.01)

    for i in range(times):
        x_show = x_dgp[:i + 1]
        y_show = y_dgp[:i + 1]
        X = np.matrix(np.stack((np.ones(i + 1), x_show))).T
        y = np.matrix(y_show).T
        b = (X.T * X).I * X.T * y
        b_0 = b[0, 0]
        b_1 = b[1, 0]
        ax1.clear()
        ax1.axis([0, 10, -5, 5])
        ax1.scatter(x_show, y_show)
        ax1.text(1, 4, 'observations: {}'.format(i + 1), fontsize=16)
        if fit is True:
            ax1.plot(x_fit, b_0 + b_1 * x_fit, color='r')
            ax1.text(1, 3.5, 'y = {:.3f} + {:.3f} * x'.format(b_0, b_1), fontsize=16)
        plt.pause(pause)

    while True:
        plt.pause(0.1)
