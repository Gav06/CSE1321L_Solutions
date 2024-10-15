"""
Gavin Conley
9/24/2024
cse1321L midterm
question a
"""

def print_pyramid(n):
    # calculate the maximum width we are going to need
    width = 0
    for i in range(n):
        if width == 0:
            width = 1
            continue

        # each layer of the pyramid will be 1 character wider on each side (total of 2)
        width += 2

    curr_width = 0
    for row in range(n):
        if curr_width == 0:
            curr_width = 1
        else:
            curr_width += 2
        line = ""

        # the amount of blank spaces for the leading and lagging side
        white_space = (width - curr_width) // 2
        for col in range(white_space):
            line += "-"
        for col in range(curr_width):
            line += "x"
        for col in range(white_space):
            line += "-"

        print(line)


def __main__():
    valid_size = False
    while not valid_size:
        size = int(input("Enter size: "))
        if size < 1 or size > 26:
            valid_size = False
            print("Invalid size")
        else:
            valid_size = True
            print_pyramid(size)


if __name__ == "__main__":
    __main__()
