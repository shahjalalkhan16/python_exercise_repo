input  = str(input("Enter a string that you want to check: "))

def is_palindrome(input):
    if len(input) <= 1:
        return True
    if input[0] == input[-1]:
        return is_palindrome(input[1:-1])
    
    return False
    

print(is_palindrome(input))