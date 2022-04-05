def is_sorted_ascending(lst):
    previous = lst[0]
    for number in lst:
        if number < previous:
            return False
        previous = number
    return True

print(is_sorted_ascending([3, 2, 1]))
print(is_sorted_ascending([1, 2, 3]))
