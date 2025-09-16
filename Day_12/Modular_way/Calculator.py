import datetime as dt
def year_valid(year : int)->bool:
    '''Check of the year is valid'''
    current_year = dt.datetime.today().year
    if year < 1900 or year > current_year:
        return False
    else:
        return True
    
    
def age_in_min(birth_year : int) -> int :
        
        now = dt.datetime.today()
        years = now.year - birth_year - 1 # Because this current year is still not completed
        months = now.month - 1 # Because this current month is still not completed
        days = now.day - 1 # Because this current day is still not completed
        hours = now.hour - 1 # Because this current hour is still not completed
        minutes = now.minute - 1 # because this current Minute is not completed
                
        Total = years *365 *24*60 + months * 30 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes
        return Total
                
    
    