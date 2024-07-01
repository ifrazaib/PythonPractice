def is_prime(num):
    if num <= 1: 
        return False
        
    for div in range(2, num // 2 + 1): 
        if num % div == 0:
            return False
            
    return True


def print_primes_in_loop(num):
    for n in range(2, num + 1): 
       if not is_prime(n):  
           continue
           
       print(n, end=" ")


num = int(input("Enter a number: "))
is_prime_check = is_prime(num)  
if is_prime_check:
    print(f"{num} is a Prime Number")
    
else:
    print(f"{num} is Not a Prime Number")
print_primes_in_loop(num)
