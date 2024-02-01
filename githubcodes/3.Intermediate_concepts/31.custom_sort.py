## Custom Sort: Write a program that sorts a list of tuples using Lambda.

myList = [("Abir", 3, 5), ("Rakin", 2, 1), ("Tamim", 8, 3)]
myList.sort(key= lambda pair: pair[1])

print(myList)