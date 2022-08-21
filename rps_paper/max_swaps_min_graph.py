

import numpy as np
import itertools
import cProfile
from general_functions import graph_generator

# we represent a dag as a square array, 1 if row beats column, 0 if not
# assume p1 < p2
# Note diagonals stay on diagonals
def swap_value(p1, p2, dag):
    # Swap rows and columns, take diff, divide by 2
    bar = dag.copy()
    bar[:,[p1,p2]] = bar[:,[p2,p1]]
    bar[[p1,p2], :] = bar[[p2,p1], :]
    return np.sum(np.abs((dag.astype(int) - bar.astype(int))))/2

#
def max_of_min(n, swap_list):
    r1,r2 = 0,0
    curr = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if i != j:
                res = swap_value(i,j,swap_list)
                if res > curr:
                    curr = res
                    r1 = i
                    r2 = j
    return r1, r2, curr

def find_best_configs(n):
    curr = 100*n - 3
    combo = np.zeros((n,n))
    a = 0
    b = 0
    for r2 in graph_generator(n):
        q,z,c = max_of_min(n, r2)
        if c < curr:
            combo = r2.astype(int)
            curr = c
            a = q
            b = z
    print(combo)
    print("swaps", curr)
    print("person 1", a)
    print("Person 2", b)


for i in range(3, 100):
    print(i)
    find_best_configs(i)
