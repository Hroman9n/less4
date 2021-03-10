import random

def bubble(a):

    for i in range(len(a)):
        for j in range (len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

# тестовые значения
# заранее записанный массив для теста
ar = [10, 31, 2, 4, 1, -15, 46, 23, 0, -4982385]
# рандомно генерируемый массив


while 1:
    res = []
    print("""Сортировка пузырьком
    Для ввода собственного списка введите                   1
    Для использования случайных чисел в массиве введите     2
    Для использования заранее записанного массива введите   3
    Для выхода нажмите Enter""")

    ask = input("Вариант ввода: ")

    if ask == "":
        exit()
    elif ask == "3":
        res = bubble(ar)
    elif ask == "2":
        arand = []
        for i in range(10):
            arand.append(random.randint(-100, 99))

        res = bubble(arand)
    elif ask == "1":
        try:
            arr = list(input("Введите значения через пробел: ").split())
            arr = list(map(int, arr))
        except ValueError:
            print("Ошибка ввода. Попробуйте ещё раз")
        
        res = bubble(arr)
    else:
        print("Ошибка ввода. Попробуйте ещё раз")

    print()

    if res != []:
        print("Итоговый массив: ")
        for i in res:
            print(i, end=" ")
    
    print("\n\n")
