from faker import Faker
import shutil

fake = Faker('en_US')

# print(dir(fake))


# print(fake_word)

# for _ in range(100):
#     fake_word = fake.word()
#     print(fake_word)

# fake_word = fake.word()

# print(fake_word)

# fake_words = fake.words(100)
# print(fake_words)

# fake_sentences = fake.sentences(10)
# print(fake_sentences)

# fake_paragraph = fake.paragraph()
# print(fake_paragraph)

# fake_phonenum = fake.phone_number()
# print(fake_phonenum)

content = ''

for _ in range(100):
    content += fake.paragraph()
    content += fake.email()
    content += fake.paragraph()
    content += fake.phone_number()
    content += fake.paragraph()
    content += fake.email()
    content += fake.phone_number()

# print(content)


with open('content.txt', 'w+') as f:
    f.write(content)

shutil.copy('content.txt', 'assets')
