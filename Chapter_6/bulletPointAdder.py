#! /usr/bin/env python3

#bulletPointAdder.py - Adds Wikipedia bullet points to the start
#of each line of text on the clipboard

import pyperclip as pyclip

#Before producing the bullet point list the text is --
pyclip.copy('''Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars''')

text = pyclip.paste()

lines = text.split("\n")
for i in range(len(lines)):    #loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] #add star to each string in "lines" list

pyclip.copy("\n".join(lines))

print(pyclip.paste())
