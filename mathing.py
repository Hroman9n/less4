### функции для мат. вычислений ###
def plus(f, s):
    return f + s

def minus(f, s):
    return f - s

def multy(f, s):
    return f * s

def divide(f, s):
    return f / s

# необходимый словарь, чтобы мы могли ассоциативно выполнять операцию, получая символ
ops = {'+': plus, '-': minus, '*': multy, '/': divide}

### функция для вычислений приоритета операций, потребуется для преобразования в ОПЗ ###
def ops_prior(op):
    if op == '+':
        return 1
    elif op == '-':
        return 1
    elif op == '/':
        return 2
    elif op == '*':
        return 3

### функция для вычисления примера, переведенного в польскую запись
def polsk_ans(polsk):
    stack = []                      # результирующий массив, в котором будут производиться вычисления
    lst = list(polsk)               # здесь необходимо формировать список из списка, так как иначе lst будет просто ссылаться на polsk

    for i in polsk:
        if i.isdigit():             # если встречается число
            stack.append(i)         # просто добавляем в стек
        else:                       # TODO: необходимо поставить проверку, что в стеке есть минимум 2 элемента
            tmp2, tmp1 = stack.pop(), stack.pop()           # берем два последних элемента стека. Порядок важен, так как извлекаем с конца, первым идет tmp2 (для операций вычитания/деления)
            stack.append(ops[i](float(tmp1), float(tmp2)))  # применяем к ним операцию (выбор операции идет через ассоциативный словарь)
    
    return stack.pop()

### функция для перевода строки с примером в ОПЗ ###
def to_polsk(primer):
    
    res = []                       
    opers = []
    lst = list(primer.split())

    for i in lst:
        if i.isdigit():         # если текущий символ число просто добавляем в вывод
            res.append(i)
        elif i in ['+', '-', '/', '*']: # если символ - оператор
            tmp = ''
            if len(opers) > 0:          # если стек операторов не пуст проверяем приоритет
                tmp = opers[-1]
                while len(opers) > 0 and tmp != '(':
                    if ops_prior(i) <= ops_prior(tmp):
                        res.append(opers.pop())
                    else:
                        break
            opers.append(i)             # в конце добавляем текущий оператор в стек операторов
        elif i == '(':                  # если встретилась открывающая скобка добавим в стек
            opers.append(i)
        elif i == ')':
            tmp = opers[-1]
            while tmp != '(':           # пока не встретим открывающую скобку
                res.append(opers.pop()) # перекидываем операторы в итоговую строку
                tmp = opers[-1]
                if len(opers) == 0:
                    print("Ошибка ввода, в примере пропущена (")
                    return
                if tmp == '(':
                    opers.pop()

    while len(opers) > 0:
        tmp = opers[-1]
        res.append(opers.pop())
        if tmp == '(':
            print("Ошибка ввода, в примере пропущена )")
            return

    return res

a = to_polsk('57 * 6 + 35 * 5 + 2')
c = ['3', '4', '+']
b = ['1', '2', '+', '4', '*', '3', '+']
d = to_polsk('( 45 + 45 ) / ( 180 - 90 )')
e = ['7', '2', '3', '*', '-']

assert polsk_ans(a) == 519.0
assert polsk_ans(b) == 15.0
assert polsk_ans(c) == 7.0
assert polsk_ans(d) == 1.0
assert polsk_ans(e) == 1.0
