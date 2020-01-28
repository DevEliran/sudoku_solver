def create_sudoku():
    board = [['_', '_', '_', 2, 6, '_', 7, '_', 1],
             [6, 8, '_', '_', 7, '_', '_', 9, '_'],
             [1, 9, '_', '_', '_', 4, 5, '_', '_'],
             [8, 2, '_', 1, '_', '_', '_', 4, '_'],
             ['_', '_', 4, 6, '_', 2, 9, '_', '_'],
             ['_', 5, '_', '_', '_', 3, '_', 2, 8],
             ['_', '_', 9, 3, '_', '_', '_', 7, 4],
             ['_', 4, '_', '_', 5, '_', '_', 3, 6],
             [7, '_', 3, '_', 1, 8, '_', '_', '_']]
    return board


def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i > 0:
            print("------------------")
        for j, col in enumerate(row):
            if j % 3 == 0 and j > 0:
                print("|", end="")
            if j == len(board[0]) - 1:
                print(board[i][j])
            else:
                print(str(board[i][j])+' ', end="")


def find_empty_field(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return [i, j]
    return None


def is_valid(board, n, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == n and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == n and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == n and (i, j) != pos:
                return False
    return True


def solve(board):
    empty_pos = find_empty_field(board)
    if not empty_pos:
        return True
    else:
        r, c = empty_pos
    for i in range(1, 10):
        if is_valid(board, i, [r, c]):
            board[r][c] = i
            if solve(board):
                return True
            board[r][c] = '_'
    return False


def main():
    sudoku = create_sudoku()
    print("Original board : ")
    print_board(sudoku)
    solve(sudoku)
    print()
    print("Solution : ")
    print_board(sudoku)


if __name__ == '__main__':
    main()