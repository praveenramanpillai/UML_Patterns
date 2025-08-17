def prime_checker(n):
    # checks number less than or equals to 1
    if n<=1:
        return False
    # number 2 is a only Prime Even number
    if n==2:
        return True
    # eliminates all even numbers
    if n%2==0:
        return False
    # checks other numbers for prime
    for i in range(3, int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

# User input and calculates output
try:
    n=int(input("Enter a number to check if it is Prime: "))
    if prime_checker(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

except ValueError:
    print("Invalid input! Please enter a valid integer")