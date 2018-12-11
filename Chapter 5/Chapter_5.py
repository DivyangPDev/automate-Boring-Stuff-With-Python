#! /usr/bin/env python3

#Practise Questions

# 1. What does the code for an empty dictionary look like?
# dict = {}

# 2. What does a dictionary value with a key 'foo' and a value 42 look like?
# {'foo':42}

#3. What is the main difference between a dictionary and a list?
# dictionary are unordered objects and list are ordered objectsself. List is mutable sequence and dictionary is immutable sequenceself.

# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
#It will throw KeyError Exception

# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# It would return true for both the expressions. Infact 'cat' in spam is a shorter version of writing 'cat' in spam.keys()

# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# The expression 'cat' in spam would return true while it would return false for 'cat' in spam.values()

# 7. What is a shortcut for the following code?
# if 'color' not in spam:
#     spam['color'] = 'black'
#
# spam.setdefault('color','black')

# 8. What module and function can be used to “pretty print” dictionary values?
# Below module and function can be used to "pretty print" dictionary values.
# module - pprint
# functions - pprint, pformat

# Practise Projects -

# Fantasy Game Inventory

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby','gold coin','dagger','ruby','ruby','dagger']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+ ' '+k)
        item_total += v
    print("Total number of items: " + str(item_total))

# List to Dictionary Function for Fantasy Game inventory

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}


def addToInventory(inventory, addedItems):
    items_total = 0
    displayInventory(inventory)

    print("Updating Inventory:")
    items_total = 0
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1

    displayInventory(inventory)

addToInventory(stuff,dragonLoot)
