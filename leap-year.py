def leap_year(year):
    return True if year % 400 is 0 or (year % 100 is not 0 and year % 4 is 0) else False
