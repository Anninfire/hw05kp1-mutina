# Игровое поле
maps = [1,2,3,
        4,5,6,
        7,8,9]

# Выигрышные сочитания
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

# Печатаем поле
def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

# Ход
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Проверить выигрышные сочитания
def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем игровое поле
    print_maps()

    # 2. Запрос хода
    if player1 == True:
        symbol = "X"

        step = int(input("X, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("O, ваш ход: "))

    step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print("Победитель", win)

