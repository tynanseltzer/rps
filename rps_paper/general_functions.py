import numpy as np
import itertools
def graph_generator(n):
    ret = np.zeros((n, n))
    up_inds = np.triu_indices(len(ret))
    # Don't put the diags because we really want to minimize size of this
    # Also fix 1 edge because of symmetry, that's the minus 1
    combos = (itertools.product((0, 1), repeat=len(up_inds[0]) - n - 1))
    for item in combos:
        item = list(item)
        # this is ugly
        # Insert the 1 to fix
        item.insert(0, 1)
        inc = 0
        for i in range(n):
            item.insert(inc, 1)
            inc += (n - i)

        r2 = ret.astype(bool).copy()
        r2[up_inds] = item
        i_lower = np.tril_indices(len(r2))
        r2[i_lower] = r2.T[i_lower]
        r2[i_lower] = ~r2[i_lower]
        np.fill_diagonal(r2, 1)

        yield r2

def do_swap(p1, p2, dag):
    bar = dag.copy()
    bar[:, [p1, p2]] = bar[:, [p2, p1]]
    bar[[p1, p2], :] = bar[[p2, p1], :]
    return bar