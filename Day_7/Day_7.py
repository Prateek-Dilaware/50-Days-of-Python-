def string_range(int):
    string = ""
    for a in range(int):
        string = string +str(a) +"."
        
    return string.strip(".")

print(string_range(5))


# Extra Challenge 

def Start_count(lst):
    # Use a dictionary to store the counts of names
    dic= {}
    
    # Iterate through the list of names
    for name in lst:
        # Check if the name starts with "s" (case-insensitive)
        if name.lower().startswith("s"):
            # Use the .get() method for a cleaner way to handle counting.
            # It gets the current count for 'name' or defaults to 0 if it's new.
            lower_name = name.lower()
            dic[lower_name] = dic.get(lower_name, 0) + 1
            
    return dic

l1 = ["Sarthak","Sohail","Vucy","swarnshi","Shivam","Vicky","Sohail","Sarthak","Shivam","sarThak"]
print(Start_count(l1))
            