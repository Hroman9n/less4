

tree = [['s', 1, 1, 1, 0, 0, 0, 0],             #        0
        [-1, 's', 0, 0, 1, 1, 0, 0],            #     /   |  \
        [-1, 0, 's', 0, 0, 0, 1, 0],            #    /    |   \
        [-1, 0, 0, 's', 0, 0, 0, 1],            #   1     2    3
        [0, -1, 0, 0, 's', 0, 0, 0],            #   /\    |     \
        [0, -1, 0, 0, 0, 's', 0, 0],            #  /  \   |      \
        [0, 0, -1, 0, 0, 0, 's', 0],            # 4    5  6       7
        [0, 0, 0, -1, 0, 0, 0, 's']]            #

tree_dict = dict()

for i in range(len(tree)):
    if str(i) not in tree_dict:
            tree_dict[str(i)] = []
    for j in range(len(tree[i])):
        if tree[i][j] == 1:
            tree_dict[str(i)].append(j)
        
print(tree_dict)