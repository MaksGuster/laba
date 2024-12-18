import random


def main():
    print("Добро пожаловать в игру!!!!!!!!!")
    print("Правила: вы и компьютер по очереди берете 1, 2 или 3 камня.")
    print("Тот, кто оставляет последний камень своему сопернику, выигрывает.")

    user_wins = 0
    computer_wins = 0

    while True:
        N = random.randint(4, 30)
        print(f"\nВ начале игры {N} камней.")

        while N > 0:
            user_move = get_user_move(N)
            N -= user_move
            print(f"\nВы взяли {user_move} камней. Осталось {N} камней.")
            if N == 0:
                print("Поздравляем! Вы выиграли!")
                user_wins += 1
                break

            computer_move = get_computer_move(N)
            N -= computer_move

            print(f"\nКомпьютер взял {computer_move} камней. Осталось {N} камней.")
            if N == 0:
                print("Компьютер выиграл! Попробуйте снова.")
                computer_wins += 1

        print(f"\nТекущий счет: Вы {user_wins} - Компьютер {computer_wins}")

        play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != "да":
            print("Спасибо за игру!")
            break


def get_user_move(remaining_stones):
    while True:
        try:
            move = int(input(f"\nСколько камней вы хотите взять? (1, 2 или 3): "))
            if move in [1, 2, 3] and move <= remaining_stones:
                return move
            else:
                print("Неверный ввод. Пожалуйста, возьмите 1, 2 или 3 камня, не превышая оставшиеся.")
        except ValueError:
            print("Пожалуйста, введите число.")


def get_computer_move(remaining_stones):
    move = random.randint(1, min(3, remaining_stones))
    print(f"Компьютер выбрал {move} камней.")
    return move


main()