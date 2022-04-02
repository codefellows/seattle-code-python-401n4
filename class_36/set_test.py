# def ispangram(word):
#     ALPHA = "abcdefghijklmnopqrstuvwxyz"
#     for char in ALPHA:
#         if char not in word.lower():
#             return False
#     return True














# def ispangram(str):
#     is_str_pan = True
#     for num in range(97, 123):
#         if chr(num) not in str.lower():
#             return False

#     return is_str_pan




















import string
alphabet = set(string.ascii_lowercase)
  
def ispangram(string):
    return set(string.lower()) >= alphabet

print(ispangram('The quick brown fox'))
print(ispangram('The quick brown fox jumped over the lazy sleeping dog'))
print(ispangram('Five quacking Zephyrs jolt my wax bed'))