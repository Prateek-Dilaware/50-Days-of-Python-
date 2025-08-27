# def only_float(a,b):
#     if type(a)== float and type(b)== float:
#         return 2 
#     elif type(a) == float or type(b)== float :
#         return 1
#     else :
#         return 0 

# print(only_float(2.4,5.34))

# Another way 

def only_float2(a=1,b=2): # just setting  the default values if there are no arguments or one argument
    if isinstance(a,float) and isinstance(b,float):
        return 2 
    elif isinstance(a, float) or isinstance(b,float) :
        return 1
    else :
        return 0 

print(only_float2("q","wjenk"))
print(only_float2(3.4,5.34))


# Extra question 
print("$$$$$$$$$$$$$$$$$$$$$$$$")
print()
print("Extra question solution :- ")


def word_index(lst):
    if not lst : # Means empty list 
        print("List is empty")
        return -1
    if len(lst) == 1:
        print("List has only one element")
        return 0
    checker = len(lst[0])
    longest_index = 0
    for j in range(len(lst)) :
        if len(lst[j]) > len(lst[longest_index]):
            longest_index = j 
        else : 
            continue
        
    if checker == len(lst[longest_index]):
        print("The lenghth of all elements of the list is same")
        return 0
    else :
        print("The longest word is at index",longest_index)
        return longest_index

l1 = ["abvc","abc","abcd","abcde"]
l2 = ["abc","bcd","cde","efg","hij","klm","nop"]
print(word_index(l1))
print(word_index(l2))

        