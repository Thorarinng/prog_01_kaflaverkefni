# 10-5 Dot product

def input_vector(size):
    """Spyr um staerd fylkis og les inn tolur midad vid staerd"""
    vector = []
    for i in range(1,size+1):
        vector.append(element(i))
    return vector

def element(the_index):
    """spyr um tolur. Skilar float tolu ut"""
    element = float(input("Element no {}: ".format(the_index)))
    return element

def dot_product(vec1, vec2):
    """Reiknar dot product utfra fylkjum"""
    dot_prod = 0
    for index in range(len(vec1)):
        dot_prod += vec1[index] * vec2[index]
    return dot_prod

# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))