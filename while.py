#!/usr/bin/python
number = 23
running = True
while running :
    userinput = int(input('Enter an integer : '))
    if userinput == number :
        print('Congratulations, You guessed it right :D')
        running = False
    elif userinput < number :
        print('No, it is a little higher than that.')
    else :
        print('No, it is a little lower than that')
else :
    print('The while loop is over.')
print('Done.')


