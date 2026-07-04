try:
    age=int(input("Enter Your Age"))
    if age>18:
        print("Elligible")
    else:
        print("You Are A Minor")

except ValueError as e:
    print(e)

