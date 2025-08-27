# def user_name(user_input):
#     name = ""
#     for j in user_input:
#               if j == "@":
#                   break 
#               else:
#                   name = name + j 
#     return name 
   
# print(user_name(input("Enter your email address: ")))


# Another way - 
def user_name(user_input):
    name = user_input.split("@")[0]
    return name

print(user_name(input("Enter your email address: ")))
# Extra question 

def zeroed(lst):
    lst[0] = 0
    lst[-1] = 0
    return lst

l1 = [1,2,3,4,5]
print(zeroed(l1))

