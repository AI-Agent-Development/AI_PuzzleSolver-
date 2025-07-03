from collections import deque
import heapq
import time
from typing import List, Tuple, Optional
from puzzle import EightPuzzle
from utils import manhattan_distance

def bfs(start: EightPuzzle) -> Tuple[Optional[List[str]], int, float]:
    visited = set()
    queue = deque([(start, [])])
    nodes_explored = 0
    start_time = time.time()

    while queue:
        current_state, path = queue.popleft()
        nodes_explored += 1

        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state.is_goal():
            elapsed_time = time.time() - start_time
            return path, nodes_explored, elapsed_time

        for move, next_state in current_state.get_successors():
            if next_state not in visited:
                queue.append((next_state, path + [move]))

    elapsed_time = time.time() - start_time
    return None, nodes_explored, elapsed_time


def a_star(start: EightPuzzle) -> Tuple[Optional[List[str]], int, float]:
    visited = set()
    heap = []
    heapq.heappush(heap, (manhattan_distance(start.board), 0, start, []))
    nodes_explored = 0
    start_time = time.time()

    while heap:
        f, g, current_state, path = heapq.heappop(heap)
        nodes_explored += 1

        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state.is_goal():
            elapsed_time = time.time() - start_time
            return path, nodes_explored, elapsed_time

        for move, next_state in current_state.get_successors():
            if next_state not in visited:
                g_new = g + 1
                h_new = manhattan_distance(next_state.board)
                f_new = g_new + h_new
                heapq.heappush(heap, (f_new, g_new, next_state, path + [move]))

    elapsed_time = time.time() - start_time
    return None, nodes_explored, elapsed_time
