n = int(input("Enter a number: "))

# for i in n:
#     sum = sum +i


def sum_of_digits(n):
    sums = 0
    while n != 0:
        sums = sums + n%10
        n = n//10
    return sums


result = sum_of_digits(n)

print(result)