#!/usr/bin/python
#this is the python file for the tuples data structures
#tuples are used to hold together multiple objects. tuples cannot be modified and hence are immutable. tuples are defined by specifying items seperated by commas within an optional pair of parentheses.

zoo = ('python', 'elephant', 'penguin')
print 'Number of animals in the zoo is', len(zoo)

new_zoo = ('monkey', 'camel', zoo)
print 'Number of cages in the new zoo is', len(new_zoo)
print 'All animals in new zoo are', new_zoo
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animal bought from the old zoo is', new_zoo[2][2]
print 'Number of animals in the new zoo is', len(new_zoo)-1+len(zoo)

