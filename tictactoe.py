def print_grid(cells):
    print("---------")
    for i in range(3):
        print(f"| {cells[3 * i]} {cells[3 * i + 1]} {cells[3 * i + 2]} |")
    print("---------")


def check_winner(cells):
    rows = ["".join(cells[0:3]), "".join(cells[3:6]), "".join(cells[6:9])]

    columns = ["".join([cells[0], cells[3], cells[6]]),
               "".join([cells[1], cells[4], cells[7]]),
               "".join([cells[2], cells[5], cells[8]])]

    diagonals = ["".join([cells[0], cells[4], cells[8]]),
                 "".join([cells[2], cells[4], cells[6]])]

    if "XXX" in rows + columns + diagonals:
        return "X wins"
    elif "OOO" in rows + columns + diagonals:
        return "O wins"
    elif " " not in cells:
        return "Draw"
    else:
        return "Game not finished"


def is_valid_move(x, y, cells):
    if not (x.isdigit() and y.isdigit()):
        return "You should enter numbers!"
    x, y = int(x), int(y)
    if not (1 <= x <= 3 and 1 <= y <= 3):
        return "Coordinates should be from 1 to 3!"
    index = (x - 1) + (y - 1) * 3
    if cells[index] != " ":
        return "This cell is occupied! Choose another one!"
    return None


def make_move(cells, x, y, symbol):
    index = (x - 1) + (y - 1) * 3
    return cells[:index] + symbol + cells[index + 1:]


cells = "           "
print_grid(cells)
current_symbol = "X"
while True:
    x, y = input("Enter the coordinates: ").split()
    error = is_valid_move(x, y, cells)
    while error:
        print(error)
        x, y = input("Enter the coordinates: ").split()
        error = is_valid_move(x, y, cells)

    cells = make_move(cells, int(x), int(y), current_symbol)
    print_grid(cells)

    result = check_winner(cells)
    if result != "Game not finished":
        print(result)
        break

    current_symbol = "O" if current_symbol == "X" else "X"
