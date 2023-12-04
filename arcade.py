from guess_number import play_game
from rps import play_game as play_rps

arcade_count = 0
def arcade_program(name):
    global arcade_count
    arcade_count += 1
    while True:
        try:
            game_to_play = input(f"\n{name.capitalize()}, {'welcome back to arcade menu' if arcade_count > 1 else 'welcome to the Arcade! 🤖'} \n\nplease choose a game:\n\n1 = Rock Paper Scissors\n2 = Guess My Number \n\nOr press \"X\" to exit the Arcade \n> ").lower()
            if game_to_play == 'x':
                print(f"\n{name.capitalize()}, Bye 👋❗")
                break
            elif int(game_to_play) == 2:
                play_game(name)
                arcade_count += 1
            elif int(game_to_play) == 1:
                play_rps(name)
                arcade_count+=1
            else:
                print(f"\n{name.capitalize()}, please enter the correct value!")
        except ValueError:
                print(f"\n{name.capitalize()}, please enter the correct value! 1,2 or x")


        
    

if __name__ == '__main__':
    import argparse

    parse = argparse.ArgumentParser(
        description="Please type the name of the player"
    )

    parse.add_argument(
        '-n',"--name", metavar="name",
        required=True, help="You have to enter the -n flag and the player name value"
    )

    args = parse.parse_args()
    arcade_program(args.name)
