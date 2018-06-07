#!/usr/bin/python

# Default argument values
#for some functions, we want to make some parameters optional and use default values in the case if user does not want to provide values for them. This is done with the help of default argument values. 

def say(message, times=1):
    print message * times
say('Hello')
say('World', 5)
