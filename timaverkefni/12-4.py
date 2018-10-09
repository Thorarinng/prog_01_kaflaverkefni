#12-4 MERGE LISTS

def merge_lists(alist, blist):
    clist = alist
    for i in blist:
        if i not in clist:
            clist.append(i)
    clist.sort()
    return clist



# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
