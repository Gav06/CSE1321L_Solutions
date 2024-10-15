"""
Gavin Conley
9/24/2024
cse1321L midterm
question c
"""

# returns bool
def is_prime(n):
    if n <= 1:
        return False
    # find factors
    for i in range(2, n):
        if (n % i) == 0:
            return False
    # no factors found, must be prime
    return True


def custom_buzz(n, multiple1=7, multiple2=3):
    for num in range(1, n + 1):
        text = str(num) + " "

        # if multiple of multiple1
        if num % multiple1 == 0:
            text += "Foo"

        # if multiple of multiple2
        if num % multiple2 == 0:
            text += "Bar"

        # if prime
        if is_prime(num):
            text += "Prime"
        text += " "
        print(text)


def __main__():
    number = int(input("Enter a number: "))
    mul1 = int(input("Enter the first multiple: "))
    mul2 = int(input("Enter the second multiple: "))

    custom_buzz(number, multiple1=mul1, multiple2=mul2)


if __name__ == "__main__":
    __main__()

