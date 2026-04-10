user_input = input("Type one letter, number, or symbol: ")

if type(user_input) is str and len(user_input) == 1:
    
    secret_number = ord(user_input)
    print("The ASCII secret number is:", secret_number)
    
    if 65 <= secret_number <= 90:
        print("Category: Uppercase Letter")
    elif 97 <= secret_number <= 122:
        print("Category: Lowercase Letter")
    elif 48 <= secret_number <= 57:
        print("Category: Digit (Number)")
    else:
        print("Category: Special Character")

else:
    print("Oops! Please enter exactly ONE character.")
    print("If you enter another 2 digit number again something BAD will happen so dont!")
