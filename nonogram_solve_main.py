"""
AUTHOR: KIERAN WACHSMUTH, 30th Jun 2020

Main script for solving a Nonogram.
"""
import numpy as np
#import matplotlib.pyplot as plt
from useful_fns import load_obj
from permutator import permutate
#
x = load_obj('nonogram_x')
y = load_obj('nonogram_y')
dim_x = len(x)
dim_y = len(y)
# Generate all solutions for each column 'x':
sol_dict = {}
for i in range(dim_x):
    sol_dict[i] = permutate(dim_x,x[i])