# file = open('assets/spam.txt')
# print(file)

# contents = file.read()
# print(contents)
# for i in contents:
#     if i == 'e':
#         print(i)

# print('Is this file closed?', file.closed)
# file.close()
# print('Is this file closed?', file.closed)

with open('assets/spam.txt') as file:
    print(file.read())

print('Is this file closed?', file.closed)

# help(file)
# print(dir(help))

with open('assets/brain.jpg', 'rb') as f:
    contents = f.read()

with open('assets/brain_copy.jpg', 'wb') as f2:
    f2.write(contents)
