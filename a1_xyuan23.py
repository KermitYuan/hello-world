#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_xyuan23.py (replace [Seneca_name] with your Seneca User name)
Author: "Kermit Yuan"
The python code in this file (a1_xyuan23.py) is original work written by
"Kermit Yuan". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    '''
    This function will check if it is a leap year or not of obj
    '''
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                status = True
            else:
               status = False
        else:
                status = True
    else:
            status = False
    
    return status

def sanitize(obj1,obj2):
    '''
    check each character of obj1 if it exist in obj2, if it exist, add it to status string and return.
    '''
    results = ""
    for char in obj1:
            if char in obj2:
                results += char 
    return results

def size_check(obj, intobj):
    '''
    check the size/len of obj if it's the same as intobj, if same return ture if not return false
    '''
    status = False
    if len(obj) == intobj:
        status = True

    return status

def range_check(obj1, obj2):
    '''
    check obj1 is in the value range of obj2 or not, if it is return ture if not return false
    '''
    status = False

    if int(obj1) in range(obj2[0],obj2[1]+1):
     status = True
    
    return status
    
def usage():    
    '''
    display the usuage of the script
    '''
    status = """Usage: %s YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD""" % os.path.basename(__file__)

    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)  
