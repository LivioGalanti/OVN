import itertools
import numpy as np
from Network import Network
import pandas as pd
from random import shuffle, random, choice
import copy
import matplotlib.pyplot as plt


# used for the traffic matrix
def main():
    sat_percent = 50
    # fixed rate_____________________________________________________________________________
    network = Network('nodes.json', 'fixed_rate')
    n_node = len(network.nodes.keys())
    saturation_fixed = []
    M_fixed = []
    M = 1
    while 1:
        t_mtx = np.ones((n_node, n_node)) * 100 * M
        for i in range(n_node):
            t_mtx[i][i] = 0
        elements = list(itertools.permutations(network.nodes.keys(), 2))
        n_elem = len(elements)
        for e in elements:  # remove the diagonal
            if e[0] == e[1]:
                elements.remove(e)
        for i in range(100):
            if len(elements) == 0:
                break
            el = choice(elements)
            val = network.upgrade_traffic_matrix(t_mtx, el[0], el[1])
            if (val == 0) | (val == np.inf):
                elements.remove(el)
        sat = 0
        for row in t_mtx:
            for el in row:
                if el == float('inf'):
                    sat += 1
        sat = sat / n_elem * 100
        saturation_fixed.append(sat)
        M_fixed.append(M)
        if sat > sat_percent:
            break
        M += 1
        network.free_space()
    plt.plot(M_fixed, saturation_fixed)
    plt.title('Saturation Fixed-Rate')
    plt.xlabel('M')
    plt.ylabel('% of unsatisfied requests')
    plt.grid(linestyle='-', linewidth=0.5)
    plt.show()

    # flex rate_____________________________________________________________________________
    network_flex_rate = Network('nodes.json', 'flex_rate')
    n_node = len(network_flex_rate.nodes.keys())
    saturationflex = []
    Msflex = []
    M = 1
    while(1):
        t_mtx = np.ones((n_node, n_node)) * 100 * M
        for i in range(n_node):
            t_mtx[i][i] = 0
        elements = list(itertools.permutations(network_flex_rate.nodes.keys(), 2))
        n_elem = len(elements)
        for e in elements:  # remove the diagonal
            if e[0] == e[1]:
                elements.remove(e)
        for i in range(100):
            if len(elements) == 0:
                break
            el = choice(elements)
            val = network_flex_rate.upgrade_traffic_matrix(t_mtx, el[0], el[1])
            if (val < 0) | (val == np.inf):
                elements.remove(el)
        sat = 0
        for row in t_mtx:
            for el in row:
                if el == float('inf'):
                    sat += 1
        sat = sat / n_elem * 100
        saturationflex.append(sat)
        Msflex.append(M)
        if sat > sat_percent:
            break
        M += 1
        network_flex_rate.free_space()
    plt.plot(Msflex, saturationflex)
    plt.title('Saturation Flex-Rate')
    plt.xlabel('M')
    plt.ylabel('% of unsatisfied requests')
    plt.grid(linestyle='-', linewidth=0.5)
    plt.show()

    # shannon________________________________________________________________________________
    network_shannon = Network('nodes.json', 'shannon')
    n_node = len(network_shannon.nodes.keys())
    saturationshan = []
    Msshan = []
    M = 1

    while(1):
        t_mtx = np.ones((n_node, n_node)) * 100 * M
        for i in range(n_node):
            t_mtx[i][i] = 0
        elements = list(itertools.permutations(network_shannon.nodes.keys(), 2))
        n_elem = len(elements)
        for e in elements:  # remove the diagonal
            if e[0] == e[1]:
                elements.remove(e)
        for i in range(100):
            if len(elements) == 0:
                break
            el = choice(elements)
            val = network_shannon.upgrade_traffic_matrix(t_mtx, el[0], el[1])
            if (val < 0) | (val == np.inf):
                elements.remove(el)
        sat = 0
        for row in t_mtx:
            for el in row:
                if el == float('inf'):
                    sat += 1
        sat = sat / n_elem * 100
        saturationshan.append(sat)
        Msshan.append(M)
        if sat > sat_percent:
            break
        M += 1
        network_shannon.free_space()
    plt.plot(Msshan, saturationshan)
    plt.title('Saturation Parameter Shannon')
    plt.xlabel('M')
    plt.ylabel('% of unsatisfied requests')
    plt.grid(linestyle='-', linewidth=0.5)
    plt.show()
    plt.plot(M_fixed, saturation_fixed, label='fixed-rate')
    plt.plot(Msflex, saturationflex, label='flex-rate')
    plt.plot(Msshan, saturationshan, label='shannon')
    plt.xlabel('M')
    plt.ylabel('% of unsatisfied requests')
    plt.grid(linestyle='-', linewidth=0.5)
    plt.legend(loc='lower right')
    plt.title('Saturation Parameter')
    plt.show()


if __name__ == "__main__":
    main()