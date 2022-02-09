# shift 11
# IWT FJXRZ QGDLC UDM 
# THE QUICK BROWN FOX
# MAX 
# THE QUICK BROWN FOX JUMPED OVER THE LAZYLY SLEEPING DOG
import nltk
from nltk.corpus import words, names
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)


words_list = words.words()
names_list = names.words()
# print(words_list)

test_sentence = 'THE QUICK BROWN FOX JUMPED OVER THE LAZYLY SLEEPING DOGKJBDF'
word_list_test = test_sentence.split(' ')

for word in word_list_test:
    if word.lower() in words_list:
        print(f'The word {word} is in the list')
    else:
        print(f'The word {word} is not in the list')