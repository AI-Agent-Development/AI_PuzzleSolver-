from typing import List, Tuple, Optional
class EightPuzzle:
    def __init__(self, board: List[int]):
        if len(board) != 9:
            raise ValueError("Board must have 9 elements.")
        self.board = tuple(board)
        self.size = 3
        self.goal = tuple(range(1, 9)) + (0,)

    def is_goal(self) -> bool:
        return self.board == self.goal

    def find_zero(self) -> int:
        """Find the index of the blank (0) tile."""
        return self.board.index(0)

    def get_moves(self) -> List[str]:
        """Return possible moves from current blank position."""
        zero_pos = self.find_zero()
        row, col = divmod(zero_pos, self.size)
        moves = []
        if row > 0: moves.append("up")
        if row < self.size - 1: moves.append("down")
        if col > 0: moves.append("left")
        if col < self.size - 1: moves.append("right")
        return moves

    def move(self, direction: str) -> Optional['EightPuzzle']:
        """Return new puzzle state after moving in the given direction."""
        zero_pos = self.find_zero()
        row, col = divmod(zero_pos, self.size)

        if direction == "up": row -= 1
        elif direction == "down": row += 1
        elif direction == "left": col -= 1
        elif direction == "right": col += 1
        else: return None

        if 0 <= row < self.size and 0 <= col < self.size:
            swap_pos = row * self.size + col
            new_board = list(self.board)
            new_board[zero_pos], new_board[swap_pos] = new_board[swap_pos], new_board[zero_pos]
            return EightPuzzle(new_board)
        return None

    def get_successors(self) -> List[Tuple[str, 'EightPuzzle']]:
        """Return list of (move, new_state) tuples for all possible moves."""
        return [(move, self.move(move)) for move in self.get_moves() if self.move(move)]

    def __str__(self):
        """Return a human-readable string representation of the board."""
        return "\n".join(
            " ".join(str(n) if n != 0 else "_" for n in self.board[i:i+3])
            for i in range(0, 9, 3)
        )

    def __eq__(self, other):
        return isinstance(other, EightPuzzle) and self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def __lt__(self, other):
        return self.board < other.board 
