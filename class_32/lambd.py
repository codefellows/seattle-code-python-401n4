def this_function(x):
    return x

this_var = this_function(5)
# exptected return would be 5.

x = lambda x: x
x(5)
# expected return would be 5


def add_one(x):
    return x + 1

add_one_var = add_one(5)
# expected 6

x = lambda x: x + 1

print(x(5))

# expected 6

def add_all(x, y, z):
    return x + y + z

sum_all = add_all(1, 2, 3)
# Expected 6

x = lambda x, y, z: x + y + z
print(x(1, 2, 3))

print(x)
x = lambda x, y: a if x>y else b

