## Implement a program to print out the first 100 prime numbers
# Brett Shearer
# CSCI 102 - Section B
# Git Workshop Week 2


# Function for determining whether a number is prime
def is_prime(number):
    for val in range (2, number - 1):
        if number % val == 0:
            return False
            break
    return True


# program for counting to/listing up to the 100th prime number
count = 0
i = 2
while count < 100:
    if is_prime(i) == True:
        print(i)
        i += 1
        count += 1
    else:
        i += 1
