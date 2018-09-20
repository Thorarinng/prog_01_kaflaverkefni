# 9-2

    # Write a function named is_float(s) that takes one argument that is a string.  
    # It returns True if string s represents a floating point value and returns False otherwise.  
    # You are required to use try-except.  The basic concept is to "try" to 
    # convert string s to a float and if it succeeds, return True, but if it fails 
    # (that is, an exception is raised), return False.  
    # Note that float() raises a  ValueError exception.

# is_float function definition goes here
def is_float(s):
    """Change string to float"""
    try:
        my_float = float(s)
        return True
    except ValueError:
        return False


# Do not change the lines below
print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))