from typing import List, Optional
from puzzle import EightPuzzle
from utils import is_solvable
from algorithms import bfs, a_star

def solve_puzzle(board: List[int], goal: List[int], method: str = "a_star") -> Optional[List[str]]:
    if not is_solvable(board, goal):
        return None

    puzzle = EightPuzzle(board, goal)

    if method == "bfs":
        return bfs(puzzle)
    else:
        return a_star(puzzle)
