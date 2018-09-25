# 10-5

    # Input vector size: 3
    # Element no 1: 1
    # Element no 2: 3.0
    # Element no 3: -5
    # Element no 1: 4
    # Element no 2: -2.0
    # Element no 3: -1
    # Dot product is:  3.0

# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))