from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return f"{self.data}"


class Tree:
    def __init__(self):
        self.root = None

    @staticmethod
    def __find(node, parent, value):
        if node is None:
            return None, parent, False

        while True:
            if value < node.data:
                parent = node
                if not node.left:
                    break
                node = node.left

            elif value > node.data:
                parent = node
                if not node.right:
                    break
                node = node.right

            else:
                return node, parent, True  # value уже в дереве

        return node, parent, False

    def __find_min(self, node, parent):
        if node.left is None:
            return node, parent

        while True:
            parent = node
            node = node.left
            if node.left is None:
                return node, parent


    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node, direction="left"):
        res, stack = [], deque()
        direction = ("left", "right") if direction == "left" else ("right", "left")
        print(f"we are on node {node.data}")

        while True:  # совершаем проход по ветви вниз
            stack.append(node)
            node = node.__getattribute__(direction[0])
            print(f"we are on node {node}")
            if not node:  # дошли до листовой вершины
                while True:  # совершаем проход по ветви вверх
                    try:
                        node = stack.pop()
                    except IndexError:
                        return res
                    res.append(node.data)
                    node = node.__getattribute__(direction[1])
                    print(f"we are on node {node}")
                    if node:  # если встретили не листовую вершину прерываем цикл и вываливаемся в цикл идущий вниз
                        break

    def show_wide_tree(self, node):
        if node is None:
            return None

        v = [node]
        while v:
            vn = []
            for i in v:
                print(i.data, end=" ")
                if i.left:
                    vn.append(i.left)
                if i.right:
                    vn.append(i.right)
            print("")
            v = vn

    def __del_leaf(self, s, p):
        """
        удаление листовой вершины
        """
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        """
        удаление вершины с одним потомком
        """
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def dell_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:  # key не найден в дереве
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

# v = [10, 5, 7, 16, 13, 2, 20]
#
# t = Tree()
# for x in v:
#     t.append(Node(x))
#
# #print(t.show_tree(t.root, direction="right"))
# t.show_wide_tree(t.root)
# t.dell_node(5)
#
# t.show_wide_tree(t.root)

v = [20, 5, 24, 2, 16, 11, 18]

t = Tree()
for x in v:
    t.append(Node(x))

#st.show_wide_tree(t.root)
t.dell_node(5)

t.show_wide_tree(t.root)
