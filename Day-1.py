# Day -1 


# def divide_or_square(X):
#     if X%5 == 0:
#         return X**0.5
#     else:
#         X%5
    
# print(divide_or_square(10))


# Using maths function 
import math

def divide_or_square(X):
    if X%5 == 0:
        return math.sqrt(X)
    else:
        return X
    
print(divide_or_square(10))


def longest_value(dict):
    longest = "" 
    for value in dict.values():
        if len(longest) < len(value):
            longest = value 
    return longest 


d1 = {"key1": "ABC", "key2": "XYZabc", "key3": "val"}
if longest_value(d1) == "XYZabc":
    print("Success")
else:
    print("Fail")