import numpy as np
import time
from scipy.optimize import minimize
import cvxpy as cp
import matplotlib.pyplot as plt

def generate_linear_system(size):
    A = np.random.rand(size, size)
    b = np.random.rand(size)
    return A, b

def solve_with_scipy(A, b):
    start_time = time.time()
    minimize(lambda x: np.linalg.norm(A.dot(x) - b), np.zeros(len(b)))
    end_time = time.time()
    return end_time - start_time

def solve_with_cvxpy(A, b):
    start_time = time.time()
    x = cp.Variable(len(b))
    objective = cp.Minimize(cp.norm(A @ x - b))
    cp.Problem(objective).solve()
    end_time = time.time()
    return end_time - start_time

sizes = [10, 20, 50, 100]  # Sizes of the linear systems to test
scipy_times = []
cvxpy_times = []

for size in sizes:
    a, b = generate_linear_system(size)
    scipy_time = solve_with_scipy(a, b)
    cvxpy_time = solve_with_cvxpy(a, b)
    scipy_times.append(scipy_time)
    cvxpy_times.append(cvxpy_time)


plt.plot(sizes, scipy_times, label='Scipy')
plt.plot(sizes, cvxpy_times, label='CVXPY')
plt.xlabel('System Size')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime Comparison of Scipy and CVXPY')
plt.legend()
plt.grid(True)
plt.savefig("comparison.png")
plt.show()


