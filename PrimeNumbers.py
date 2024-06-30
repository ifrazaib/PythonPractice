def is_prime(num):
    if num <= 1: # 1 is not a prime number
        print("Not a prime number")
        return
    for i in range(2, num): # loop to check range
        if num % i == 0: # check condition if divided then prime
            print("Not a prime number")
            return
    print("Prime number")


def print_primes_in_loop(num):
    if num <= 1:
        print("No prime numbers")
        return
    for n in range(2, num + 1): # outer loop 
        is_prime = True
        for i in range(2, n): # inner loop to check the outer loop number is prime or not
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(n, end=" ")


num = int(input("Enter a number: "))
is_prime(num) # function calling
print("Prime numbers in a loop:")
print_primes_in_loop(num)
