import random

def play_game(name):
    user_input = None
    game_choice = ["r","s","p"]
    comp_guess = random.choice(game_choice) 
    while True:
        user_input = input(f"{name.capitalize()}, enter the value 'r' rock, 's' scissor & 'p' paper 🎮: \n\n>").lower()
        if user_input not in ["r","s","p"]:
            continue
        else:
            break
    
    if user_input == comp_guess:
        print("😃 Tie game")
    else:
        check_result(user_input,comp_guess,name)
    
    play_again = input(f"\n{name.capitalize()},You wanna play again 'y' or 'n'?: ").lower()
    if play_again == 'y':
        return play_game(name)
    else:
        print("\nThank you for playing our game🙏🙏🙏")
    

def check_result(user,comp,name):
    if user == 's' and comp == 'p' or user == 'p' and comp == 'r' or user =='r' and comp=='s':
        print(f"\n{name.capitalize()}, you wins🎉")
        return

    print("\nthe computer wins 😎")
    
if __name__ == "__main__":
    import argparse

    parse = argparse.ArgumentParser(
        description="Please the name of the player"
    )
    parse.add_argument(
        '-n','--name', metavar="player name",
        required=True, help="Please yu have to enter the name of th player"
    )

    args = parse.parse_args()
    play_game(args.name)
