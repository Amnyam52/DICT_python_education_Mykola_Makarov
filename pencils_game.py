import random


def get_pencil_count():
    while True:
        pencils = input("How many pencils would you like to use:\n")
        if not pencils.isdigit() or int(pencils) <= 0:
            print("The number of pencils should be numeric" if not pencils.isdigit() else "The number of pencils should be positive")
        else:
            return int(pencils)


def get_first_player(player1, player2):
    while True:
        first = input(f"Who will be the first ({player1}, {player2}):\n")
        if first not in {player1, player2}:
            print(f"Choose between '{player1}' and '{player2}'")
        else:
            return first


def bot_move(pencils_left):
    if pencils_left % 4 == 0:
        return 3
    elif pencils_left % 4 == 3:
        return 2
    elif pencils_left % 4 == 2:
        return 1
    else:
        return random.choice([1, 2, 3])


def get_player_move(pencils_left):
    while True:
        move = input()
        if not move.isdigit() or int(move) not in [1, 2, 3]:
            print("Possible values: '1', '2' or '3'")
        elif int(move) > pencils_left:
            print("Too many pencils were taken")
        else:
            return int(move)


def play_game():
    player1 = "Player"
    player2 = "Bot"

    pencils = get_pencil_count()
    first_player = get_first_player(player1, player2)
    current_player = first_player

    print("|" * pencils)

    while pencils > 0:
        print(f"{current_player}'s turn!")

        if current_player == player2:
            move = bot_move(pencils)
            print(move)
        else:
            move = get_player_move(pencils)

        pencils -= move
        if pencils > 0:
            print("|" * pencils)

        current_player = player1 if current_player == player2 else player2

    winner = player1 if current_player == player2 else player2
    print(f"{winner} won!")


play_game()
