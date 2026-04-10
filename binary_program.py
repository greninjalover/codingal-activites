print("--- Ramcharan's Super Cool Number System ---")

number = int(input("Enter a number: "))
original_number = number
binary_result = ""

if number == 0:
    binary_result = "0"
else:
    while number > 0:
        remainder = number % 2
        binary_result = str(remainder) + binary_result
        number = number // 2


print("------------------------------")
print("Decimal Number:", original_number)
print("Binary Number: ", binary_result)
print("------------------------------")
print("Have a Wondrous Day Companion")

input("Press Enter to exit")

