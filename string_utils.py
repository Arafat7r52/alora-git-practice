MAX_HUMAN_AGE = 150  # maximum recorded human lifespan


def reverse_string(s):
    return s[::-1]


def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")


def validate_age(age):
    """
    Validates whether the given age is within a human lifespan.

    Args:
        age (int): The age to validate.

    Returns:
        bool: True if age is between 0 and 150, False otherwise.

    Raises:
        TypeError: If age is not an integer.
    """
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    return 0 <= age <= MAX_HUMAN_AGE