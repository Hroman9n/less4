
def comp(list1, list2):
    setl1 = list(set(list1))
    setl2 = list(set(list2))

    if len(setl1) != len(setl2):
        print("\nМножества из данных списков не совпадают\n")
        return
    else:
        for i in setl1:
            for j in range(len(setl2)):
                if setl2[j] == i:
                    setl2.remove(setl2[j])
                    break
    
    if setl2 != []:
        print("\n Множества из данных списков не совпадают\n")
    else:
        print("\nМножества из данных списков совпадают\n")


# тестовые списки #
frst = [10, 2, 3, 4, 5, 1, 3, 6, 1]         # совпадает с первым scnd
# frst = [2, 3, 5, 1, 10]                   # не совпадает с первым scnd
scnd = [3, 4, 1, 4, 2, 10, 10, 6, 5, 5]     # совпадает с первым frst
# scnd = [1, 2, 3, 4, 5, 6, 7]              # не совпадает со вторым frst

while 1:
    print()

    print("""Сравнение множеств
    Для ввода собственных списков введите                   1
    Для использования заранее записанных списков введите    2
    Для выхода нажмите Enter""")

    ask = input("Вариант ввода: ")

    if ask == "":
        print("\nДо встречи!")
        exit()
    elif ask == "2":
        comp(frst, scnd)
    # elif ask == "1":
    #     # frsti = input("\nВведите первый список: ")
    #     # scndi = input("Введите второй список: ")


    else:
        print("\nОшибка ввода. Попробуйте ещё раз")