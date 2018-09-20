# 9-1

with open("test.txt", 'r') as t_file:
    for line in t_file:
        newLine = line.strip().replace(" ", "")
        print(newLine, end='')

