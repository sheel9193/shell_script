def play_game():
    import random

    choices = ["rock", "paper", "scissors"]
    user_choice = input("rock, paper, or scissors?").lower()
    while user_choice not in choices:
        print("Invalid choice, choose again.")
        user_choice = input("rock, paper, or scissors?")
    
    computer_choice = random.choice(choices)
    print(f"You choose {user_choice}")
    print(f"Computer's choose's {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif(
        (user_choice == 'rock' and computer_choice == 'scissors')
        or (user_choice == 'paper' and computer_choice == 'rock') 
        or (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("User wins!")
    else:
        print("Computer wins!")
play_game()