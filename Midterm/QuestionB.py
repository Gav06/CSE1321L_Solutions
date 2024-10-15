"""
Gavin Conley
9/24/2024
cse1321L midterm
question b
"""

# checks sudoku row for validity
def is_valid_row(row):
    list = row.split()

    # check length
    if len(list) != 9:
        return f"Row has invalid length: {len(list)}"

    # check each digit is within the range of 1 to 9
    for i in range(len(list)):
        if (not str.isnumeric(list[i])) or (int(list[i]) > 9 or (int(list[i]) < 1)):
            return f"Row has invalid numbers: {list[i]}"

    # check for repeats
    cache = []
    for i in range(len(list)):
        num = int(list[i])

        for n in range(len(cache)):
            cached_num = cache[n]
            if num == cached_num:
                return f"Row contains duplicates: {num}"
        cache.append(num)

    return "Row is valid."


def __main__():
    row = input("Enter row (e.g. 1 3 2): ")
    print(is_valid_row(row))


if __name__ == "__main__":
    __main__()

