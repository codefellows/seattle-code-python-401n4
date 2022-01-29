# Given a ll of single char strings, write a function that will return a reversed string.
# [p] -> [y] -> [t] -> [h] -> [o] -> [n] - none
# 'nohtyp'

# algo
# create a function that takes a ll
# create a variable to hold the node data
# assign current variable to ll.head
# while loop to traverse through the ll
# concat the .value to my variable
# return the reverse of the variable string


# ['p'] -> ['y'] -> ['t'] -> ['h'] -> ['o'] -> ['n'] - none
#            ^
# temp_string = 'python'
#  

def ll_to_string(ll):
    temp_string = ''
    current = ll.head
    while current:
        temp_string += current.value
        current = current.next
    return temp_string[::-1]