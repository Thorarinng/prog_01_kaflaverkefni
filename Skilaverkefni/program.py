import string

mystring = "This is. my sentence. and I, am damn prou'd of it"

for i in range(len(mystring)):
    if mystring[i] in string.punctuation:
        print(mystring[i])