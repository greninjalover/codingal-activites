import random
rando=(random.randint(0,9))
print(rando)

while True:
    guess= (int(input("Guess A Number... NOW!!!!!")))
    if rando==guess:
        print("You Got That Right!")
        break
    else:
        print("Try Again!")
        

