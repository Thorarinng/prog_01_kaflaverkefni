# 10-5

def input_vector(size):
    vec=[]
    for i in range(1,size+1):
        ele=float(input("Element no "+ str(i) + ": "))
        vec.append(ele)
    return vec

def dot_product(vec1, vec2):
    dot_prod = 0
    for j in range(0,len(vec1)):
        dot_prod += vec1[j] * vec2[j]
    return dot_prod
    
# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))


#     # Input vector size: 3
#     # Element no 1: 1
#     # Element no 2: 3.0
#     # Element no 3: -5
#     # Element no 1: 4
#     # Element no 2: -2.0
#     # Element no 3: -1
#     # Dot product is:  3.0


# def input_vector(size):
#     """Spyr um staerd fylkis og les inn tolur midad vid staerd"""
#     vector = []
#     for i in range(size):
#         vector.append(element(i))
#     return vector

# def element(the_index):
#     """spyr um tolur"""
#     element = float(input("Element no {}: ".format(the_index)))
#     return element

# # def dot_product(vec1, vec2):
# #     for i in vec1:
# #         print('i', i, 'vec2[i]', vec2[i])
# #     #     bla = i * vec2[i]
# #     return print("buid")

# def dot_product(vec1, vec2):
#     dot_prod = 0
#     for j in range(0,len(vec1)):
#         dot_prod += vec1[j] * vec2[j]
#     return dot_prod

# # Main program starts here, DO NOT change
# size = int(input("Input vector size: "))
# vector1 = input_vector(size)
# vector2 = input_vector(size)
# print("Dot product is:", dot_product(vector1, vector2))