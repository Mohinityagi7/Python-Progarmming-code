# String
# collection of charecters inside single quotes or double quotes
from distutils.log import error


first_name = "Mohini"
last_name = "Tyagi"
full_name = first_name + " " + last_name
print(full_name)
# print(first_name + 3) #error
# print(first_name + "3") #no error
print(first_name +str(3)) # no error
print(first_name * 3)