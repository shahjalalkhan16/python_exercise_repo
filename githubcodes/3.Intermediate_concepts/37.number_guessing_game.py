n = 10

while True:
    number = int(input("Enter your number that you guess!: "))
    if number == n:
        print("Your gessing number is correct!")
        break
    if number > n:
        print("try something smaller")
    if number < n:
        print("Try something bigger")