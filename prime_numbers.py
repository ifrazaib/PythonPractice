class PrimeNumber:
    """class to check whether a number is prime and to find prime numbers in a range"""

    def prime_numbers_check(self, num):
        """check whether a given number is prime or not"""
        if num == 1:  # as 1 is not a prime number
            print("Number is not a Prime")
        elif num > 1:
            flag = False
            for i in range(2, num):  # loop to check if the given number is prime
                if num % i == 0:
                    flag = True
                    break
            if flag:  # if flag is True, then it is not a prime number
                print("Number is not a Prime Number")
            else:  # if flag is False, then it is a prime number
                print("Number is a Prime Number")
        else:
            print("Wrong input")

    def prime_by_loop(self, start, end):
        """check and print prime numbers in a given range"""
        for num in range(start, end + 1):
            if num > 1:
                is_prime = True
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(num, end=" ")


num = int(input("Enter a number to check either prime or not : "))  # create an instance of PrimeNumber class
obj = PrimeNumber()
obj.prime_numbers_check(num)  # call the method to check if the number is prime

start = int(input("Enter your start number to check in a range: "))
end = int(input("Enter your end number to check a number in a range: "))
obj.prime_by_loop(start, end)  # call the method to print prime numbers in the given range
