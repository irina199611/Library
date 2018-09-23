import random

moods = ['веселый','серьезный','злой','бодрый','мечтательный','кввёлый','креативний']
mood = random.sample(moods, 1)

f = open('names.txt', 'r', encoding='utf-8')

# print(dir(f))
file_content = f.readlines()
# replace("\n", "")
for element in file_content:
    file_content[file_content.index(element)] = element.replace("\n", "")

# print(file_content)

# phrase = f'{file_content[0]} сегодня {moods[0]}.'
# phrase = f'{file_content[0]} сегодня {random.sample(moods, 1)[0]}.'
# print(phrase)


for name in file_content:
    phrase = f'{name} сегодня {random.sample(moods, 1)[0]}.'
    print(phrase)


