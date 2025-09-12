# def count_dots(xyz):
#     count = 0 
#     for j in xyz :
#         if j == ".":
#             count += 1
#     return count

# print(count_dots("j.s.s.s.p."))


#Extra challenge

import datetime
def age_verfiy(age):
    current_year = datetime.date.today().year
    
    if age>1900 and age<current_year:
        return True
    else:
        return False

def Age_in_min():
    while True:
            try:
                
                birth_year = int(input("Enter your birth year : "))
                
                if age_verfiy(birth_year) == True:
                    
                    current_year = datetime.date.today().year
                    birth_year = birth_year-1 # Because this current year is still not completed
                    number_of_months = datetime.datetime.today().month 
                    number_of_months = number_of_months - 1 # Because this current month is still not completed
                    number_of_days = datetime.datetime.today().day
                    number_of_days = number_of_days - 1 # Because this current day is still not completed
                    number_of_hours = datetime.datetime.today().hour
                    number_of_hours = number_of_hours - 1 # Because this current hour is still not completed
                    number_of_minutes = datetime.datetime.today().minute
                    number_of_minutes = number_of_minutes-1 # because this current Minute is not completed 
                    
                    
                    
                    age_in_min = ((current_year - birth_year)* 365 * 24 * 60) + (number_of_months*30*24*60) + (number_of_days*24*60) + (number_of_hours*60) + number_of_minutes
                    return f"Your age in minutes is approximately {age_in_min:,} minutes ."
                    break
                else:
                    print("Invalid age. Please enter a valid age between 1900 and the current year.")
                    
            except ValueError:
                print("Invalid input. Please enter a number for the year.The digits must be 4 digits.")
                    
            
                
            
        
print(Age_in_min())
            