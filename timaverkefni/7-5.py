# palindrome function definition goes here
def is_palindrome(strengur):
    nyr_strengur = strip(strengur)
    if nyr_strengur and (nyr_strengur[::-1] == nyr_strengur):
        return print('"{}"'.format(strengur), "is a palindrome.")
    else:
        return print('"{}"'.format(strengur), "is not a palindrome.")

def strip(orgStrengur):
    samsett = ""
    temp = ""
    for stafur in orgStrengur:
        if stafur.isalpha(): 
            samsett = temp + stafur
        temp = samsett
    return samsett.lower()


in_str = input("Enter a string: ")

# call the function and print out the appropriate message
is_palindrome(in_str)