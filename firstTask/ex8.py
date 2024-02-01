#Gussing Game
def gussGame():
    tar = 5
    user = int(input("Enter your guess number: "))

    if user < tar:
        print("Your guess is almost there")
    elif user>tar:
        print("your guess is higher")
    else:
        print("Your guess is correct!")

gussGame()