from sympy import *
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigs
import numpy as np

p = symbols('rho')
l = symbols('lambda')
m = symbols('mu')

keys = [(0, 3), (1, 4), (2, 5), (3, 0), (4, 1), (5, 2), (6, 0), (8, 0)]
values = [-1/p, -1/p, -1/p, -(l + 2*m), -m, -m, -l, -l]

coords = dict(zip(keys, values))
A = SparseMatrix(None, coords)
A = A.col_insert(8, zeros(9, 3))

print(A.eigenvals())

