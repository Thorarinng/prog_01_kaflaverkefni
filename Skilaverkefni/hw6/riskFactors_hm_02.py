import string

data_file = []
with open("riskFactors.csv", 'r') as df:
    for line in df:
        data_file.append(line.split(','))

def To_Compare(data_file, category):
    """Takes a list and a category and finds the Max/Min numbers and the states"""
    list_to_compare = []
    for i in range(1, len(data_file)):
        # print("Line: ", i, "Item: ", float(data_file[i][category].strip('%')))
        list_to_compare.append(float(data_file[i][category].strip('%')))

    MaxVal = max(list_to_compare)
    MinVal = min(list_to_compare)
    MaxIndex = list_to_compare.index(max(list_to_compare))+1
    MaxState = data_file[MaxIndex][0]
    MinIndex = list_to_compare.index(min(list_to_compare))+1
    MinState = data_file[MinIndex][0]

    return MinVal, MinState, MaxVal, MaxState





MinVal, MinState, MaxVal, MaxState = To_Compare(data_file,11)
print(MinVal, MinState, MaxVal, MaxState)
