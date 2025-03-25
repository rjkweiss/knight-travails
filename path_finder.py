from collections import deque

from tree import Node


class KnightPathFinder:
    def __init__(self, start_pos):
        self._root = Node(start_pos)
        self._considered_positions = set([start_pos])

    def get_valid_moves(self, pos):
        valid_moves = []
        knight_offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for dx, dy in knight_offsets:
            next_x = pos[0] + dx
            next_y = pos[1] + dy

            if 0 <= next_x < 8 and 0 <= next_y < 8:
                valid_moves.append((next_x, next_y))

        return valid_moves

    def new_move_positions(self, pos):
        valid_moves = set(self.get_valid_moves(pos))
        new_moves = valid_moves.difference(self._considered_positions)
        self._considered_positions.update(new_moves)
        return new_moves

    def build_move_tree(self):
        # create queue with root node
        queue = deque([self._root])

        while queue:
            # pop first item in queue
            curr_node = queue.popleft()
            curr_pos = curr_node.value

            # find new positions starting at this place
            new_positions = self.new_move_positions(curr_pos)

            # for each node, set its parents (ultimately sets the children as well)
            for pos in new_positions:
                child_node = Node(pos)
                child_node.parent = curr_node
                queue.append(child_node)







if __name__ == '__main__':
    knight = KnightPathFinder((0, 0))
    knight.build_move_tree()
    for child in knight._root.children:
        print(f"{child.value}: {[c.value for c in child.children] }")
