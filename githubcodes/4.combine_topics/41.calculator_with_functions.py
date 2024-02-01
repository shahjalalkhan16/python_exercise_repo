n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

def calculator(op):
    if op == "+":
        print("Sum of the numbers is: ", n1 + n2)
    if op == "-":
        print("Sum of the numbers is: ", n1 - n2)
    if op == "*":
        print("Multipication the numbers is: ", n1*n2)
    if op == "/":
        print("Division if the numbers is: ", n1/n2)


op = input("Enter your operator: ")

calculator(op)