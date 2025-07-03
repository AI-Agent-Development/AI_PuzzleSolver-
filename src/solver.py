from typing import List, Tuple, Optional
from puzzle import EightPuzzle
from algorithms import bfs, a_star
from utils import is_solvable

def solve_puzzle(board: List[int], goal: List[int], method: str = "a_star") -> Tuple[Optional[List[str]], int]:
    if not is_solvable(board, goal):
        return None, 0

    puzzle = EightPuzzle(board, goal)

    if method == "bfs":
        return bfs(puzzle)
    else:
        return a_star(puzzle)
