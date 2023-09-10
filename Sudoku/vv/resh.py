from .cydoky import *


def solution(value):
    Q = 1
    for i in range(9):
        for j in range(9):
            q[i][j] = int(value[Q])
            Q += 1
    return solve(q)
def complete(value):
    Q = 1
    for i in range(9):
        for j in range(9):
            q[i][j] = int(value[Q])
            Q += 1
    return q


