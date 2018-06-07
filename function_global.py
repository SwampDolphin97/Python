#!/usr/bin/python

#If a value has to be assigned outside any kind of scope such as a function or a class, then we have to tell python that the name is not local. We have to use the global keyword.

x=50
def func() :
    global x
    print 'x is', x
    x=2
    print 'changed global x to', x

func()
print 'value of x is', x

