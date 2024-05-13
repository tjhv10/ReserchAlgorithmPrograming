def deep_sorted(data:any)->str:
    """
    Returns a string representation of the data structure with sorted elements.

    Args:
        data (dict, list, tuple, set, int, float, str): The input data structure.

    Returns:
        str: A string representation of the sorted data structure.

    Examples:
        >>> deep_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]})
        '{"a": 5, "b": [1, 2, 3, 4], "c": 6}'
        
        >>> deep_sorted([3, {"b": 2, "a": 1}])
        '[3, {"a": 1, "b": 2}]'

        >>> deep_sorted((5, [4, 3], {"c": 6, "a": 7}))
        '(5, [3, 4], {"a": 7, "c": 6})'

        >>> deep_sorted({"b": {2, 1, 3}, "a": (4, 5), "c": [6, 7]})
        '{"a": (4, 5), "b": {1, 2, 3}, "c": [6, 7]}'

        >>> deep_sorted({"d": {"z": 1, "y": 2, "x": 3}, "e": {"w": 4, "v": 5, "u": 6}})
        '{"d": {"x": 3, "y": 2, "z": 1}, "e": {"u": 6, "v": 5, "w": 4}}'

        >>> deep_sorted([3, 2, 1])
        '[1, 2, 3]'

        >>> deep_sorted({"z": {"c": 3, "a": 1, "b": 2}})
        '{"z": {"a": 1, "b": 2, "c": 3}}'

        >>> deep_sorted({"a": [5, 4, 3], "b": (3, 2, 1)})
        '{"a": [3, 4, 5], "b": (1, 2, 3)}'

        >>> deep_sorted((1, 2, 3))
        '(1, 2, 3)'

        >>> deep_sorted(5)
        '5'

        >>> deep_sorted("hello")
        'hello'
    """
    if isinstance(data, dict):
        sorted_items = sorted(data.items(), key=lambda x: str(x[0]))  # Sort dictionary items by keys
        return "{" + ", ".join(f'"{k}": {deep_sorted(v)}' for k, v in sorted_items) + "}"
    elif isinstance(data, list):
        return "[" + ", ".join(deep_sorted(item) for item in sorted(data, key=str)) + "]"
    elif isinstance(data, tuple):
        return "(" + ", ".join(deep_sorted(item) for item in sorted(data, key=str)) + ")"
    elif isinstance(data, set):
        return "{" + ", ".join(deep_sorted(item) for item in sorted(data, key=str)) + "}"
    else:
        return str(data)


# Run doctests
if __name__ == "__main__":
   import doctest
   x = eval(input())
   print(deep_sorted(x))
   doctest.testmod()

