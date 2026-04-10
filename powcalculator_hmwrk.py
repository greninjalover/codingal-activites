base_number = int(input("Which number would you like to multiply? "))
how_many_powers = int(input("How many powers do you want to see? "))

print("Calculating...")

if how_many_powers>100:
    print("Wow HUGE number dude!")

for power in range(1, how_many_powers + 1):
    result = base_number ** power
    print(base_number, "to the power of", power, "is", result)
