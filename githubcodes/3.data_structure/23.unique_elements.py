list1 = [2,3,4,5,2,2,7,7,8,8,9]

unique_list = []

print(list1)

for i in list1:
    if i not in unique_list:
        unique_list.append(i)


print(unique_list)