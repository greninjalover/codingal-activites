import random
rando=(random.randint(0,9))
print(rando)

while True:
    guess= (int(input("Guess A Number... NOW!!!!!")))
    if rando==guess:
        print("You Got That Right!")
        break
    elif rando<guess:
        print("Hotter")
    elif rando>guess:
        print("Colder")
    else:
        print("Try Again!")
        
 
