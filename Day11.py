def equal_str(a,b):
    set1 = set() # creating empty set because '{}' creates an emty dictionary
    set2 = set() 
    if len(a)== len(b):
        for i,j in zip(a,b):
            set1.add(i) 
            set2.add(j)
            if set1 == set2:    
                return True
    else:
        return False
    
print(equal_str("abc","cab"))
print(equal_str("harsh","arhsh"))


# Extra questions

def swap(lst):
    var = lst[0]
    lst[0] = lst[-1]
    lst[-1] = var
    return lst

print(swap([1,2,3,4,5]))





