import sys

output_file = open("Battleship.out", "a")
print("Battle of Ships Game \n")
print("Battle of Ships Game \n", file=output_file)

letters = "   A B C D E F G H I J"
column_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                  'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

board_p1 = [["-" for x in range(10)] for y in range(10)]
board_p2 = [["-" for a in range(10)] for b in range(10)]
try:
    txt_files = ["Player1.txt", "Player2.txt", "Player1.in", "Player2.in"]
    unreachable = [txt for txt in txt_files if txt not in sys.argv]
    if len(unreachable) == 1:
        raise IOError("IOError: input file {} is not reachable.".format(unreachable[0]))
    elif len(unreachable) > 1:
        raise IOError("IOError: input files {} are not reachable.".format(",".join(unreachable)))

    player1_hidden_board = []
    player2_hidden_board = []

    player1_input = open("Player1.txt", "r")
    player2_input = open("Player2.txt", "r")

    for line in player1_input:
        player1_hidden_board.append(line.strip("\n").split(";"))
    player1_input.close()

    for line in range(len(player1_hidden_board)):
        for item in range(len(player1_hidden_board[line])):
            if player1_hidden_board[line][item] == '':
                player1_hidden_board[line][item] = '-'

    for line in player2_input:
        player2_hidden_board.append(line.strip("\n").split(";"))
    player2_input.close()

    for line in range(len(player2_hidden_board)):
        for item in range(len(player2_hidden_board[line])):
            if player2_hidden_board[line][item] == '':
                player2_hidden_board[line][item] = '-'

    player1_move_file = open("Player1.in", "r")
    player2_move_file = open("Player2.in", "r")

    player1_move = [item.split(",") for item in player1_move_file.read().split(";")]
    player1_move.pop(-1)
    player2_move = [item.split(",") for item in player2_move_file.read().split(";")]
    player2_move.pop(-1)
    player1_move_file.close()
    player2_move_file.close()

except IOError as error:
    print(error)
    print(error, file=output_file)

else:
    def players_round(rounds):
        print("Round : {} \t\t\t\t\tGrid Size: 10x10 \n".format(rounds))
        print("Round : {} \t\t\t\t\tGrid Size: 10x10 \n".format(rounds), file=output_file)
        print("Player1’s Hidden Board \tPlayer2’s Hidden Board")
        print("Player1’s Hidden Board \tPlayer2’s Hidden Board", file=output_file)
        print(letters, "\t   ", letters)
        print(letters, "\t   ", letters, file=output_file)


    def print_grid(grid_p1, grid_p2):
        num = 1
        for line_1, line_2 in zip(grid_p1, grid_p2):
            if num != 10:
                print(num, "", " ".join(line_1), " \t", end="")
                print(num, "", " ".join(line_2))
                print(num, "", " ".join(line_1), " \t", end="", file=output_file)
                print(num, "", " ".join(line_2), file=output_file)
                num += 1
            else:
                print(num, " ".join(line_1), " \t", end="")
                print(num, " ".join(line_2), "\n")
                print(num, " ".join(line_1), " \t", end="", file=output_file)
                print(num, " ".join(line_2), "\n", file=output_file)


    def carrier(hidden_1, hidden_2):
        if "C" not in hidden_1:
            c_p1 = "X"
        else:
            c_p1 = "-"
        print("Carrier    \t{}\t\t\t\t".format(c_p1), end="")
        print("Carrier    \t{}\t\t\t\t".format(c_p1), end="", file=output_file)

        if "C" not in hidden_2:
            c_p2 = "X"
        else:
            c_p2 = "-"
        print("Carrier   \t{}".format(c_p2))
        print("Carrier   \t{}".format(c_p2), file=output_file)


    def battleship(hidden_1, hidden_2):
        if "B" not in hidden_1:
            b_p1 = "X"
        else:
            b_p1 = "-"
        print("Battleship\t{} {}\t\t\t\t".format(b_p1, b_p1), end="")
        print("Battleship\t{} {}\t\t\t\t".format(b_p1, b_p1), end="", file=output_file)

        if "B" not in hidden_2:
            b_p2 = "X"
        else:
            b_p2 = "-"
        print("Battleship\t{} {}".format(b_p2, b_p2))
        print("Battleship\t{} {}".format(b_p2, b_p2), file=output_file)


    def destroyer(hidden_1, hidden_2):
        if "D" not in hidden_1:
            d_p1 = "X"
        else:
            d_p1 = "-"
        print("Destroyer \t{}\t\t\t\t".format(d_p1), end="")
        print("Destroyer \t{}\t\t\t\t".format(d_p1), end="", file=output_file)

        if "D" not in hidden_2:
            d_p2 = "X"
        else:
            d_p2 = "-"
        print("Destroyer \t{}".format(d_p2))
        print("Destroyer \t{}".format(d_p2), file=output_file)


    def submarine(hidden_1, hidden_2):
        if "S" not in hidden_1:
            s_p1 = "X"
        else:
            s_p1 = "-"
        print("Submarine \t{}\t\t\t\t".format(s_p1), end="")
        print("Submarine \t{}\t\t\t\t".format(s_p1), end="", file=output_file)

        if "S" not in hidden_2:
            s_p2 = "X"
        else:
            s_p2 = "-"
        print("Submarine \t{}".format(s_p2))
        print("Submarine \t{}".format(s_p2), file=output_file)


    def patrol_boat(hidden_1, hidden_2):
        if "P" not in hidden_1:
            p_p1 = "X"
        else:
            p_p1 = "-"
        print("Patrol Boat\t{} {} {} {}\t\t\t".format(p_p1, p_p1, p_p1, p_p1), end="")
        print("Patrol Boat\t{} {} {} {}\t\t\t".format(p_p1, p_p1, p_p1, p_p1), end="", file=output_file)

        if "P" not in hidden_2:
            p_p2 = "X"
        else:
            p_p2 = "-"
        print("Patrol Boat\t{} {} {} {}".format(p_p2, p_p2, p_p2, p_p2))
        print("Patrol Boat\t{} {} {} {}".format(p_p2, p_p2, p_p2, p_p2), file=output_file)


    def attack_to_bomb(hidden_board, board, move):
        print("Enter your move: {},{}".format(move[0], move[1]), "\n")
        print("Enter your move: {},{}".format(move[0], move[1]), "\n", file=output_file)
        row = int(move[0]) - 1
        col = column_letters.get(move[1])
        if hidden_board[row][col] == "-":
            hidden_board[row][col] = "O"
            board[row][col] = "O"
        else:
            hidden_board[row][col] = "X"
            board[row][col] = "X"


    def print_error():
        print(error, "\n")
        print(error, "\n", file=output_file)


    round_p1 = 0
    round_p2 = 0
    for move_p1, move_p2 in zip(player1_move, player2_move):
        check_p1 = [item for rows in player1_hidden_board for item in rows]
        check_p2 = [item for rows in player2_hidden_board for item in rows]
        try:
            if len(move_p1) > 2:
                raise ValueError("ValueError: {} too many values to unpack, expected 2".format(" ".join(move_p1)))
            elif len(move_p1) < 2:
                raise IndexError("IndexError: {} not enough values, expected 2!".format(" ".join(move_p1)))
            elif move_p1[0] == "" or move_p1[1] == "":
                raise IndexError("IndexError: {} not enough values, expected 2!".format(" ".join(move_p1)))
            elif not 0 < int(move_p1[0]) < 11 and move_p1[1] not in letters:
                raise AssertionError("AssertionError: {} invalid row and column!".format(" ".join(move_p1)))
            elif not 0 < int(move_p1[0]) < 11:
                raise AssertionError("AssertionError: {} invalid row!".format(" ".join(move_p1)))
            elif move_p1[1] not in letters:
                raise AssertionError("AssertionError: {} invalid column!".format(" ".join(move_p1)))
            else:
                round_p1 += 1
                print("Player1’s Move \n")
                print("Player1’s Move \n", file=output_file)
                players_round(round_p1)
                print_grid(board_p1, board_p2)
                carrier(check_p1, check_p2)
                battleship(check_p1, check_p2)
                destroyer(check_p1, check_p2)
                submarine(check_p1, check_p2)
                patrol_boat(check_p1, check_p2)
                attack_to_bomb(player2_hidden_board, board_p2, move_p1)

        except IndexError as error:
            print_error()
        except ValueError as error:
            print_error()
        except AssertionError as error:
            print_error()
        except Exception:
            print("kaBOOM: run for your life! \n")
            print("kaBOOM: run for your life! \n", file=output_file)

        try:
            if len(move_p2) > 2:
                raise ValueError("ValueError: too many values to unpack, expected 2")
            elif len(move_p2) < 2:
                raise IndexError("IndexError: not enough values, expected 2")
            elif move_p2[0] == "" or move_p2[1] == "":
                raise IndexError("IndexError: not enough values, expected 2")
            elif not 0 < int(move_p2[0]) < 11 and move_p2[1] not in letters:
                raise AssertionError("AssertionError: invalid row and column!")
            elif not 0 < int(move_p2[0]) < 11:
                raise AssertionError("AssertionError: invalid row!")
            elif move_p2[1] not in letters:
                raise AssertionError("AssertionError: invalid column!")
            else:
                round_p2 += 1
                print("Player2’s Move \n")
                print("Player2’s Move \n", file=output_file)
                players_round(round_p2)
                print_grid(board_p1, board_p2)
                carrier(check_p1, check_p2)
                battleship(check_p1, check_p2)
                destroyer(check_p1, check_p2)
                submarine(check_p1, check_p2)
                patrol_boat(check_p1, check_p2)
                attack_to_bomb(player1_hidden_board, board_p1, move_p2)

        except ValueError as error:
            print_error()
        except IndexError as error:
            print_error()
        except AssertionError as error:
            print_error()
        except Exception:
            print("kaBOOM: run for your life! \n")
            print("kaBOOM: run for your life! \n", file=output_file)


        def final_information():
            print("Final Information \n")
            print("Final Information \n", file=output_file)
            print("Player1’s Board \t\t\tPlayer2’s Board")
            print("Player1’s Board \t\t\tPlayer2’s Board", file=output_file)
            print(letters, "\t   ", letters)
            print(letters, "\t   ", letters, file=output_file)


        if ('C' and 'B' and 'D' and 'S' and 'P' not in check_p2) and (
                'C' and 'B' and 'D' and 'S' and 'P' not in check_p1):
            print("The game is a draw \n")
            print("The game is a draw \n", file=output_file)
            final_information()
            print_grid(player1_hidden_board, player2_hidden_board)
            carrier(check_p1, check_p2)
            battleship(check_p1, check_p2)
            destroyer(check_p1, check_p2)
            submarine(check_p1, check_p2)
            patrol_boat(check_p1, check_p2)
            break

        elif 'C' and 'B' and 'D' and 'S' and 'P' not in check_p2:
            print("Player1 Wins! \n")
            print("Player1 Wins! \n", file=output_file)
            final_information()
            print_grid(player1_hidden_board, player2_hidden_board)
            carrier(check_p1, check_p2)
            battleship(check_p1, check_p2)
            destroyer(check_p1, check_p2)
            submarine(check_p1, check_p2)
            patrol_boat(check_p1, check_p2)
            break

        elif 'C' and 'B' and 'D' and 'S' and 'P' not in check_p1:
            print("Player2 Wins! \n")
            print("Player2 Wins! \n", file=output_file)
            final_information()
            print_grid(player1_hidden_board, player2_hidden_board)
            carrier(check_p1, check_p2)
            battleship(check_p1, check_p2)
            destroyer(check_p1, check_p2)
            submarine(check_p1, check_p2)
            patrol_boat(check_p1, check_p2)
            break

output_file.close()

