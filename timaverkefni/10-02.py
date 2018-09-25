# 10-2
import string

def to_list(strengur):
    replace_str = strengur.replace(",", " ")
    nyr_strengur = replace_str.split()
    return nyr_strengur

# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)