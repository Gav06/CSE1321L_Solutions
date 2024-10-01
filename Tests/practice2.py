# another practice problem for the midterm
"""
-create method for calculations
-method for handling input


1st question
-user input
-print 4 rows
-create tree of "x"'s and dashes

2nd question
-user input a set of numbers (any length)
-program checks if list exceeds a certain length of numbers
-check if any numbers are greater than 9
-check for duplicate numbers
-check for non-numbers
-looping

3rd question
-prompt user for number
-print numbers from 1 to user's number
-next to each number it will say if it is a multiple of the user's number
-also print next to each number if it is prime

example:

user number: 25

1 2 3<-(prime) 4 5 <-(multiple, prime) 6 7<-(prime) 8 9 10 11<-(prime) 12 13<-(prime) 14 15 16 17<-(prime) 18 19<-(prime) 20 21 22 23<-(prime) 24 25

"""

# problem 3 attempt:



def is_prime(num):
    if num <= 1:
        return False

    flag = False
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    return not flag

def is_factor(potential_factor, num):
    return (num % potential_factor) == 0


user_num = int(input("Please enter an integer: "))

for i in range(1, user_num + 1):
    prime = is_prime(i)
    factor = is_factor(i, user_num)

    line = str(i)

    if prime:
        line += " (prime)"
    if factor:
        line += " (factor)"

    line += ", "
    print(line, end="")
