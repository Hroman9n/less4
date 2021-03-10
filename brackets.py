def brackets_chk(msg):

    stack = []                                      # сюда будут закидываться скобки

    associate = {')': '(', ']': '[', '}': '{'}      # необходимо для проверки какая скобка подается

    for i in msg:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif i == ')' or i == ']' or i == '}':
            if stack == [] and i == ')' or i == ']' or i == '}':
                print(f"\nПрисутствует закрывающая скобка {i}, когда нет открывающей скобки такого же вида")
                return
            elif stack[-1] == associate[i]:
                stack.pop()
            elif stack[-1] != associate[i]:
                print(f"\nСкобка {i} не закрыта")
                return

    if stack == []:
        print("\nВсе скобки закрыты правильно")
    else:
        remain = ""
        for i in stack:
            remain.join(i + ' ')
        print("\nОставшиеся незакрытые скобки: " + remain)


# message = "i (love) programming"
message = "this  is wrong] string"
# message = "this ({}) should [be] ({[correct]})"
# message = "([{}])"

# brackets_chk(message)

while 1:
    print()
    print("""Проверка скобок
    Для ввода собственной строки введите                    1
    Для использования заранее записанной строки введите     2
    Для выхода нажмите Enter""")

    ask = input("Вариант ввода: ")

    if ask == "":
        exit()
    elif ask == "2":
        brackets_chk(message)
    elif ask == "1":
        imessage = input("Введите строку: ")
        brackets_chk(imessage)
    else:
        print("\nОшибка ввода. Попробуйте ещё раз")
    