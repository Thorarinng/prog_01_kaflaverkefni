# Document collection: ap_docs.txt
# What would you like to do?
# 1. Search Documents
# 2. Print Document
# 3. Quit Program
# > 1
# Enter search words: stock prices
# Documents that fit search: 16 2 221 222
# What would you like to do?
# 1. Search Documents
# 2. Print Document
# 3. Quit Program
# > 2
# Enter document number: 2
# Document #2
# The stock market closed out its worst week 

def Get_Input():
    """Asks for input, returns file"""
    #try: 
    document = input("Document collection: ")
    #except
    return document

def Get_File(doc_name):
    """"""
    #try:
    with open(doc_name, 'r') as doc:
        pass
    #except
    return doc

def Menu():
    """"""
    print("What would you like to do?")
    print("1. Search Documents")
    print("2. Print Document")
    print("3. Quit Program")
    #try
    choice = int(input("> "))
    #except
    if choice == 1:
        print("Choice 1")
    elif choice == 2:
        print("Choice 2")
    elif choice == 3:
        Quitting()


def Quitting():
    quit() # finna ut hvad er ad med quitting

def main():
    #input collection
    doc = Get_Input()
    # doc_file = get_file()

    print(doc)
    #menu
    Menu()


main()