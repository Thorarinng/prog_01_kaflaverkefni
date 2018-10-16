# Skrifið Python forrit sem biður notandann að slá inn nafn skrár sem inniheldur 
# eitt orð/tóka í línu með auðri línu á milli setninga.  Forritið prentar út lengsta 
# orðið í skránni ásamt lengd þess.  Ef inntaksskrá finnst ekki þá skal fallið 
# open_file skila None og aðalforritið prentar þá út viðeigandi villuskilaboð. 
# Aðal forritið er gefið og því má EKKI breyta.

# Write a Python program that prompts the user for an input file containing 
# one word/token per line with an empty line between sentences.  The program 
# prints out the longest word found in the file along with its length.  If the 
# input file is not found, the function open_file should return None, and the main 
# program then prints out an appropriate error message. The main program is given 
# and you are NOT allowed to change it. 

# Dæmi um línur í inntaksskrá / Example lines in input file:
# Russian
# spies
# have
# been
# accused
# of
# involvement
# in

# Dæmi um inntak/úttak -  Example input/output:
# Enter name of file: xx.txt
# File xx.txt not found!

# Enter name of file: words.txt
# Longest word is 'cyber-attacks' of length 13

# import string

# Function definitions start here
def open_file(fname):
    """Tekur inn texta skrá or opnar hana"""
    try:
        input_file =  open(fname, 'r')
        return input_file
    except FileNotFoundError:
        return 0
    

def get_longest_word(wfile):
    """Finnur lengsta ordid og skilar thvi ut"""
    longest = ''
    length = 0
    for word in wfile:
        if len(word) >= length:
            longest = word.strip() #prufa ad strippa annarsstadar
            length = len(longest)
    return longest


# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)

if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close
else:
	print('File',filename,'not found!')