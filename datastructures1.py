#!/usr/bin/python

#there are 4 built-in data structures in python.
#list, tuples, dictionary and set.

#this is the list program.
#list is a data structure that holds an ordered collection of items i.e. you can store a sequence of items in a list. This is similar to the shopping list that contains the list of the items that we have to buy. we put commas between each item in a list. The list should be enclosed between a square brackets so that python knows that we are specifying a list. Once the list is created, we can add, remove and search for items in a single list. This is a mutable data type.

#this is my sample shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print 'I have', len(shoplist), 'items to purchase'
#end=' ' is used to list all the items of the list
for items in shoplist:
    print items

print '\nI also have to buy rice.'
shoplist.append('rice')
print('My shopping list is now', shoplist)

print 'I have to sort my list now'
shoplist.sort()
print 'sorted shopping list is', shoplist

print 'The first item I have to buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shoppig list is now', shoplist
