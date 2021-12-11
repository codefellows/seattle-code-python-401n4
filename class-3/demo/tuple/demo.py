# def make_set(my_string):
#     new_set = set(my_string)
#     new_word = ''
#     for i in new_set:
#         new_word += i
#     return new_word

# def go_through_string(my_string):
    # put into a list
    # check if the letter is in the list
    # new_list = []
    # new_word = ''
    # for i in my_string:
    #     if i not in new_word:
            # new_list.append(i)
    #         new_word += i
    # return new_word

# word1 = 'commissioner'
# word2 = 'aggressiveness'

# print(make_set(word1))

# print(go_through_string(word2))

months = ('Jan', 'Feb', 'Marr')
months = list(months)
months[2] = 'Mar'
months = tuple(months)
months[2] = 'Marr'
# months = ('Jan', 'Feb', 'Mar')
print(months)