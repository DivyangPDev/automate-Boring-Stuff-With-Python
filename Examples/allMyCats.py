#Storing number of cats and cats names

catnames = []
while True:
    print("Enter the name of the cat"+str(len(catnames)+1)+" or enter nothing to quit: ")
    name = input()
    if name == '':
        break
    catnames += [name]
print("The cat names are: ")
for catname in catnames:
    print(" " + catname)
