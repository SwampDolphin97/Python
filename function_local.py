#!/usr/bin/python

#when variables are declared inside a function definition, they are not related to the variables which are declared outside the function with the same names, i.e. variable names are local to function. This is called the scope of the variables. 

x=50;
def func(x) :
    print 'x is ', x
    x=2
    print 'changed local x to ', x

func(x)
print 'x is still ', x 


    
