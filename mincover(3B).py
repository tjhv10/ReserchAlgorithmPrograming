import subprocess, sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxpy"], stdout=subprocess.DEVNULL)

import networkx as nx
from time import perf_counter

def mincover(graph: nx.Graph)->int:
    n = len(graph.nodes())
    if n==0:
        return 0
    import cvxpy as cp
    x = cp.Variable(n, boolean=True)
    constraints = []
    for i, j in graph.edges():
        constraints.append(x[i] + x[j-1] >= 1)
    problem = cp.Problem(cp.Minimize(cp.sum(x)), constraints)
    try:
        problem.solve(solver=cp.GLPK_MI)
        return int(sum(x.value))
    except cp.error.SolverError as e:
        print("Solver error:", e)
        return None

def measure_time(func, *args, **kwargs):
    start = perf_counter()
    res = func(*args, **kwargs)
    end = perf_counter()
    return end - start, res

if __name__ == '__main__':
    print(mincover((nx.Graph(eval(input())))))