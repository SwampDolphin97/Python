#!/usr/bin/python

#A dictionary is like an address book where you can find the address or contact details of the person only by knowing the name of the person. we associate keys(name) with values(details). key must be unique. 
#pairs of keys and values are specified in the dictionary by using d = {key1 : value1, key2 : value2}
#key-value pairs are seperated by a colon and the pairs are seperated themselves by commas and all this is enclosed in a pair of curly braces. 

address_book = {'karan' : 'karan@gmail.com', 'hello' : 'abc@gmail.com', 'world' : 'xyz@gmail.com'}
print 'karan\'s address is', address_book['karan']

#deleting a key value pair
del address_book['world']
print '\nThere are {} contacts in the address-book\n'.format(len(address_book))

for name, address in address_book.items() :
    print 'contact {} at {}'.format(name, address)
#adding a key value pair
address_book['sample'] = 'sample@mail.com'

if 'sample' in address_book :
    print "\nsample address is ", address_book['sample']

