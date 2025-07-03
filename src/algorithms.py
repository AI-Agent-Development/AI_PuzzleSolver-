from collections import deque
import heapq
from typing import List, Tuple, Optional
from puzzle import EightPuzzle
from utils import manhattan_distance

def bfs(start: EightPuzzle) -> Tuple[Optional[List[str]], int]:
    visited = set()
    queue = deque([(start, [])])
    nodes_explored = 0

    while queue:
        current_state, path = queue.popleft()
        nodes_explored += 1

        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state.is_goal():
            return path, nodes_explored

        for move, next_state in current_state.get_successors():
            if next_state not in visited:
                queue.append((next_state, path + [move]))

    return None, nodes_explored
def a_star(start: EightPuzzle) -> Tuple[Optional[List[str]], int]:
    visited = set()
    heap = []
    heapq.heappush(heap, (manhattan_distance(start.board), 0, start, []))
    nodes_explored = 0

    while heap:
        f, g, current_state, path = heapq.heappop(heap)
        nodes_explored += 1

        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state.is_goal():
            return path, nodes_explored

        for move, next_state in current_state.get_successors():
            if next_state not in visited:
                g_new = g + 1
                h_new = manhattan_distance(next_state.board)
                f_new = g_new + h_new
                heapq.heappush(heap, (f_new, g_new, next_state, path + [move]))

    return None, nodes_explored
