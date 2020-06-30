"""
AUTHOR: KIERAN WACHSMUTH, 30th Jun 2020

function(s) to use for solving a Nonogram. Implements a package 'combinatorics',
https://phillipmfeldman.org/Python/combinatorics.html.
"""
import numpy as np
from combinatorics import unlabeled_balls_in_labeled_boxes as box_perm
def permutate(N,lst):
    # we want only excess zeros
    N_zeros = N - sum(lst) - (len(lst)-1)
    solutions = []
    if N_zeros == 0:
        triv_solution = []
        for j in range(N-1):
            triv_solution += list(np.ones(lst[j],dtype=int))
            triv_solution += [0]
        triv_solution += list(np.zeros(sol[-1],dtype=int))
        solutions.append(solution)
        return
    """box_arr = (np.ones(len(lst)+1,dtype=int))*int(N_zeros)
    print(box_arr)
    box_sizes = list(box_arr)
    print(box_sizes)"""
    box_sizes = []
    for i in range(len(lst)+1):
        box_sizes.append(N_zeros)
    for sol in list(box_perm(N_zeros,box_sizes)):
        # now generate the row/column solution:
        solution = list(np.zeros(sol[0],dtype=int))
        for j in range(len(sol)-2):
            solution += list(np.ones(lst[j],dtype=int))
            solution += [0]
            solution += list(np.zeros(sol[j+1],dtype=int))
        solution += list(np.ones(lst[-1],dtype=int))
        solution += list(np.zeros(sol[-1],dtype=int))
        solutions.append(solution)
    return solutions