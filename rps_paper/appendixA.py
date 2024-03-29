import numpy as np
from general_functions import graph_generator, do_swap

def best_choice_swap(n, g):
    hold = np.zeros((n, n))
    np.fill_diagonal(hold, 0)
    c = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if i != j:
                # We do the swap them subtract from the original to see what changed.
                new_g = do_swap(i, j, g)
                hold += np.abs(g.astype(int) - new_g.astype(int))
                c += 1
    # After we calculate all the swaps, we say the mathemagician
    # chose best. So if something swapped more than half the time, they choose correctly
    hold = np.minimum(hold, c - hold)
    # Average it, and we only take half the graph since it's symmetric
    return np.sum(hold) / (2 * c)

def Theorem23(n):
    curr_max = 0
    curr_min = 1000000
    for g in graph_generator(n):
        wrong_swps = best_choice_swap(n, g)
        if wrong_swps > curr_max:
            curr_max = wrong_swps
        if wrong_swps < curr_min:
            curr_min = wrong_swps
    print("Max wrong", curr_max)
    print("Min wrong", curr_min)

for i in range(3, 8):
    print(i)
    Theorem23(i)