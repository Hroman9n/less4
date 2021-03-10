### костыль, который я написал перед там как вспомнил,
###  что можно сравнивать множества

# def comp(list1, list2):
#     setl1 = list(set(list1))
#     setl2 = list(set(list2))

#     if len(setl1) != len(setl2):                                # если длинна списков не совпадает то множества уже не равны
#         print("\nМножества из данных списков не совпадают\n")   # поэтому нам не нужно сравнивать какое из множеств больше чтобы взять за основу первого цикла
#         return
#     else:
#         # идем по каждому предмету в первом списке, 
#         # если находим его во втором то удаляем его
#         for i in setl1:
#             for j in range(len(setl2)):
#                 if setl2[j] == i:
#                     setl2.remove(setl2[j])
#                     break
    
#     if setl2 != []:
#         print("\n Множества из данных списков не совпадают\n")
#     else:
#         print("\nМножества из данных списков совпадают\n")



def comp(list1, list2):

    a = set(list1)
    b = set(list2)

    if a == b:
        print("\nМножества из данных списков совпадают\n")
    else:
        print("\n Множества из данных списков не совпадают\n")


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
    elif ask == "1":
        try:
            frsti = list(input("Введите значения первого списка через пробел: ").split())
            frsti = list(map(int, frsti))

            scndi = list(input("Введите значения первого списка через пробел: ").split())
            scndi = list(map(int, scndi))
        except ValueError:
            print("Ошибка ввода. Попробуйте ещё раз")

        comp(frsti, scndi)

    else:
        print("\nОшибка ввода. Попробуйте ещё раз")