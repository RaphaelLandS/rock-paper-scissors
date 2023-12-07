import random


def play():
    # Storing points outside the while loop, so it doesn't get reset.
    player_points = 0
    enemy_points = 0
    # Storing the winner variable to break the game while loop.
    winner = False
    # Rounds
    rounds_number = 0
    valid_rounds_input = False
    while not valid_rounds_input:
        rounds_input = input("Choose how many rounds"
                             "\n(1 = Best of 3)"
                             "\n(2 = Best of 5)"
                             "\n(3 = Best of 10)"
                             "\n>")
        if rounds_input == '1':
            valid_rounds_input = True
            rounds_number = 3
            break
        elif rounds_input == '2':
            valid_rounds_input = True
            rounds_number = 5
            break
        elif rounds_input == '3':
            valid_rounds_input = True
            rounds_number = 10
            break
        else:
            print("Invalid option, try again.")
            valid_rounds_input = False

    while not winner:
        # Enemy moves
        possible_enemy_moves = ("Rock", "Paper", "Scissors")
        enemy_move = possible_enemy_moves[random.randrange(0, 3)]

        # Player moves
        player_move = ''
        valid_move_input = False
        while not valid_move_input:
            moves_input = input("Make your move"
                                "\n(1 = Rock)"
                                "\n(2 = Paper)"
                                "\n(3 = Scissors)"
                                "\n>")
            if moves_input == '1':
                valid_move_input = True
                player_move = 'Rock'
                break
            elif moves_input == '2':
                valid_move_input = True
                player_move = 'Paper'
                break
            elif moves_input == '3':
                valid_move_input = True
                player_move = 'Scissors'
                break
            else:
                print("Invalid option, try again.")
                valid_move_input = False

        # Player vs Enemy
        # Draw
        if player_move == enemy_move:
            print("Draw, try again.")
        # Player point
        if player_move == 'Paper' and enemy_move == 'Rock':
            print("You made a point!")
            player_points = player_points + 1
        elif player_move == 'Scissors' and enemy_move == 'Paper':
            print("You made a point!")
            player_points = player_points + 1
        elif player_move == 'Rock' and enemy_move == 'Scissors':
            print("You made a point!")
            player_points = player_points + 1
        # Enemy point
        if player_move == 'Scissors' and enemy_move == 'Rock':
            print("The enemy made a point...")
            enemy_points = enemy_points + 1
        elif player_move == 'Rock' and enemy_move == 'Paper':
            print("The enemy made a point...")
            enemy_points = enemy_points + 1
        elif player_move == 'Paper' and enemy_move == 'Scissors':
            print("The enemy made a point...")
            enemy_points = enemy_points + 1

        # Player message
        print(f"You chose {player_move} and the enemy chose {enemy_move}."
              f"\nYou have {player_points} point(s)."
              f"\nThe enemy has {enemy_points} point(s).")

        # Winning conditions
        if rounds_number == 3:
            if player_points == 2:
                print("You won!")
                winner = True
            elif enemy_points == 2:
                print("The enemy won...")
                winner = True
            else:
                continue
        if rounds_number == 5:
            if player_points == 3:
                print("You won!")
                winner = True
            elif enemy_points == 3:
                print("The enemy won...")
                winner = True
            else:
                continue
        if rounds_number == 10:
            if player_points == 6:
                print("You won!")
                winner = True
            elif enemy_points == 6:
                print("The enemy won...")
                winner = True
            else:
                continue


if __name__ == "__main__":
    play()