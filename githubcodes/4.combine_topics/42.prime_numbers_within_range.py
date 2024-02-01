n = int(input("Enter a range that you want to check: "))

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True
def prime_within_range(minValue, maxValue):
    for i in range(minValue, maxValue):
        if isPrime(i):
            print(i)

prime_within_range(1, n)