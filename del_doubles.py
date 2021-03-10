import random

def delitto(a):

    repeated = []                       # сюда записываются впервые встречающиеся элементы
    res = []                            # этот массив необходим, так как если мы будем удалять элементы из списка
                                        # то получим ошибку IndexError
    for i in range(len(a)):
        if a[i] not in repeated:
            res.append(a[i])
            repeated.append(a[i])

    return res


# тестовый массив
a = [10, 0, 2, 3, 3, 4, 6, 0, 2, 5, 5, 1, 4, 5]

while 1:
    print()

    print("""Удаление повторяшек
    Для ввода собственного списка введите                   1
    Для использования заранее записанного списка введите    2
    Для выхода нажмите Enter""")

    ask = input("Вариант ввода: ")

    if ask == "":
        exit()
    elif ask == "2":
        res = delitto(a)
    elif ask == "1":
        print()

        ai = input("Введите элементы списка через пробел: ")

        res = delitto(ai)
    else:
        print("\nОшибка ввода. Попробуйте ещё раз")

    print()

    if res != []:
        print("\nИтоговый массив: ")
        for i in res:
            print(i, end=" ")

    print("\n\n")