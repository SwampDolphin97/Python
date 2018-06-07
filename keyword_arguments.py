#!/usr/bin/python
def func(a,b=5,c=10):
    print 'a is', a, 'and b is', b, 'and c is', c
func(3, 7)
func(25, c=24)
func(c=50,a=100)
#if we have some functions with many parameteres and we want to specify only some of them, then we can give values for such parameters by naming them - this is called keyword arguments
