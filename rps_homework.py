import random 

while True: 
    useract = input("Enter a choice (rock, paper, scissors): ") 
    possact = ["rock", "paper", "scissors"]
    comact = random.choice(possact)
    print(f"\nYou chose {useract}, computer chose {comact}.\n")  


    if useract == comact: 
        print(f"Both players selected {useract}. It's a tie!")
    elif useract == "rock":
        if comact == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif useract == "paper":
        if comact == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif useract == "scissors":
        if comact == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Play again? (yes/no): ")
    if play_again != "yes":
        break 