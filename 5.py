from collections import deque

message = """Введите N, M"""

rules = """
Поле вводится в виде матрицы N x M
"_" - белая клетка
"0" - чёрная клетка
"#" - дырка
"""

#  ввод
white = []
black_squares = []
black_turns = []
holes = []
turn = 0

print(message)
N, M = map(int, input().split())
print(rules)
for i in range(N):
    line = input()
    for j in range(M):
        if line[j] == '_':
            white.append((i, j))
        elif line[j] == '0':
            black_squares.append((i, j))
            black_turns.append(turn)
        else:
            holes.append((i, j))

# раскраска
to_paint = deque((black_squares[i], black_turns[i]) for i in range(len(black_squares)))
max_turn = turn
while to_paint and white:
    square, turn = to_paint.popleft()
    moves = ((+1, 0), (-1, 0), (0, +1), (0, -1))

    for move in moves:
        new_square = (square[0] + move[0], square[1] + move[1])
        if new_square in white:
            to_paint.append((new_square, turn + 1))
            white.remove(new_square)
            black_squares.append(new_square)
            black_turns.append(turn + 1)
            max_turn = turn + 1

# вывод ответа
if not white:
    print("Необходимое число ходов: ", max_turn)
else:
    print("Невозможно раскрасить")

# вывод поля
'''
for i in range(N):
    for j in range(M):
        if (i, j) in white:
            print('_', end=' ')
        elif (i, j) in holes:
            print('#', end=' ')
        else:
            print(black_turns[black_squares.index((i, j))], end=' ')
    print()
'''
