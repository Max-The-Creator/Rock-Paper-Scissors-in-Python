# Import the random module
import random

# Function to get the player's move
def get_player_move():
    # Get the player's move input
    move = input("Rock, paper, or scissors? ").strip().lower()
    # Loop until the player enters a valid move
    while move not in {"rock", "paper", "scissors"}:
        move = input("Your entry is invalid. You must pick from rock, paper, or scissors: ").strip().lower()
    # Return the player's move
    return move

# Function to get the computer's move
def get_computer_move():
    # Choose a random move for the computer
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner of the round
def determine_winner(player_move, computer_move):
    # If the player's move is the same as the computer's move, it's a tie
    if player_move == computer_move:
        return "tie"
    # Check for all the cases where the player wins
    elif player_move == "rock" and computer_move == "scissors":
        return "player"
    elif player_move == "paper" and computer_move == "rock":
        return "player"
    elif player_move == "scissors" and computer_move == "paper":
        return "player"
    # If none of the above conditions are met, the computer wins
    else:
        return "computer"

# Function to play a single round of the game
def play_round():
    # Get the player's move
    player_move = get_player_move()
    # Get the computer's move
    computer_move = get_computer_move()
    # Print both moves
    print(f"Player move: {player_move} Computer move: {computer_move}.")
    # Determine the winner of the round
    winner = determine_winner(player_move, computer_move)
    # Print the result of the round
    if winner == "tie":
        print("Tie!")
    else:
        print(f"{winner.capitalize()} wins!")
    # Return the winner of the round
    return winner

# Function to play the full game
def play_game():
    # Initialize scores for the player and computer
    player_score = 0
    computer_score = 0
    # Loop until one player has won two rounds
    while player_score < 2 and computer_score < 2:
        # Play a round
        winner = play_round()
        # Update the scores based on the winner of the round
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        # Print the current scores
        print(f"SCOREBOARD Player: {player_score}, Computer: {computer_score}")
    # Print the final result of the game
    if player_score > computer_score:
        print("You win!")
    else:
        print("You lost!")

# Call the play_game function to start the game
play_game()
