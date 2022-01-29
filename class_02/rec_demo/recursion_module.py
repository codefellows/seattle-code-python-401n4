def quick_test():
    pass


def factorial(n):
    """
    return n! (as it's sometimes written)
    e.g. factorial(3) = 3 * 2 * 1 = 6

    Note: Normally wouldn't name a package or module this way
    but wanted to be really clear about which was which

    Bonus: hover your mouse over the function name when importing
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)

    # factorial(8) = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320

    # Call Stacl

    # 8 factorial(8)
    # return 8 * factorial(8 - 1)

    # 7 factorial(7)
    # return 7 * factorial(7 - 1)

    # 6 factorial(6)
    # return 6 * factorial(6 - 1)

    # 5 factorial(5)
    # return 5 * factorial(5 - 1)

    # 4 factorial(4)
    # return 4 * factorial(4 - 1)

    # 3 factorial(3)
    # return 3 * factorial(3 - 1)

    # 2 factorial(2)
    # return 2 * factorial(2 - 1)

    # 1 factorial(1)
    # return 1

