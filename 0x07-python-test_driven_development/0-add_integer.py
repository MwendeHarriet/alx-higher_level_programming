def add_integer(a, b=98):
    """
    This adds two integers a and b.
    Args:
        a (int/float): Number(1st).
        b (int/float): Number(2nd).
    Returns:
        int: a + b.
    Raises:
        TypeError: If a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
