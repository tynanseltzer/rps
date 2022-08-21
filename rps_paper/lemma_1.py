import numpy as np
from general_functions import graph_generator, do_swap

# this script is for lemma 1, "suppose that n > 7 and fix a ...

# For every graph show average victory reversals is less than mimumum non by guessing no change

def calc_avg_swaps(n, g):
    hold = np.zeros((n, n))
    np.fill_diagonal(hold, 0)
    c = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if i != j:
                new_g = do_swap(i, j, g)
                hold += np.abs(g.astype(int) - new_g.astype(int))
                c+= 1
    return np.sum(hold) / (2*c)

def lemma_1(n):
    curr_avg = 0
    curr_graph = 0
    for g in graph_generator(n):
        avg = calc_avg_swaps(n, g)
        if avg > curr_avg:
            curr_avg = avg
            curr_graph = g

    print("n", n)
    print("avg", curr_avg)
    print("graph", curr_graph.astype(int))


for i in range (3, 8):
    lemma_1(i)