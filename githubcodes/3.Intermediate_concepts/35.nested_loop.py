n = int(input("Enter a row of a matrix: "))
m = int(input("Enter a number of coloumn: "))
arr=  []
for i in range(n):
    col = []
    for j in range(m):
        col.append(j)
    arr.append(col)


print(arr)