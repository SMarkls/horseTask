def formating(board): # форматирует список списков, чтобы он выглядел, как шахматная доска
    ans = ''
    for i in range(len(board)):
        for j in range(len(board[i])):
            ans += str(board[i][j]) + '\t'
        ans += '\n'
    return ans


def allow_moves(x, y): # ищет всевозможные шаги для конкретных x, y, возвращает список ходов.
    possible = []
    for step in steps:
        if (0 <= x + step[0] < N) and (0 <= y + step[1] < M) and (board[y + step[1]][x + step[0]]) == 0:
            possible.append(step)
    return possible


def solve():
    x = X - 1
    y = Y - 1
    for i in range(1, M * N + 1):
        board[y][x] = i
        next_step = []
        min = 100
        for move in allow_moves(x, y):
            count = len(
                allow_moves(x + move[0], y + move[1]))          # здесь реализуется правило Варнсдорфа, согласно которому
            if count < min and (count != 0 or i == N * M - 1):  # коню нужно идти на ту клетку, с которой можно сделать
                min = count                                     # меньше ходов
                next_step = move
        if len(next_step) == 0:
            break
        x += next_step[0]
        y += next_step[1]
    if i != M * N:
        print("Маршрут не существует")


steps = ((-2, -1), (2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (2, 1), (1, 2))  # все возможные ходы коня
f = open("input.txt", "r")
M, N = map(int, f.readline().split()) # размеры доски в формате: строки, столбцы
X, Y = map(int, f.readline().split()) # стартовые координаты
f.close()

board = [[0 for j in range(N)] for i in range(M)]
solve()
f = open("output.txt", 'w')
f.write(formating(board))