import random

wordList = []
special_char = ['@', '#', '$', '%', '^']

with open("wikipedia.txt",'r') as file:
    data = file.readlines()

    for line in data:
        words = line.split()
        
        for item in words:
            if len(item) > 5:
                wordList.append(item.capitalize())

word = random.choice(wordList)
schar = random.choice(special_char)
num = str(random.randint(10, 99))

passw = word + schar + num
print(passw)