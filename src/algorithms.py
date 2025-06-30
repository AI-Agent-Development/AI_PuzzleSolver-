from collections import deque
from typing import Dict, Tuple, List, Optional
import heapq
from puzzle import EightPuzzle
from utils import manhattan_distance

def bfs(start: EightPuzzle) -> Optional[List[str]]:
    """Breadth-First Search (uninformed). Returns list of moves."""
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state.is_goal():
            return path

        for move, next_state in current_state.get_successors():
            if next_state not in visited:
                queue.append((next_state, path + [move]))
    return None


def a_star(start: EightPuzzle) -> Optional[List[str]]:
    """A* Search using Manhattan distance. Returns list of moves."""
    visited = set()
    heap = []
    heapq.heappush(heap, (manhattan_distance(start.board), 0, start, []))  

    while heap:
        f, g, current_state, path = heapq.heappop(heap)

        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state.is_goal():
            return path

        for move, next_state in current_state.get_successors():
            if next_state not in visited:
                g_new = g + 1
                h_new = manhattan_distance(next_state.board)
                f_new = g_new + h_new
                heapq.heappush(heap, (f_new, g_new, next_state, path + [move]))
    return None
