def hid_pass():
    password = input("Enter your password: ")
    count = 0
    hid = ""
    for char in password :
        count = count + 1
    
    for j in range(count):
        hid = hid + "*"
    return f"Your password {hid} is {count} characters long"

print(hid_pass())





# Extra Challenge 

def thousand_seprator(lst):
    for k in range(len(lst)):
        lst[k] = "{:,}".format(lst[k])
        
    return lst

print(thousand_seprator([1238876,878787,984874847,98479849]))

# Another way of doing extra challenge 
def th_sep(lst):
    l = ["{:,}".format(x) for x in lst]
    return l

lst = [199239938,398398398,989379290908,28099873]
print(th_sep(lst))

    