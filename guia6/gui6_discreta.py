import numpy as np
from scipy.stats import binom, nbinom
import matplotlib.pyplot as plt


def graficar_continua(data) -> None:
    _, ax = plt.subplots(1,1)
    d = np.diff(np.unique(data)).min()
    left_of_first_bin = data.min() - float(d)/2
    right_of_last_bin = data.max() + float(d)/2
    x =  np.arange(left_of_first_bin, right_of_last_bin + d, d)
    ax.hist(data, bins = 30, density=False)
    plt.show()


if __name__ == "__main__":
    fig, ax = plt.subplots(3, 2)
