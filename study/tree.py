class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def visit(T):
    print(T.data)


def preorder_traverse(T):
    if T:
        visit(T)
        preorder_traverse(T.left)
        preorder_traverse(T.right)


def inorder_traverse(T):
    if T:
        inorder_traverse(T.left)
        visit(T)
        inorder_traverse(T.right)


def postorder_traverse(T):
    if T:
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)


def trees(data):
    global root
    now = root
    for i in range(2, data + 2):
        if not now.left:
            now.left = Tree(i)
        elif not now.right:
            now.right = Tree(i)
        else:
            if now.left.right:
                now = now.right
                now.left = Tree(i)
            else:
                now = now.left
                now.left = Tree(i)


def print_tree(root):
    print(root.data)
    if tree[root][0] != 0:
        pre(tree[root][0])
    if tree[root][1] != 0:
        pre(tree[root][1])


tree_root = Tree(1)
root = tree_root


# tree_top.left = Tree(2)
# tree_top.right = Tree(3)
# print(tree_top.data)
# print(tree_top.left.data)
# print(tree_top.right.data)

# trees(10)
# print(top.data)
# print(top.left.data)
# print(top.right.data)
# print(top.left.left.data)
# print(top.left.right.data)
# print(top.left.left.left.data)
# print(top.left.left.right.data)
# # print(top.right.left.data)
# # print(top.right.right.data)

def pre(root):
    print(root)
    if tree[root][0] != 0:
        pre(tree[root][0])
    if tree[root][1] != 0:
        pre(tree[root][1])


inputS = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, inputS.split()))
V = 13
tree = [[0, 0] for _ in range(V + 1)]
parent = [0] * (V + 1)
for idx in range(0, len(lst), 2):
    p, c = lst[idx], lst[idx + 1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    parent[c] = p
# print(tree)
# print(parent)
pre(1)
