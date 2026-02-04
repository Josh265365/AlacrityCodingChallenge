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

#cathching invalid inputs using try and except block
def get_valid_integer(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print(f"Invalid input '{user_input}'. Please enter a whole number.")
            

            
#------Main Program------
def main():
    pass


print("----------------------------------------------------")
print ("Welcome to the prime number checker!")
print("----------------------------------------------------")


while True:
    
    print ("please select an option:")
    print ("1. Check if a number is prime")
    print ("2. Exit")
    
    option = input("Enter your choice (1 or 2): ")
    if option == '1':
        num = get_valid_integer("Enter a number: ")
            
        if is_prime(num):
            #If prime - output the string 'Prime!' 
            print("Prime!")
        else:
                #If not prime, output factors 
            factors = get_factor(num)
            print(f"{num} is not prime.")
            print(f"Factors: {factors}")
    
    elif option == '2':
        print("Exiting the program. Goodbye!")
        break
        
        
        
    




