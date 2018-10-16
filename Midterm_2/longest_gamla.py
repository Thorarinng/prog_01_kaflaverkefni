import string

# Function definitions start here
def open_file(fname):
    """Tekur inn texta skrá or opnar hana"""
    try:
        word_file = ''
        input_file =  open(fname, 'r')
            # for line in input_file:
            #     word_file += line
    except FileNotFoundError:
        print("File {}.txt not found!".format(fname))
    # return word_file
    return input_file

def get_longest_word(wfile):
    """Finnur lengsta ordid og skilar thvi ut"""
    longest = ''
    length = 0
    new_list = wfile.split()
    for word in new_list:
        if len(word) > length:
            longest = word
            length = len(longest)
    return longest


# The main program starts here
# filename = input("Enter name of file: ")
filename = "longest.txt"
file_stream = open_file(filename)

if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close
else:
	print('File',filename,'not found!')