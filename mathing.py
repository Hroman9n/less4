
def plus(f, s):
    return f + s

def minus(f, s):
    return f - s

def multy(f, s):
    return f * s

def divide(f, s):
    return f / s

ops = {'+': plus, '-': minus, '*': multy, '/': divide}

def polsk_ans(primer):
    stack = []
    lst = list(primer)

    for i in primer:
        if i.isdigit():
            stack.append(i)
            lst.remove(i)
        else:
            tmp1, tmp2 = stack.pop(), stack.pop()
            stack.append(ops[i](float(tmp1), float(tmp2)))
            lst.remove(i)
    
    return stack.pop()

a = ['3', '4', '+']
b = ['1', '2', '+', '4', '*', '3', '+']

assert polsk_ans(a) == 7.0
assert polsk_ans(b) == 15.0

print(polsk_ans(a))
print(polsk_ans(b))