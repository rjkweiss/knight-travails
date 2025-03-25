from collections import deque


class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self._children:
            node.parent = self

    def remove_child(self, node):
        if node in self._children:
            # delete from list
            self._children.remove(node)

            # update parent to node
            node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent is not None:
            self._parent.remove_child(self)
        self._parent = node
        if node and self not in node.children:
            node._children.append(self)

    def depth_search(self, value):
        if self.value == value:
            return self

        for child in self.children:
            res = child.depth_search(value)

            if res:
                return res

        return None

    def breadth_first_search(self, value):
        queue = deque([self])
        while queue:
            curr_node = queue.popleft()

            if curr_node.value == value:
                return curr_node
            for child in curr_node.children:
                queue.append(child)

        return None


# node1 = Node('root1')
# node2 = Node('root2')
# node3 = Node('root3')

# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)

# print(f'node 1 parent: {node1.parent}')
# print(f'node 2 parent: {node2.parent}')
# print(f'node 3 parent: {node3.parent.value}')
