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

    def find_path(self, end_pos):

        # find the node with end_pos value
        target_node = self._root.depth_search(end_pos)

        #  if we found the node, then call trace_to_root
        if target_node:
            return self.trace_to_root(target_node)

        # otherwise, return an empty path
        return []

    def trace_to_root(self, end_node):
        path = []

        current = end_node
        while current is not None:
            path.append(current.value)
            current = current.parent

        # reverse the path so it starts at the root
        return path[::-1]








if __name__ == '__main__':
    knight = KnightPathFinder((0, 0))
    knight.build_move_tree()
    print(knight.find_path((2, 1)))
    print(knight.find_path((3, 3)))
    print(knight.find_path((6, 2)))
    print(knight.find_path((7, 6)))
