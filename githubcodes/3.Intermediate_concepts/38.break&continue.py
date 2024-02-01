n = int(input("Enter a range of number: "))

for i in range(1, n+1):
    print("Here", i)
    if i == 2:
        continue
    print("Now",i)
    if i == 3:
        break
