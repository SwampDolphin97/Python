#!/usr/bin/python

#every module has a name and statements in a module can find out the name of their module. When a module is imported, the code of the module gets executed. module can be called by using __name__ attribute of the module.

if __name__ == '__main__':
    print('this program is being run by itself')
else:
    print('I am being imported from another module')

