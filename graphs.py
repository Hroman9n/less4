
# в данном случае я использовал ордерево, где мы можем только спускаться на уровень ниже, но если заменить -1 на 1, то получится обыкновенное дерево
tree = [['s', 1, 1, 1, 0, 0, 0, 0],             #        0
        [-1, 's', 0, 0, 1, 1, 0, 0],            #     /   |  \
        [-1, 0, 's', 0, 0, 0, 1, 0],            #    /    |   \
        [-1, 0, 0, 's', 0, 0, 0, 1],            #   1     2    3
        [0, -1, 0, 0, 's', 0, 0, 0],            #   /\    |     \
        [0, -1, 0, 0, 0, 's', 0, 0],            #  /  \   |      \
        [0, 0, -1, 0, 0, 0, 's', 0],            # 4    5  6       7
        [0, 0, 0, -1, 0, 0, 0, 's']]            #

tree_dict = dict()                              # словарь, в котором запись строится следующим образом
                                                # ключ - вершина, значения - вершины, в которые мы можем перейти из ключевой

for i in range(len(tree)):
    if str(i) not in tree_dict:                 # если вершина ещё не находится в словаре, добавляем её
            tree_dict[str(i)] = []
    for j in range(len(tree[i])):
        if tree[i][j] == 1:                     # если мы видим единицу, значит вершины связаны, и мы можем перейти
            tree_dict[str(i)].append(j)         # добавляем номер вершины в возможные пути
        
print(tree_dict)