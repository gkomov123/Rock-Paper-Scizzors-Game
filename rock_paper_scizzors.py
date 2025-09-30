from random import choice

# Winning moves dictionary
winning_moves = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
# Hello prints
print("""\
    ---------------------------------------------------------------------------------------------------------
                       Welcome to my Rock, Paper, Scissors game! 
    In this simple but fun game you pick rock paper or scissors and face off against the computer!
    ---------------------------------------------------------------------------------------------------------
      """)

# Counters
user_wins = 0
computer_wins = 0
draws = 0

while True:
    #Computer choice logic
    computer_move = choice(list(winning_moves.keys()))
    # User input
    user_move = input("\nChoose rock, paper or scissors: ").lower()

    # Invalid move case
    if user_move not in winning_moves:
        print("\nInvalid move - please type 'rock', 'paper' or 'scissors'")
        continue

    #Win,Draw and Lose Logic
    if user_move == computer_move:
        draws += 1
        print(f"It's a draw the computer chose: {computer_move}")
    elif winning_moves[user_move] == computer_move:
        user_wins += 1
        print(f"You won the computer chose: {computer_move}")
    else:
        computer_wins += 1
        print(f"You lost the computer chose: {computer_move}")
             
    # Keep playing logic
    keep_playing_input = input("\nDo you want to keep playing? y, n: ").lower()
    valid_input = ["y", "yes", "ye"]
    if keep_playing_input in valid_input:
        continue
    else:
        print("--------------------------------------------------------------" 
            "\nThank you, for playing my Game <3!"
            "\nFINAL SCORE:"
            f"\nComputer:{computer_wins}"
            f"\nHuman:{user_wins}"
            f"\nDraws:{draws}")
        break
