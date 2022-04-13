# define a function that takes a list
# assign a variable to hold the total
# check to see if the list is empty (clarifying question)
    # check the lenght of the ll and if 0, return 0
# loop through the list
# set a variable to track total in each list as a string (to concat)
    # assign the current to .head
    # check while there is a current
        # concat the value as a string to tracking variable
        # traverse to next
    # convert tracking to int and add to variable holding total
# return total

# The lists will be passed as parameters.

# ll1: [5]->[9]->[9] -> None = 599
# ll2: [2]->[1]->[1] = 211
# ll3: [1]->[4]->[1] = 141
# 951

# ([ll1, ll2, ll3])

def sum_linked_lists(lst):
    total_sum = 0
    if len(lst) == 0:
        return total_sum

    for ll in lst:
        list_total = ''
        current = ll.head
        while current:
            list_total += str(current.value)
            current = current.next
        total_sum += int(list_total)
    return total_sum
