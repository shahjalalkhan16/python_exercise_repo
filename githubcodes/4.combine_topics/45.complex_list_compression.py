# complex_list = [['Robin', 5, "student"],['Mahi',9, 'employee']]

# print(complex_list[2][1])

my_list =[]
n = int(input("Enter number of elements that in the list: "))

## List Comprehension
comprehension_list  = [(i, i*i, i**3) for i in range(1, n+1)]
print(tuple(comprehension_list))


# for i in range(1, n+1):
#     my_list.append(i)


# print("Original list")
# print(my_list)

# square_of_list = [i*i for i in my_list]
# cube_of_list = [i**3 for i in my_list]
# print("Square of the list is")
# print(square_of_list)
# print("Cube of the list is")
# print(cube_of_list)

# print((tuple(my_list),tuple(square_of_list),tuple(cube_of_list)))
# newlist =[]
# for i in range(1, n+1):
#     newlist.append(i)

# for i in range(1, n+1):
#     newlist.append(i*i)

# for i in range(1, n+1):
#     newlist.append(i**3)

# print("List compreshion")
# print(tuple(newlist))

# ## List Comprehension
# comprehension_list  = [(i, i*i, i**3) for i in range(1, n+1)]
# print(tuple(comprehension_list))


