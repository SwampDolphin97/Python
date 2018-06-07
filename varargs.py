#!/usr/bin/python

#sometimes we want to define a function that can take any number of parameters i.e. variable number of arguments, this can be achieved by using the stars

def total(a=5, *numbers, **phonebook):
    print 'a', a
#iterate through all the items in tuple
for single_item in numbers:
    print 'single_item',single_item
#iterate through all the items in dictionary
for first_part, second_part in phonebook.items():
    print (first_part, second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

#when we declare a starred parameter such as *param, then all the positional arguments from that point till the end are collected as a tuple called 'param'.
#when we declare a double starred parameter such as **param, then all the keywords arguments from that point till the end are collected as a dictionary
