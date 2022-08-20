

import numpy as np
import itertools
import cProfile

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
    ret = np.zeros((n,n))
    up_inds = np.triu_indices(len(ret))
    # Don't put the diags because we really want to minimize size of this
    combos = (itertools.product((0,1), repeat=len(up_inds[0]) - n))
    curr = 100*n - 3
    combo = ()
    a = 0
    b = 0
    for item in combos:
        item = list(item)
        for i in range(n):
            item.insert(i * (n+1), 1)
        r2 = ret.astype(bool).copy()
        r2[up_inds] = item
        i_lower = np.tril_indices(len(r2))
        r2[i_lower] = r2.T[i_lower]
        r2[i_lower] = ~r2[i_lower]
        np.fill_diagonal(r2, 1)
        q,z,c = max_of_min(n, r2)
        if c < curr:
            combo = item
            curr = c
            a = q
            b = z
    print(combo)
    print(curr)
    print(a)
    print(b)


find_best_configs(7)