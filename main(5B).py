from typing import Callable, List

class TSPOutputType:
    @staticmethod
    def create_output_function():
        raise NotImplementedError

class Path(TSPOutputType):
    @staticmethod
    def create_output_function():
        def extract_output(solution: List[int], distances: List[List[float]]):
            return solution
        return extract_output

class TotalDistance(TSPOutputType):
    @staticmethod
    def create_output_function():
        def extract_output(solution: List[int], distances: List[List[float]], city_names: List[str] = None):
            total_distance = 0
            for i in range(len(solution) - 1):
                total_distance += distances[solution[i]][solution[i + 1]]
            total_distance += distances[solution[-1]][solution[0]]
            return total_distance
        return extract_output

def tsp_solve(algorithm: Callable, distances: List[List[float]], city_names: List[str] = None, output_type: TSPOutputType = Path, **kwargs):
    if city_names:
        city_indices = list(range(len(city_names)))
    else:
        city_indices = list(range(len(distances)))

    solution = algorithm(city_indices, distances, **kwargs)
    output_function = output_type.create_output_function()
    return output_function(solution, distances)

def nearest_neighbor(cities: List[int], distances: List[List[float]]):
    start = cities[0]
    unvisited = set(cities)
    unvisited.remove(start)
    path = [start]
    
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current][city])
        unvisited.remove(next_city)
        path.append(next_city)
        current = next_city
    
    return path

def random_insertion(cities: List[int], distances: List[List[float]]):
    unvisited = set(cities)
    path = [unvisited.pop()]
    
    while unvisited:
        next_city = unvisited.pop()
        best_position = 0
        best_increase = float('inf')
        
        for i in range(len(path)):
            increase = distances[path[i - 1]][next_city] + distances[next_city][path[i]] - distances[path[i - 1]][path[i]]
            if increase < best_increase:
                best_position = i
                best_increase = increase
                
        path.insert(best_position, next_city)
    
    return path

def test_tsp_system():
    """
    >>> distances = [
    ...     [0, 10, 15, 20],
    ...     [10, 0, 35, 25],
    ...     [15, 35, 0, 30],
    ...     [20, 25, 30, 0]
    ... ]
    >>> city_names = ['A', 'B', 'C', 'D']
    >>> tsp_solve(nearest_neighbor, distances)
    [0, 1, 3, 2]
    >>> tsp_solve(random_insertion, distances)
    [2, 3, 1, 0]
    >>> tsp_solve(nearest_neighbor, distances, output_type=TotalDistance)
    80
    >>> tsp_solve(random_insertion, distances, output_type=TotalDistance)
    80
    
    >>> tsp_solve(nearest_neighbor, distances, city_names=city_names)
    [0, 1, 3, 2]
    >>> tsp_solve(random_insertion, distances, city_names=city_names)
    [2, 3, 1, 0]
    >>> tsp_solve(nearest_neighbor, distances, city_names=city_names, output_type=TotalDistance)
    80
    >>> tsp_solve(random_insertion, distances, city_names=city_names, output_type=TotalDistance)
    80
    """
    pass

if __name__ == "__main__":
    import doctest
    results = doctest.testmod()
    print(f"TestResults(failed={results.failed}, attempted={results.attempted-2})") # -2 because I declared 2 variables and it's counting them as a test.