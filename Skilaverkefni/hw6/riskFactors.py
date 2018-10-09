# Hlynur Magnus Magnusson
# hlynurm18@ru.is
# Skilaverkefni 06; riskFactors

import string

def GetFile():
    """Prompts for input and returns a file"""
    file_name = input("Enter filename containing csv data: ")
    return file_name

def GetData(fname):
    """Imports data from a file and returns a list"""
    try:
        data_file = []
        with open(fname, 'r') as df:
            for line in df:
                data_file.append(line.split(','))
    except FileNotFoundError:
        print("Cannot find file {}.".format(fname))
    return data_file

def To_Compare(data_file, category):
    """Takes a list and a category and finds the Max/Min numbers and the states"""
    list_to_compare = []
    for i in range(1, len(data_file)):
        list_to_compare.append(float(data_file[i][category].strip('%')))

    MaxVal = round(max(list_to_compare), 1)
    MinVal = round(min(list_to_compare), 1)
    MaxIndex = list_to_compare.index(max(list_to_compare))+1
    MaxState = data_file[MaxIndex][0]
    MinIndex = list_to_compare.index(min(list_to_compare))+1
    MinState = data_file[MinIndex][0]

    return MinVal, MinState, MaxVal, MaxState

def print_out_info(data_file):
    # 0     State
    # 1     Heart
    # 5     Motor
    # 7     Teen
    # 11    Adult Smoking
    # 13    Adult Obesity
    category_list = [1,5,7,11,13]

    for category in category_list:
        MinVal, MinState, MaxVal, MaxState = To_Compare(data_file, category)
        category_name = data_file[0][category]
        print_info(category_name, MinState, MinVal, MaxState, MaxVal)


def print_header():
    
    print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format("Indicator","Min", '','', "Max", ''))
    print('-' * 87)

def print_info(col_1, col_2, col_3, col_4, col_5):
    """Formats the printout"""
    print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format(col_1, col_2, col_3,'', col_4, col_5))

def main():
    """Run main program"""

    file_name = GetFile()
    stats_file = GetData(file_name)

    print_header()
    print_out_info(stats_file)

main()
