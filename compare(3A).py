import numpy as np
from scipy.optimize import root
import matplotlib.pyplot as plt
from time import perf_counter

def measure_time(func, *args, **kwargs):
    """
    Measure the execution time of a function.

    Parameters:
        func (callable): The function to measure its execution time.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        Tuple[float, Any]: A tuple containing the execution time in seconds and the result of the function call.
    """
    start = perf_counter()
    res = func(*args, **kwargs)
    end = perf_counter()
    return end - start, res


def solve_with_root(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Solve a system of linear equations using scipy.optimize.root.

    Parameters:
        a (np.ndarray): Coefficient matrix.
        b (np.ndarray): Dependent variable values.

    Returns:
        np.ndarray: Solution vector.

    Examples:
    >>> import numpy as np
    >>> from scipy.optimize import root
    >>> # Define the coefficient matrix
    >>> A = np.array([[3, 2], [2, 1]])
    >>> # Define the dependent variable values
    >>> b = np.array([1, 2])
    >>> # Solve the system of equations using solve_with_root
    >>> x = solve_with_root(A, b)
    >>> # Check if the solution is correct
    >>> np.allclose(np.dot(A, x), b)
    True
    """
    def equation_to_solve(x: np.ndarray) -> np.ndarray:
        return np.dot(a, x) - b
    
    initial_guess = np.zeros_like(b)
    solution = root(equation_to_solve, initial_guess)
    return solution.x



def test_solve_with_root():
    """
    Test the solve_with_root function.

    It generates random test matrices and verifies that the solution obtained
    by solve_with_root matches the solution obtained by numpy.linalg.solve.
    """
    # Generating random test matrices
    np.random.seed(0)  # For reproducibility
    for _ in range(10):
        n = np.random.randint(1, 10)  # Random size of the matrix
        a = np.random.rand(n, n)
        b = np.random.rand(n)
        
        # Solve using solve_with_root and numpy.linalg.solve
        x_root = solve_with_root(a, b)
        x_numpy = np.linalg.solve(a, b)
        
        # Check if the solutions are close
        assert np.allclose(x_root, x_numpy), f"Solutions do not match for matrix size {n}"


def compare_solution_methods():
    """
    Compare the performance of solve_with_root and numpy.linalg.solve.

    It measures the execution time of both functions for random inputs of various sizes
    and plots the results.
    """
    sizes = np.arange(1, 1001, 50)
    times_root = []
    times_numpy = []

    for size in sizes:
        a = np.random.rand(size, size)
        b = np.random.rand(size)

        # Measure time for solve_with_root
        time_taken, _ = measure_time(solve_with_root, a, b)
        times_root.append(time_taken)

        # Measure time for numpy.linalg.solve
        time_taken, _ = measure_time(np.linalg.solve, a, b)
        times_numpy.append(time_taken)

    plt.plot(sizes, times_root, label='solve_with_root')
    plt.plot(sizes, times_numpy, label='numpy.linalg.solve')
    plt.xlabel('Matrix size')
    plt.ylabel('Time (s)')
    plt.title('Comparison of Solution Methods')
    plt.legend()
    plt.grid(True)
    plt.savefig("comparison.png")
    # plt.show()


if __name__ == '__main__':
    test_solve_with_root()
    compare_solution_methods()

