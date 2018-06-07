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

#Break statement is used to break out of a loop statement. or to stop the execution of the current looping instruction.
#while True :
#s = input('Enter Something : ')
#if s == 'quit' :
#   break;
#printf('Length of the string is', len(s))
#printf('Done')
