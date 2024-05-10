"""Resolucion de ejercicios con distribuciones discretas

Las distribuciones que se usaron son:
    - Binomial
    - Uniforme Discreta
    - Binomial Negativa
    - Hipergeometrica
"""

import numpy as np
from scipy.stats import binom, hypergeom, nbinom
import matplotlib.pyplot as plt


def graficar_discreta(data) -> None:
    """Grafica la distribucion para observar y determinar que distribucion discreta utilizar

    Args:
        data (NDArray) : datos a evaluar
    """
    _, ax = plt.subplots(1,1)
    d = np.diff(np.unique(data)).min()
    left_of_first_bin = data.min() - float(d)/2
    right_of_last_bin = data.max() + float(d)/2
    x =  np.arange(left_of_first_bin, right_of_last_bin + d, d)
    ax.hist(data, bins = 30, density=True)
    plt.show()


def graficar_binomial(data, ax) -> None:
    """Genera el grafico de una distribucion binomial

    Args:
        data (NDArray): datos para graficar
        ax :objeto para agregar los graficos 
    """
    mean = np.mean(data)
    n = len(data)
    p = mean / n
    print(f"n {n}")
    print(f"p {p}")
    x = np.arange(binom.ppf(0.01, n, p),
                  binom.ppf(0.99, n, p))
    ax[0, 0].plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
    ax[0, 0].vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
    rv = binom(n, p)
    ax[0, 0].vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
    ax[0, 0].legend(loc='best', frameon=False)
    ax[0, 0].set_title("Distribucion Binomial")
    print(f"MLE Binomial\n\tp = {p}\n\tn = {n}")


def graficar_uniforme(data, ax) -> None:
    """Genera el grafico de una distribucion uniforme discreta

    Args:
        data (NDArray): datos para graficar
        ax :objeto para agregar los graficos 
    """
    d = np.diff(np.unique(data)).min()
    valor_minimo = data.min() - float(d)/2
    valor_maximo = data.max() + float(d)/2
    mean = np.mean(data)
    varianza = np.mean(data)
    x =  np.arange(valor_minimo, valor_maximo + d, d)
    ax[0, 1].hist(data, bins = 30, density=True)
    ax[0, 1].set_title("Distribucion Uniforme Discreta")
    print(f"MLE Uniforme Discreta\n\tMedia = {mean}\n\tVarianza = {varianza}")


def graficar_binomial_negativa(data, ax) -> None:
    """Genera el grafico de una distribucion binomial negativa

    Args:
        data (NDArray): datos para graficar
        ax :objeto para agregar los graficos 
    """
    varianza = np.var(data)
    mean = np.mean(data)
    n = (mean * mean) / (varianza - mean)
    p = mean / varianza
    x = np.arange(nbinom.ppf(0.01, n, p),
                  nbinom.ppf(0.99, n, p))
    ax[1, 0].plot(x, nbinom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
    ax[1, 0].vlines(x, 0, nbinom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
    rv = nbinom(n, p)
    ax[1, 0].vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
    ax[1, 0].legend(loc='best', frameon=False)
    ax[1, 0].set_title("Distribucion Binomial Negativa")
    print(f"MLE Binomial Negativa\n\tp = {p}\n\tn = {n}")


def graficar_hipergeometrica(data, ax) -> None:
    """Genera el grafico de una distribucion hypergeometrica

    Args:
        data (NDArray): datos para graficar
        ax :objeto para agregar los graficos 
    """

    """
    Se eligieron valores de n y N de manera arbitraira para poder trabajar con el modulo de
    hypergeom de scipy.stats
    """
    M = len(data)
    [n, N] = [200, 600]
    rv = hypergeom(M, n, N)
    x = np.arange(0, n + 1)
    pmf_n = rv.pmf(x)
    ax[1, 1].plot(x, pmf_n, 'bo')
    ax[1, 1].vlines(x, 0, pmf_n, lw=2)
    ax[1, 1].set_title("Distribucion Hipergeometrica")
    ax[1, 1].set_xlabel('# de n en un grupo de N')
    ax[1, 1].set_ylabel('Distribucion Hypergeometrica')
    print(f"MLE Hipergeometrica\n\tM = {M}\n\tn = {n}\n\tN = {N}")


if __name__ == "__main__":
    fig, ax = plt.subplots(2, 2)
    datos_discreto1 = np.array([4, 8, 6, 5, 3, 3, 3, 7, 5, 6, 2, 8, 7, 4, 4, 4, 4, 5, 5, 4, 5, 3, 4, 4, 5, 6, 4, 5, 5, 2, 5, 3, 3, 8, 8, 6, 4, 3, 6, 5, 3, 5, 2, 7, 4, 6, 4, 5, 5, 4, 8, 6, 7, 7, 5, 7, 3, 4, 2, 4, 5, 4, 7, 4, 4, 5, 3, 6, 3, 8, 6, 4, 1, 6, 6, 6, 6, 3, 4, 3, 7, 6, 4, 3, 4, 4, 6, 6, 7, 5, 3, 6, 6, 5, 6, 5, 5, 5, 2, 3, 2, 6, 4, 5, 7, 4, 5, 6, 4, 3, 4, 3, 7, 6, 6, 7, 6, 4, 7, 5, 6, 7, 4, 3, 4, 5, 6, 7, 1, 5, 5, 4, 3, 4, 7,  4, 5, 6, 4, 8, 8, 4, 5, 4, 4, 2, 5, 5, 2, 4, 7, 4, 3, 5, 8, 4, 6, 6, 4, 6, 4, 6, 6, 5, 3, 7, 4, 4, 2, 5, 6, 2, 5, 4, 6, 4, 6, 5, 7, 3, 4, 3, 7, 7, 4, 6, 6, 5, 5, 4, 3, 7, 7, 6, 4, 4, 6, 7, 7, 6, 6, 3, 3, 7, 5, 1, 3, 6, 1, 3, 5, 6, 6, 4, 6, 4, 4, 6, 6, 7, 6, 5, 3, 4, 4, 4, 8, 5, 7, 6, 6, 5, 5, 5, 4, 6, 4, 2, 6, 4, 7, 8, 7, 4, 2, 7, 5, 8, 8, 7, 4, 5, 7, 4, 3, 5, 7, 6, 5, 3, 5, 9, 3, 5, 7, 6, 6, 6, 4, 4, 6, 6, 7, 7, 5, 5, 6, 6, 6, 6, 7, 4, 4, 3, 5, 2, 5, 5, 4, 5, 2, 2, 6, 4, 3, 5, 6, 4, 5, 3, 2, 5, 5, 6, 6, 8, 5, 4, 6, 4, 5, 3, 2, 8, 7, 6, 5, 4, 3, 4, 5, 6, 6, 4, 8, 6, 5, 5, 5, 4, 4, 6, 2, 3, 2, 2, 7, 6, 5, 3, 5, 5, 4, 5, 5, 5, 6, 2, 4, 6, 5, 7, 6, 3, 3, 6, 2, 5, 7, 5, 5, 6, 5, 5, 7, 5, 8, 7, 4, 3, 3, 2, 3, 6, 3, 4, 7, 2, 6, 4, 3, 6, 6, 7, 6, 6, 4, 4, 6, 6, 9, 5, 4, 6, 4, 7, 7, 5, 6, 6, 3, 7, 5, 6, 4, 7, 5, 2, 7, 3, 4, 8, 8, 5, 6, 5, 4, 4, 6, 6, 6, 6, 3, 5, 3, 5, 5, 7, 4, 3, 3, 6, 5, 3, 3, 6, 3, 6, 6, 3, 3, 8, 4, 4, 6, 8, 8, 6, 4, 3, 6, 5, 5, 7, 3, 5, 2, 5, 3, 3, 3, 6, 6, 5, 8, 4, 4, 7, 4, 8, 2, 8, 2, 7, 5, 9, 3, 5, 8, 5, 6, 6, 5, 6, 5, 7, 2, 4, 8, 7, 5, 5, 4, 4, 5, 4, 5, 3, 8, 8, 6, 5, 4, 6, 6, 3, 7, 6, 8, 6, 5, 5, 7, 7, 2, 2, 4, 6, 8, 3, 5, 5, 8, 7, 7, 5, 5, 4, 3, 7, 6, 10, 9, 5, 6, 7, 7, 4, 5, 3, 8, 5, 4, 6, 5, 4, 3, 6, 5, 6, 5, 7, 5, 5, 7, 5, 3, 2, 6, 5, 6, 4, 3, 2, 4, 5, 5, 5, 7, 4, 5, 6, 5, 5, 7, 8, 3, 7, 5, 4, 5, 8, 5, 4, 6, 4, 3, 3, 3, 3, 3, 6, 4, 4, 7, 5, 6, 4, 4, 2, 3, 4, 4, 3, 3, 5, 4, 4, 5, 6, 2, 6, 6, 3, 7, 7, 3, 4, 6, 6, 4, 4, 4, 5, 5, 4, 5, 6, 2, 4, 6, 7, 5, 5, 3, 5, 5, 4, 4, 5, 2, 4, 4, 4, 3, 7, 5, 6, 6, 5, 3, 5, 5, 6, 5, 3, 4, 4, 6, 5, 4, 8, 5, 4, 3, 3, 4, 3, 4, 4, 4, 7, 3, 5, 5, 8, 3, 5, 8, 7, 6, 4, 3, 6, 7, 5, 5, 4, 6, 4, 4, 5, 5, 4, 3, 5, 4, 5, 3, 5, 5, 2, 4, 3, 3, 9, 4, 6, 4, 6, 6, 5, 5, 5, 4, 7, 7, 8, 3, 6, 7, 4, 3, 6, 5, 7, 3, 6, 4, 3, 3, 6, 6, 5, 4, 7, 5, 6, 5, 4, 5, 4, 6, 5, 4, 7, 5, 5, 7, 6, 3, 7, 6, 4, 3, 6, 5, 5, 7, 6, 3, 4, 4, 6, 2, 5, 6, 7, 4, 6, 3, 7, 3, 5, 6, 3, 4, 6, 6, 6, 6, 5, 4, 4, 4, 7, 5, 5, 5, 8, 3, 5, 5, 5, 2, 7, 7, 5, 6, 7, 6, 3, 5, 5, 5, 6, 7, 7, 5, 3, 8, 7, 3, 7, 7, 5, 5, 5, 3, 4, 6, 1, 4, 5, 5, 7, 4, 4, 6, 5, 4, 5, 3, 4, 5, 5, 7, 4, 5, 6, 2, 6, 4, 8, 3, 5, 3, 9, 5, 5, 3, 6, 4, 7, 4, 4, 2, 5, 5, 3, 6, 5, 5, 5, 5, 5, 3, 4, 7, 8, 4, 4, 6, 5, 2, 3, 6, 6, 2, 4, 4, 6, 2, 3, 6, 4, 6, 4, 3, 4, 6, 7, 7, 5, 6, 4, 4, 7, 2, 3, 4, 2, 4, 5, 5, 7, 6, 4, 4, 5, 5, 4, 6, 5, 5, 5, 4, 8, 6, 3, 7, 5, 7, 6, 5, 2, 4, 5, 6, 4, 3, 7, 8, 5, 3, 4, 2, 7, 3, 5, 4, 5, 6, 7, 4, 2, 3, 7, 7, 5, 5, 6, 4, 7, 5, 5, 5, 2, 3, 6, 3, 5, 4, 5, 4, 4, 6, 4, 5, 5, 6, 7, 6, 4, 2, 4, 5, 2, 5, 5, 4, 6, 3, 3, 6, 5, 6, 5, 4, 6, 6, 6, 4, 5, 4, 3, 7, 3, 8, 5])
    graficar_binomial(datos_discreto1, ax)

    datos_discretos2 = np.array([4, 6, 3, 5, 1, 5, 6, 6, 1, 2, 1, 4, 3, 2, 1, 5, 2, 2, 1, 2, 5, 6, 2, 6, 5, 1, 3, 2, 3, 5, 2, 6, 4, 3, 2, 3, 2, 1, 6, 3, 4, 4, 5, 2, 3, 5, 3, 2, 4, 1, 4, 5, 6, 1, 5, 2, 1, 5, 2, 4, 6, 2, 3, 2, 2, 6, 3, 5, 5, 2, 3, 3, 6, 4, 5, 6, 1, 5, 6, 5, 4, 1, 4, 1, 2, 6, 1, 4, 5, 1, 6, 1, 3, 5, 6, 6, 2, 4, 2, 6, 5, 1, 1, 5, 6, 1, 1, 1, 4, 4, 3, 2, 5, 5, 5, 3, 4, 6, 6, 3, 6, 5, 2, 1, 4, 4, 3, 4, 5, 6, 5, 3, 5, 6, 2, 3, 2, 1, 2, 1, 1, 2, 3, 6, 5, 5, 6, 1, 1, 3, 4, 2, 1, 5, 3, 2, 3, 2, 2, 6, 1, 3, 3, 6, 5, 5, 1, 1, 4, 6, 5, 2, 3, 1, 3, 3, 4, 5, 1, 3, 1, 2, 4, 2, 1, 1, 5, 3, 3, 2, 4, 6, 3, 5, 2, 2, 6, 5, 4, 5, 4, 5, 5, 1, 2, 5, 6, 5, 3, 2, 3, 2, 3, 5, 5, 1, 6, 3, 4, 1, 3, 3, 1, 6, 3, 5, 1, 5, 2, 4, 3, 6, 4, 5, 3, 5, 2, 1, 3, 2, 2, 3, 5, 6, 2, 4, 2, 6, 5, 5, 4, 2, 5, 6, 3, 1, 1, 1, 2, 4, 5, 3, 6, 3, 6, 2, 1, 2, 4, 4, 6, 5, 5, 6, 4, 4, 4, 2, 4, 3, 1, 4, 6, 1, 2, 6, 1, 6, 2, 3, 2, 2, 6, 5, 4, 4, 3, 3, 4, 5, 4, 5, 3, 1, 6, 3, 3, 2, 2, 2, 6, 2, 5, 4, 1, 3, 5, 1, 5, 5, 3, 4, 2, 6, 4, 6, 3, 3, 3, 1, 6, 4, 4, 5, 5, 5, 3, 4, 6, 3, 1, 5, 3, 3, 1, 2, 4, 6, 2, 5, 3, 1, 1, 4, 2, 4, 3, 4, 6, 1, 1, 5, 5, 3, 6, 2, 4, 3, 5, 4, 5, 4, 2, 3, 4, 6, 1, 6, 6, 1, 6, 4, 4, 4, 1, 6, 1, 4, 6, 6, 5, 5, 2, 3, 5, 1, 5, 2, 6, 2, 6, 6, 3, 5, 1, 1, 4, 6, 1, 3, 6, 3, 1, 1, 4, 1, 6, 6, 6, 4, 4, 1, 2, 2, 4, 1, 2, 1, 1, 1, 5, 6, 1, 5, 4, 2, 6, 2, 6, 2, 6, 2, 2, 2, 2, 4, 1, 3, 5, 3, 3, 6, 1, 6, 1, 1, 2, 4, 2, 4, 6, 4, 6, 3, 3, 4, 4, 6, 2, 6, 2, 3, 1, 4, 2, 6, 3, 2, 6, 4, 4, 5, 1, 5, 3, 2, 3, 6, 4, 5, 5, 5, 3, 4, 2, 6, 2, 3, 6, 5, 1, 3, 3, 4, 2, 3, 3, 5, 5, 6, 1, 4, 1, 6, 5, 2, 5, 4, 5, 4, 4, 4, 6, 4, 4, 2, 1, 3, 1, 4, 2, 5, 2, 4, 2, 2, 4, 6, 2, 3, 3, 2, 6, 5, 4, 3, 5, 2, 5, 1, 3, 2, 4, 6, 2, 4, 6, 6, 2, 5, 5, 6, 5, 1, 6, 6, 4, 5, 6, 1, 4, 2, 6, 1, 3, 1, 1, 4, 2, 3, 5, 5, 1, 4, 4, 5, 3, 2, 3, 6, 6, 2, 5, 2, 4, 6, 1, 1, 5, 4, 3, 4, 1, 1, 6, 4, 4, 1, 3, 5, 5, 4, 5, 1, 1, 4, 4, 6, 4, 3, 5, 4, 2, 6, 2, 1, 5, 4, 2, 5, 1, 3, 6, 5, 5, 3, 5, 1, 1, 3, 6, 4, 2, 4, 5, 2, 3, 3, 6, 2, 1, 2, 5, 1, 3, 2, 4, 6, 4, 6, 5, 4, 2, 2, 4, 2, 5, 1, 5, 6, 5, 6, 2, 1, 2, 3, 2, 6, 2, 2, 1, 2, 1, 4, 3, 1, 6, 4, 1, 1, 3, 6, 5, 5, 1, 2, 6, 4, 2, 2, 6, 1, 1, 1, 1, 5, 1, 5, 5, 1, 3, 4, 2, 5, 6, 6, 4, 6, 3, 6, 2, 2, 5, 1, 3, 5, 3, 1, 6, 6, 1, 5, 1, 4, 2, 5, 3, 4, 5, 1, 1, 1, 1, 3, 4, 6, 2, 3, 3, 6, 6, 2, 2, 6, 1, 3, 5, 2, 2, 6, 4, 5, 5, 2, 1, 4, 5, 2, 5, 4, 4, 3, 6, 6, 2, 4, 3, 3, 5, 5, 3, 5, 4, 1, 4, 3, 3, 4, 5, 5, 6, 3, 2, 6, 5, 4, 5, 4, 6, 3, 5, 4, 3, 2, 4, 6, 2, 2, 1, 5, 4, 2, 1, 6, 3, 4, 2, 5, 1, 2, 5, 2, 4, 4, 4, 6, 6, 1, 4, 5, 2, 3, 5, 6, 6, 5, 6, 4, 1, 2, 1, 2, 2, 1, 5, 2, 1, 2, 3, 5, 4, 2, 3, 4, 4, 2, 1, 2, 3, 4, 2, 1, 2, 5, 1, 3, 4, 2, 1, 5, 1, 6, 5, 3, 4, 3, 2, 1, 6, 5, 5, 1, 6, 1, 2, 3, 5, 2, 3, 2, 6, 5, 1, 1, 3, 4, 6, 3, 4, 2, 6, 2, 5, 6, 4, 5, 1, 4, 3, 1, 1, 3, 6, 1, 4, 5, 1, 4, 2, 4, 5, 4, 3, 5, 6, 2, 3, 6, 4, 5, 2, 3, 6, 6, 2, 4, 2, 6, 1, 3, 2, 6, 4, 6, 4, 2, 4, 5, 5, 5, 1, 2, 6, 6, 1, 4, 1, 4, 4, 3, 6, 5, 4, 3, 6, 5, 4, 4, 1, 1, 6, 5, 4, 6, 6, 2, 1, 5, 4, 6, 4, 2, 5, 6, 4, 1, 2, 5, 2, 1, 5, 2, 3, 1, 1, 1, 3, 3, 4, 6])

    graficar_uniforme(datos_discretos2, ax)

    datos_discretos3 = np.array([25, 10, 13, 3, 9, 14, 7, 8, 11, 17, 12, 9, 18, 6, 11, 15, 13, 7, 10, 9, 10, 4, 8, 18, 11, 14, 9, 20, 14, 8, 7, 8, 8, 13, 17, 6, 22, 14, 8, 13, 4, 8, 10, 7, 7, 5, 17, 11, 9, 9, 11, 11, 12, 12, 11, 4, 19, 25, 9, 9, 17, 8, 6, 9, 11, 17, 10, 7, 3, 8, 12, 13, 11, 15, 14, 4, 7, 1, 14, 7, 9, 4, 5, 6, 13, 6, 2, 15, 13, 3, 5, 14, 4, 4, 13, 16, 10, 4, 4, 17, 16, 14, 17, 21, 12, 10,20, 7, 12, 12, 6, 5, 12, 10, 19, 15, 11, 4, 3, 13, 9, 11, 7, 9, 10, 13, 5, 10, 8, 4, 9, 15, 8, 3, 24, 7, 14, 17, 11, 2, 8, 17, 14, 11, 18, 4, 13, 7, 10, 6, 3, 15, 5, 9, 23, 2, 16, 11, 10, 13, 10, 5, 23, 8, 3, 15, 10, 6, 8, 8, 11, 9, 6, 5, 12, 8, 8, 7, 9, 6, 8, 8, 8, 14, 21, 6, 9, 6, 13, 9, 3, 14, 5, 8, 9, 13, 9, 4, 23, 12, 8, 9, 5, 5, 12, 14, 12, 6, 9, 12, 9, 3, 12, 8, 11, 4, 15, 12, 10, 12, 12, 6, 21, 10, 4, 6, 6, 11, 8, 7, 10, 6, 7, 9, 4, 14, 10, 12, 8, 9, 10, 8, 7, 8, 11, 6, 5, 6, 7, 18, 10, 10, 11, 10, 4, 11, 8, 21, 10, 15, 8, 7, 12, 5, 7, 30, 11, 7, 11, 13, 10, 9, 9, 4, 10, 10, 18, 14, 12, 19, 8, 10, 6, 2, 4, 17, 1, 12, 6, 14, 7, 11, 13, 2, 2, 6, 8, 13, 21, 11, 16, 12, 4, 10, 3, 11, 7, 10, 8, 11, 7, 16, 6, 13, 4, 10, 8, 10, 6, 12, 14, 10, 10, 12, 10, 10, 5, 9, 10, 5, 17, 2, 7, 16, 18, 9, 11, 11, 6, 7, 14, 3, 6, 4, 7, 9, 12, 9, 14, 7, 11, 9, 7, 10, 7, 8, 19, 10, 6, 11, 10, 17, 21, 14, 6, 9, 5, 11, 11, 10, 13, 11, 4, 9, 9, 11, 3, 8, 9, 7, 10, 8, 2, 5, 5, 4, 8, 15, 6, 6, 10, 11, 8, 17, 16, 4, 3, 9, 9, 17, 10, 14, 19, 7, 7, 23, 9, 9, 10, 5, 13, 4, 12, 12, 3, 12, 11, 4, 16, 11, 5, 16, 7, 12, 6, 3, 12, 8, 12, 13, 4, 13, 21, 6, 19, 8, 8, 2, 12, 17, 11, 13, 10, 11, 8, 6, 4, 12, 4, 11, 6, 5, 12, 7, 19, 5, 14,24, 11, 17, 10, 7, 7, 11, 14, 7, 5, 16, 4, 7, 9, 5, 7, 8, 11, 10, 16, 8, 10, 4, 11, 7, 7, 18, 10, 7, 14, 19, 3, 10, 16, 9, 7, 6, 9, 10, 16, 9, 8, 11, 12, 6, 18, 5, 7, 7, 10, 6, 13, 8, 10, 12, 11, 15, 10, 6, 6, 7, 11, 6, 10, 10, 7, 20, 16, 10, 13, 8, 12, 7, 14, 10, 10, 11, 5, 8, 15, 8, 12, 4, 4, 10, 20, 5, 7, 12, 8, 18, 20, 11, 6, 10, 9, 6, 13, 10, 4, 7, 9, 12, 17, 11, 12, 14, 11, 9, 15, 22, 16, 4, 10, 9, 17, 11, 16, 11, 19, 7, 10, 16, 21, 12, 5, 11, 13, 8, 20, 12, 5, 21, 2, 4, 12, 12, 5, 19, 6, 9, 8, 7, 10, 5, 8, 7, 8, 2, 7, 14, 10, 13, 17, 8, 9, 4, 11, 10, 12, 8, 10, 12, 5, 10, 12, 8, 8, 10, 9, 12, 12, 10, 3, 9, 10, 11, 6, 7, 4, 9, 8, 9, 4, 6, 8, 8, 11, 5, 9, 13, 8, 4, 16, 6, 15, 10, 6, 10, 10, 12, 20, 11, 5, 11, 9, 16, 3, 18, 10, 6, 13, 7, 13, 13, 18, 10, 10, 14, 19, 11, 8, 8, 11, 9, 18, 9, 2, 9, 7, 2, 11, 6, 3, 9, 6, 13, 11, 9, 4, 7, 9, 13, 9, 6, 9, 10, 6, 9, 6, 9, 14, 8, 11, 10, 10, 14, 12, 12, 6, 5, 18, 6, 12, 15, 5,4, 20, 8, 7, 17, 15, 4, 8, 8, 13, 10, 13, 19, 12, 10, 10, 12, 12, 15, 3, 5, 7, 6, 9, 8, 6, 17, 8, 8, 5, 11, 9, 7, 5, 9, 3, 19, 19, 11, 10, 12, 16, 4, 7, 8, 10, 12, 10, 5, 3, 12, 9, 9, 19, 17, 14, 8, 9, 5, 12, 12, 8, 10, 11, 14, 5, 1, 9, 13, 9, 10, 2, 8, 9, 6, 6, 8, 11, 13, 9, 10, 23, 7, 4, 18, 7, 7, 6, 8, 7, 10, 18, 10, 8, 6, 9, 11, 10, 14, 4, 11, 7, 5, 6, 12, 16, 7, 8, 8, 5, 7, 8, 6, 9, 12, 6, 14, 13, 10, 18, 16, 5, 14, 14, 9, 12, 11, 10, 4, 7, 19, 15, 9, 14, 16, 6, 6, 13, 25, 4, 8, 18, 8, 14, 16, 10, 10, 8, 9, 3, 11, 6, 13, 10, 9, 15, 10, 10, 10, 10, 11, 26, 8, 8, 16, 2, 9, 6, 6, 15, 7, 7, 12, 12, 11, 17, 10, 20, 7, 9, 10, 18, 11, 1, 6, 5, 12, 6, 14, 15, 2, 8, 12, 7, 19, 12, 4, 19, 15, 8, 14, 9, 8, 4, 4, 11, 24, 18, 7, 8, 9, 20, 8, 10, 6, 7, 2, 16, 14, 8, 10, 10, 11, 10, 12, 12, 8, 28, 8, 17, 11, 3, 12, 7, 10, 9, 4, 6, 11, 8, 14, 5, 6, 12, 9, 12, 14, 6, 17, 8, 10, 13, 9, 16, 4, 3, 5, 9, 6, 12, 14, 7, 5, 9, 10, 12, 6, 12, 9, 3, 9, 7, 2, 13, 11, 13, 13])
    graficar_binomial_negativa(datos_discretos3, ax)

    datos_discretos4 = np.array([8,10,10,10,10,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,20,20,20])
   
    graficar_hipergeometrica(datos_discretos4, ax)
    
    plt.show()
