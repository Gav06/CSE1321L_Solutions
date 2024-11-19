
def sortByString(strings):
    for _ in range(len(strings)):
        for j in range(len(strings) - 1):
            if len(strings[j]) < len(strings[j + 1]):
                temp = strings[j + 1]
                strings[j + 1] = strings[j]
                strings[j] = temp

def print_list(strings):
    t = ""
    for s in strings:
        t += s + ", "
    print(t)

print("[String List Sorting]")
amount_of_names = int(input("How many names do you want to sort? "))

names = []

for i in range(amount_of_names):
    names.append(input(f"Please enter Name {i + 1}: "))

print("Now sorting...")

sortByString(names)

print("Sorted!")

print_list(names)