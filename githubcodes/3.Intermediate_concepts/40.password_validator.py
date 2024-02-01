password  = "Mypass1#"


def pass_validator(pas):
    sp_case = ["#","!","$","&","*"]

    if len(pas) < 6 or len(pas) > 20:
        return False
    
    lowerFlag = 0
    upperFlag = 0
    digitFlag = 0
    specialFlag = 0

    for letter in password:
        if letter.isdigit():
            digitFlag =1
        # print(f"here for {letter} value of {lowerFlag}")
        if letter.islower():
            lowerFlag =1
        if letter.isupper():
            upperFlag = 1
        if letter in sp_case:
            specialFlag =1
        
    if lowerFlag == 0 or upperFlag == 0 or digitFlag == 0 or specialFlag == 0:
        return False
    
    return True


if pass_validator(password) :
    print("Good password")
else:
    print("Bad Password")


    
    

