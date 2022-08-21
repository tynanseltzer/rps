# So for each graph, we're going to find out over all swaps how frequently each edge changes
# We'll do this by for each graph, we do all the swaps and see how much each edge changed.

import numpy as np
from general_functions import graph_generator

def do_swap(p1, p2, dag):
    bar = dag.copy()
    bar[:, [p1, p2]] = bar[:, [p2, p1]]
    bar[[p1, p2], :] = bar[[p2, p1], :]
    return bar
def swaps_of_graph(n, g):
    hold = np.zeros((n, n))
    np.fill_diagonal(hold, n ** 2)
    for i in range(n-1):
        for j in range(i+1, n):
            if i != j:
                new_g = do_swap(i, j, g)
                hold += np.abs(g.astype(int) - new_g.astype(int))
    return np.amin(hold), np.argmin(hold), hold

def find_worst_edge(n):
    curr_g = np.zeros((n, n))
    curr_min = 0
    curr_arg = 0
    c_hold = 0
    for g in graph_generator(n):
        mn, arg, hold = swaps_of_graph(n, g)
        if mn > curr_min:
            curr_g = g
            curr_min = mn
            curr_arg = arg
            c_hold = hold
    print("n", n)
    print("graph =\n", curr_g.astype(int))
    print("num swaps", curr_min)
    print("edge", curr_arg)
    print(c_hold)


for i in range(3,8):
    find_worst_edge(i)