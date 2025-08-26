def register_check(DICT):
    
    count = 0 
    for j in DICT.values():
        if j== "yes":
            count += 1
        else :
            continue 
    return count

D1 = {"Amit":"yes","Sohal":"no","Rahul":"yes","Nikhil":"no","Rohan":"yes"}

print(register_check(D1))



# Extra challenge 

def only_lower(lst):
    emty_list = []
    for j in lst :
        if isinstance(j,str)  and j.islower() :
            emty_list.append(j)
        else :
            continue
    return emty_list


l1 = ["john","Jack","Harsh",'sohail','victus',"VICtor"]

print(only_lower(l1))