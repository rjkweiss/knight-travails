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


if __name__ == '__main__':
    knight = KnightPathFinder((0, 0))
    print(knight.new_move_positions((0, 0)))
    print(knight.new_move_positions((1, 2)))
