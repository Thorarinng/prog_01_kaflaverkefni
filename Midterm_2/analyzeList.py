# Skrifið Python forrit sem les inn lista L af pósitívum heiltölum (e. integers) og prentar út eftirfarandi upplýsingar:

# Listann L.
# Raðaða útgáfu af L.
# Raðaðan lista af einkvæmum (e. unique) prímtölum í L. 
# Min, max og meðaltal gilda í L.  Meðaltalið skal skrifa út með tveimur aukastöfum.
# Þið megið nota listaföll í útfærslunni en þið megið ekki nota neina import setningu.   Fallið is_prime() er gefið.

# Prenta þarf út villuskilaboð ef notandinn slær ekki eingöngu heiltölur inn í listann.  Sjá dæmi um inntak/úttak fyrir neðan.

# Write a Python program that takes a list L of positive integers as input and prints out the following information:

# The list L.
# The sorted version of L.
# A sorted list of the unique prime numbers in L.
# Minimum, maximum and average values in L.  The average value should be printed with two decimal places.
# You are allowed to use list functions, but you are not allowed to import any module.  The function is_prime() is given.

# You need to print out an error message if the user does not only input integers into the list.  See an example below.

# Dæmi um inntak/úttak - Example input/output:

# Enter integers separated with commas: 2,5,7,2,8,10,34,23,9,4,5
# Input list: [2, 5, 7, 2, 8, 10, 34, 23, 9, 4, 5]
# Sorted list:  [2, 2, 4, 5, 5, 7, 8, 9, 10, 23, 34]
# Prime list:  [2, 5, 7, 23]
# Min: 2, Max: 34, Average: 9.91
 

# Enter integers separated with commas: 1,2,b
# Incorrect input!


def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
        
def make_num_list(number_string):
    """Tekur inn input streng og skilar ut integer lista"""
    numList = []
    for each in number_string.split(','):
        numList.append(int(each))
    return numList

def Prime_List(number_list):
    prime_list = []
    for number in number_list:
        if is_prime(number) and number not in prime_list:
            prime_list.append(number)
        primesSorted = sorted(prime_list)
    return primesSorted

def Find_Average(number_list):
    total_sum = 0
    for number in number_list:
        total_sum += number
    average = float((total_sum)/len(number_list))
    return round(average, 2)


# The main program starts here
try:
    numbers_str = input("Enter integers separated with commas: ")
    original = make_num_list(numbers_str)
except ValueError:
    print("Incorrect input!")
    exit

# Utbua mismunandi lista
# original = make_num_list(numbers_str)
sortedList = sorted(original)
primes = Prime_List(original)
MinVal = min(original)
MaxVal = max(original)
Average = Find_Average(original)

print("Input list:", original)
print("Sorted list: ", sortedList)
print("Prime list: ", primes)
print("Min: {}, Max: {}, Average: {}".format(MinVal, MaxVal, Average))
