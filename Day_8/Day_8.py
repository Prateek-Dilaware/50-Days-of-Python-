def odd_even(lst):
    small_odd = float('inf') #Start with the largest possible value

     
    large_even = float('-inf') #Start with the smallest possible value
    for j in lst:
        if j == 0:
            if large_even < j:
                large_even = j
        elif j % 2 == 0:
            if large_even < j:
                large_even = j
        elif j%2 ==1:
            if small_odd > j:
                small_odd = j
                
    return  (large_even - small_odd)
                
                
l1 = [1,2,4,6,-33,68,-5]
print(odd_even(l1))




# Extra questions 