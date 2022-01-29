from textwrap import dedent

# input('> ')

# user, age = 'Roger', 21

# print(user)
# print(age)

# print(f'What ever: {user} {age}')

# print('What ever {} {}'.format(user, age))

# print(f'Whatever')

def movie():
    return_string = f'Star Wars is the best Movie'
    return return_string

# movie()

multi_line = '''This is some text
more text on another line
and still one more line
'''
print(multi_line)

new_multi_line = dedent(multi_line)

print(new_multi_line)


if __name__ == "__main__":
    # print('I am running from within the topics.py file')
    pass 
