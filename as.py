def is_leap(year):
    leap = False
    a=year/4
    if a==True:   
       return leap
    else:
       print("False")

year = int(input())
is_leap(year)