import random
game_count = 0
player_wins = 0
percentage_win = 0

def play_game(name):
    computer_guess = random.choice([1,2,3,4,5])
    global game_count
    global player_wins
    game_count += 1

    while True:
        guess = input(f"{name.capitalize()}, guess which number I'm thinking of....1,2,3,4 or 5.\n> ")
        print("")
        if int(guess) in range(1,6):
            break
        else:
            print(f"{name}, please enter 1,2,3,4 or 5.")
    
    if int(guess) == computer_guess:
        player_wins += 1
        print(f"{name.capitalize()}, you chose {guess}")
        print(f"I was thinking about the number {computer_guess} \n")
        print(f"🎉🎉{name}, you win!\n")
        print(f"Game count: {game_count}\n")
        print(f"{name}'s wins: {player_wins}\n")
        print(f"Your winning percentage: {player_wins/game_count:.2%}\n")
    else:
        print(f"{name.capitalize()}, you chose {guess}")
        print(f"I was thinking about the number {computer_guess} \n")
        print(f"Sorry, {name.capitalize()}. Better luck next time. 😢\n")
        print(f"Game count: {game_count}\n")
        print(f"{name}'s wins: {player_wins}\n")
        print(f"Your winning percentage: {player_wins/game_count:.2%}\n")
        

    play_again = input(f"Play again, {name}?\n 'y' for Yes or \n 'q' to Quit\n> ").lower()
    if play_again == 'y':
        return play_game(name)
    else:
        print("👋 thank you for playing!")
    

if __name__ == "__main__":
    import argparse

    parse = argparse.ArgumentParser(
        description="Provide the player name."
    )

    parse.add_argument(
        "-n","--name",metavar="name",
        required=True, help="Please you have to enter the player name!"
    )
    args = parse.parse_args()
    play_game(args.name)