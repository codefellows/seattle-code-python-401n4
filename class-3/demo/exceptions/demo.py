# print('Something Wrong is about to happen!')
# print('What will be the error 'with' this line?')

# try:
#     print('What happens with the following:', 1 / 0)
# except ZeroDivisionError:
#     print('Cannot devide by 0')

# print('Keep on keeping on')

# try:
#     print('Divide by 0?', 1 / 'darth')
# except:
#     print("You can't do that!")


# try:
#     spam = 1 / 0
# except ZeroDivisionError as e:
#     print('Do not divide by 0', e)
# except Exception as e:
#     print('You did something wrong', e)
#     # print(e)

# print('Prepare for this to Break')

# try:
#     value = 'I am ' + 'words'
# except TypeError as e:
#     print(f"Something broke. Details are {e}")
# else:
#     print(f'This went well. Value is {value}')
# finally:
#     print('Clean on on isle 3')

# age = 20

# if age < 21:
#     raise ValueError("Invalid Age - Gotta be 21 for this Party")

# print('I made it')

class SocialDistanceError(Exception):
    def __init__(self, distance):
        super().__init__(f"Stay 6 feet away, not {distance}")


distance_feet = 4

if distance_feet < 6:
    raise SocialDistanceError(distance_feet)