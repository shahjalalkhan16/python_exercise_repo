n = int(input("Enter a number that you want to check prime:  "))

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 3 or n == 3:
        return True
    
    for i in range(2,n):
        if n % i == 0:
            return False
          
        
    return True
        

print(is_prime(n))