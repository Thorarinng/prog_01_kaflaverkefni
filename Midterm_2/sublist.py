# Dæmi um inntak/úttak - Example input/output:
 
# Example 1:
# Enter a list separated with commas: 1,2,3
# [[], ['1'], ['1', '2'], ['1', '2', '3'], ['2'], ['2', '3'], ['3']]
 
# Example 2:
# Enter a list separated with commas: 1,2,a,b
# [[], ['1'], ['1', '2'], ['1', '2', 'a'], ['1', '2', 'a', 'b'], ['2'], ['2', 'a'], ['2', 'a', 'b'], ['a'], ['a', 'b'], ['b']]

def make_list(input_string):
    """Tekur streng og splittar honum upp i fylki"""
    split_list = input_string.split(',')
    return split_list

def make_sublist(split_list):
    """Tekur fylkin og radar saman undir listum"""
    split_list = make_list(split_list)
    # adgerdir
    new_list = []
    tomurListi = []
 
    
    for i in range(len(split_list)):
        for j in range(len(split_list-1)):
            new_lis.append(split_list[i:j])
    sub_lists = sorted(new_list)
    return sub_lists

# Main program starts here
input_str = input("Enter a list separated with commas: ")
sub_lists = make_sublist(input_str)

# This should be the last statement in your main program/function 
print(sorted(sub_lists))
