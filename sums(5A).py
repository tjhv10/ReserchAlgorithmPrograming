import heapq
from itertools import islice, takewhile

def sorted_subset_sums(S):
    """
    Generate all subset sums of a sorted list of unique positive integers in ascending order.
    
    Args:
    S (list): A list of unique positive integers.
    
    Yields:
    int: The next subset sum in ascending order.
    
    Examples:
    >>> list(sorted_subset_sums([1, 2, 4]))
    [0, 1, 2, 3, 4, 5, 6, 7]
    
    >>> list(sorted_subset_sums([1, 2, 3]))
    [0, 1, 2, 3, 3, 4, 5, 6]
    
    >>> list(sorted_subset_sums([2, 3, 4]))
    [0, 2, 3, 4, 5, 6, 7, 9]
    
    >>> list(islice(sorted_subset_sums(range(100)), 5))
    [0, 0, 1, 1, 2]
    
    >>> list(takewhile(lambda x: x <= 6, sorted_subset_sums(range(1, 100))))
    [0, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6]
    
    >>> list(zip(range(5), sorted_subset_sums(range(100))))
    [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2)]
    
    >>> len(list(takewhile(lambda x: x <= 1000, sorted_subset_sums(list(range(90, 100)) + list(range(920, 1000))))))
    1104

    >>> list(sorted_subset_sums([5, 10, 15]))
    [0, 5, 10, 15, 15, 20, 25, 30]
    
    >>> list(sorted_subset_sums([1, 1, 1]))
    [0, 1, 1, 1, 2, 2, 2, 3]
    
    >>> list(sorted_subset_sums([]))
    [0]

    >>> list(sorted_subset_sums([1, 2, 2, 3]))
    [0, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8]
    
    >>> list(sorted_subset_sums([10, 20, 30]))
    [0, 10, 20, 30, 30, 40, 50, 60]

    >>> list(islice(sorted_subset_sums([1, 2, 2, 3]), 10))
    [0, 1, 2, 2, 3, 3, 3, 4, 4, 5]

    >>> list(takewhile(lambda x: x <= 5, sorted_subset_sums([1, 2, 3])))
    [0, 1, 2, 3, 3, 4, 5]

    >>> len(list(takewhile(lambda x: x <= 50, sorted_subset_sums(range(10)))))
    1024
    """
    S = sorted(S)
    n = len(S)
    heap = [(0, 0)]
    while heap:
        curr_sum, i = heapq.heappop(heap)
        yield curr_sum

        for i in range(i, n):
            new_sum = curr_sum + S[i]
            heapq.heappush(heap, (new_sum, i + 1))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    for i in eval(input()):
        print(i, end=", ")
