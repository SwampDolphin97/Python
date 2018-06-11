#!/usr/bin/python

#return statement is used to return from the function, i.e. break out of the function. we can return the value of the function as well.

def max(x, y) :
    if x > y :
        return x
    elif x == y :
        return 'The numbers are equal'
    else :
        return y
print(max(2, 3))
print(max(5, 8))
