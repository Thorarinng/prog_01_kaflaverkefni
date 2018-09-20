# 9-3 Longerst word

length = 0
longest = ""

with open("words.txt", 'r') as t_file:
    for line in t_file:
        if len(line) > length:
            length = len(line)-1
            longest = line.strip()

print("Longest word is '{}' of length {}".format(longest, length))