from collections import deque

message = """Введите N, M"""

rules = """
Поле вводится в виде матрицы N x M
"_" - белая клетка
"0" - чёрная клетка
"#" - дырка
"""

WHITE_SQUARE = -1
HOLE_SQUARE = -2


def check_square(square):
    global N, M
    i, j = square
    return (0 <= i < N) and (0 <= j < M)


#  ввод
turn = 0
white_count = 0
to_paint = deque()

print(message)
N, M = map(int, input().split())
print(rules)

Field = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    line = input()
    for j in range(M):
        if line[j] == '_':
            Field[i][j] = WHITE_SQUARE
            white_count += 1
        elif line[j] == '0':
            Field[i][j] = turn
            to_paint.append((i, j))
        else:
            Field[i][j] = HOLE_SQUARE

# раскраска
max_turn = turn
while to_paint and white_count:
    square = to_paint.popleft()
    turn = Field[square[0]][square[1]]

    moves = ((+1, 0), (-1, 0), (0, +1), (0, -1))

    for move in moves:
        new_square = (square[0] + move[0], square[1] + move[1])

        if check_square(new_square):
            if Field[new_square[0]][new_square[1]] == WHITE_SQUARE:
                to_paint.append(new_square)
                Field[new_square[0]][new_square[1]] = turn + 1
                white_count -= 1
                max_turn = turn + 1

# вывод ответа
if not white_count:
    print("Необходимое число ходов: ", max_turn)
else:
    print("Невозможно раскрасить")

# вывод поля
'''
for i in Field:
    for j in i:
        print(j, end=' ')
    print()
'''
