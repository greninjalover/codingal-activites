my_number = input("Enter a number to count its digits: ")

clean_number = my_number.replace("-", "")

digit_count = len(clean_number)

print("That number has " + str(digit_count) + " digits!")


if digit_count > 10:
    print("Whoa! That is a massive number!")
    print("Teach me your ways, master. MWAHAHAHAHA!")

print("Now that i have solved your problem solve my problem.")

ranquest= int(input("What is 1 + 1 equal to?"))

if ranquest is 2:
    print("Correct! Thank you for solving my problem.")

else:
    print("Wrong! You will have to restart.")
