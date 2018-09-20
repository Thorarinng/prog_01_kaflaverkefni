# 9-5

    # Write a Python program that reads a file named words.txt containing 
    # one word/token per line with an empty line between sentences and writes
    #  out one sentence per line into a file called sentences.txt.  
    #   The program should also print out (to the screen) each sentence.

    # It is ok to have one space between the end of a sentence (e.g. period) and the last word.

with open("words.txt", 'r') as rf:
    with open("sentences.txt", 'w') as wf:
        for line in rf:
            stripped = line.strip().replace(" ", "")
            print(stripped, file=wf)
            print(stripped)