"""
Class:      CSE1321L
Section:    Module 7
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        13
"""

input_str = input("Enter temperatures for each day separated by space: ").split()
temps = []
for s in input_str:
    temps.append(int(s))

# Find streaks
longest_cold_streak = 0
heat_waves = 0

current_cold_streak = 0
current_heat_wave = 0

for temp in temps:
    if temp < 15:
        current_cold_streak += 1
    else:
        current_cold_streak = 0

    if current_cold_streak > longest_cold_streak:
        longest_cold_streak = current_cold_streak

    if temp > 30:
        current_heat_wave += 1
    else:
        if current_heat_wave >= 3:
            heat_waves += 1
        current_heat_wave = 0

# Account for end of loop, run checks one more time
if current_heat_wave >= 3:
    heat_waves += 1

if current_cold_streak > longest_cold_streak:
    longest_cold_streak = current_cold_streak

# this average doesn't match the output given in the assignment sheet
# for whatever reason
avg = round(sum(temps) / len(temps), 2)

print(f"Number of heat waves: {heat_waves}")
print(f"Longest cold streak: {longest_cold_streak} days")
print(f"Average temperature: {avg}°C")