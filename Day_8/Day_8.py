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


# another way of solving this problem
def od_ev(l):
    odd = []
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return max(even) - min(odd)



# Extra questions 
def prime_number(num):
    prime = []
    for j in range(2,num):
        if j>1:
            is_prime = True
            for k in range(2,j):
                if j % k == 0:
                 is_prime = False
                
        if is_prime==True:
            prime.append(j)
            
    return prime


print(prime_number(100))