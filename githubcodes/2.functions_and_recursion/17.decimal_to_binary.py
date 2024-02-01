n = int(input("Enter a decimal number:"))

binary = []
def decimal_to_binary(n):
    while n != 0:
        binary.append(n%2)
        n = n//2
     


decimal_to_binary(n)
print(binary)
