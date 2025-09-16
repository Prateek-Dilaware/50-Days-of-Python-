from age_calculate_in_min.Calculator import age_in_min, year_valid

def get_birth_year() -> int:
    while True:
        try :
            year = int(input("Enter your birth year : ")) 
            if year_valid(year) == True:
                return year
            else:
                print("Invalid year. Please enter a year between 1900 and the current year.")
        except ValueError:
            print("Invalid input. Please enter a number for the year.The digits must be 4 digits.") 
            
            
def main():
    # CLI entry point 
    birth_year = get_birth_year()
    total_minutes = age_in_min(birth_year)
    print(f"Your age in minutes is approximately {total_minutes:,} minutes.")
    

if __name__ == "__main__" :
    main()    


