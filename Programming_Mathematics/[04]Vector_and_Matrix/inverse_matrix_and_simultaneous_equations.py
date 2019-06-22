# A*x = y 연립방정식의 해는
# x = np.dot(inverse(A), y)
import numpy as np

def mat_solve(A, y):
    # To-do
    inv = np.linalg.inv(A)
    return np.dot(inv, y)



print(mat_solve(np.array([[1, 2], [3, -1]]),np.array([[1], [0]])))
