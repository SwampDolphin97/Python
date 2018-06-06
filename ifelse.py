#!/usr/bin/python
number = 23;
guess = int(input('Enter an integer : '))
if guess == number :
    #new block starts here
    print('Congratulations! you guessed it right.')
    print('but you do not win any prize :-/')
elif guess < number :
    #another block
    print('No, it is a little higher than that')
else :
    print('No, it is a little lower than that')
print('Done')

