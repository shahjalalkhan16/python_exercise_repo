list1 = [1,2,3,5]
list2 = [3,4,5,5,6]

common_list = []
for i in list1:
    flag = 0
    for j in list2:
        if i == j:
            flag = 1
    if flag == 1:
        common_list.append(i)

print(common_list)

# another process
commonList = list(set(list1).intersection(set(list2)))
print(commonList)