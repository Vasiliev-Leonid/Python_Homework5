#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Без filtr и lambda

# txt = input("Enter your text:\n") 
# print(f"Initial text: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Result: {" ".join(lst)}')

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
# ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все 
# конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# from random import randint
# def input_dat(name):
#     x = int(input(f"{name}, Please enter your number from 1 till 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, It is not correct. Please try again: "))
#     return x
# def p_print(name, k, counter, value):
#     print(
#         f" {name}, took {k}, now he have {counter}. The rest {value} ")
# player1 = input("Enter the first player: ")
# player2 = input("Enter the second player: ")
# value = int(input("Enter the quantaty of the bon-bon on the table: "))
# flag = randint(0, 2)  
# if flag:
#     print(f"The first try {player1}")
# else:
#     print(f"The second try {player2}")
# counter1 = 0
# counter2 = 0
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
# if flag:
#     print(f" The winner {player1}")
# else:
#     print(f"The winner  {player2}")


# Создайте программу для игры в ""Крестики-нолики"".

# board = [" " for i in range(9)]

# def print_board():
#     row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
#     row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
#     row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

#     print()
#     print(row1)
#     print(row2)
#     print(row3)
#     print()

# def player_move(icon):
#     if icon == "X":
#         number = 1
#     elif icon == "O":
#         number = 2

#     print("Your turn player {}".format(number))

#     choice = int(input("Enter your move(1-9): ").strip())
#     if board[choice-1] ==" ":
#         board[choice-1] = icon
#     else:
#         print()
#         print("That space is take!")

# def is_victory(icon):
#     if (board[0] == icon and board[1] ==  icon and board[2] == icon) or \
#          (board[3] == icon and board[4] ==  icon and board[5] == icon) or \
#          (board[6] == icon and board[7] ==  icon and board[8] == icon) or \
#          (board[0] == icon and board[3] ==  icon and board[6] == icon) or \
#          (board[1] == icon and board[4] ==  icon and board[7] == icon) or \
#          (board[2] == icon and board[5] ==  icon and board[8] == icon) or \
#          (board[0] == icon and board[4] ==  icon and board[8] == icon) or \
#          (board[2] == icon and board[4] ==  icon and board[6]== icon):
#         return True
#     else:
#         return False

# def is_draw():
#     if" " not in board:
#         return True
#     else:
#         return False
# while True:
#     print_board()
#     player_move("X")
#     print_board()
#     if is_victory("X"):
#         print("X Wins! Congratulations!")
#         break
#     elif is_draw():
#         print("its a draw!")
#         break
#     player_move("O")
#     if is_victory("O"):
#         print_board()
#         print("O Wins! Congratulations!")
#         break
#     elif is_draw():
#         print("its a draw!")
#         break


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.
