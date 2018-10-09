#12-5 GAME OF EIGHTS

#game_of_eights() function goes here
def game_of_eights(i_list):
    """athugar hvort 8 se lika i saetinu a undan"""
    is_eight = False

    # i_list = change_to_ints(nlist)

    for i in range(len(i_list)):
        if i_list[i] == 8 and i_list[i-1] == 8:
            is_eight = True

    print(is_eight)

def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    # remainder of main() goes here
    # i_list = change_to_ints(a_list)
    i_list = []
    try:
        for s_num in a_list:
           num = int(s_num)
           i_list.append(num)

    except:
        print("Error. Please enter only integers.")
        return 

    game_of_eights(i_list)
main()


############################################################################
# def change_to_ints(nlist):
#     """Breytir listann i ints"""
#     i_list = []
#     try:
#         for s_num in nlist:
#            num = int(s_num)
#            i_list.append(num)

#     except:
#         print("Error. Please enter only integers")
#         exit 

#     return i_list

# def main():
#     a_list = input("Enter elements of list separated by commas: ").split(',')
#     # remainder of main() goes here
#     # i_list = change_to_ints(a_list)
#     i_list = []
#     try:
#         for s_num in a_list:
#            num = int(s_num)
#            i_list.append(num)

#     except:
#         print("Error. Please enter only integers")
#         return 

#     game_of_eights(i_list)
# main()





# def game_of_eights(alist):
#     eights = False
#     prev = '0'
#     for i in alist:
#         try:
#             i = int(i)
#             i = str(i)
#         except:
#             print("Error. Please enter only integers.")
#             return

#         if i == '8' and prev == '8':
#             eights = True
#         prev = i
#     print(eights)
            
# def main():
#     a_list = input("Enter elements of list separated by commas: ").split(',')
#     game_of_eights(a_list)

# main()