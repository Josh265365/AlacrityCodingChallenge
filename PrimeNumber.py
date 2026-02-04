#num  = int(input("enter a prime number: "))

#First a function to get the factors of a number in a given range
def get_factor(number):
    factors = [] # Then i need to store the factors in a list 
    for i in range(1, number + 1): #Starting from 1 to include 1 as a factor and adding 1 to include the number itself (if a number is prime, it will only have 1 and itself as factors). 
        if number % i == 0:
            factors.append(i)
    return factors

#check if it is a prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1): #checking divisibility from 2 to the square root of the number
        if num % i == 0:
            return False
    return True


#------Main Program------
print("----------------------------------------------------")
print ("Welcome to the prime number checker!")
print("----------------------------------------------------")

#cathching invalid inputs using try and except block
#if a user inputs a string or a float value instead of an integer the program should ask for a valid integer instead of closing. 
while True:
    try:
        num = int(input("Enter a number to check if it is prime: "))
        
        if is_prime(num):
            print(f"{num} prime!")
        else:
            factors = get_factor(num)
            print(f"{num} is not a prime number. Its factors are: {factors}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    




