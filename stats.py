from collections import Counter


def mean(numbers: list[float]) -> float:
    """
    Returns the arithmetic mean of a list of numbers.

    Args:
        numbers (list[float]): A non-empty list of numbers.

    Returns:
        float: The mean value.

    Raises:
        ValueError: If the list is empty.
        TypeError: If input is not a list or contains non-numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate mean of empty list")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numbers")
    return sum(numbers) / len(numbers)


def median(numbers: list[float]) -> float:
    """
    Returns the median value of a list of numbers.

    Args:
        numbers (list[float]): A non-empty list of numbers.

    Returns:
        float: The median value.

    Raises:
        ValueError: If the list is empty.
        TypeError: If input is not a list or contains non-numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate median of empty list")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numbers")
    sorted_numbers = sorted(numbers)
    mid = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return float(sorted_numbers[mid])


def mode(numbers: list[float]) -> float:
    """
    Returns the most frequently occurring value in a list.

    Args:
        numbers (list[float]): A non-empty list of numbers.

    Returns:
        float: The mode value.

    Raises:
        ValueError: If the list is empty.
        TypeError: If input is not a list or contains non-numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate mode of empty list")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numbers")
    counts = Counter(numbers)
    return counts.most_common(1)[0][0]