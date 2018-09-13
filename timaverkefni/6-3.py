# happiness is when what you think, what you say, and what you do are in harmony
s = input("Input a string: ")

leitarord = 'o'

for index, strengur in enumerate(s):
    if strengur in leitarord:
        print(index)