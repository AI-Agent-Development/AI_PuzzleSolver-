from typing import List, Tuple

def count_inversions(arr: List[int]) -> int:
    """Count inversions in the puzzle board (excluding 0)."""
    arr = [x for x in arr if x != 0]
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

def is_solvable(start: List[int], goal: List[int]) -> bool:
    """Check if an 8-puzzle is solvable from start to goal configuration."""
    return count_inversions(start) % 2 == count_inversions(goal) % 2

def manhattan_distance(current: Tuple[int], goal: Tuple[int] = (1, 2, 3, 4, 5, 6, 7, 8, 0)) -> int:
    """Compute the Manhattan distance between current state and goal."""
    total = 0
    for index, tile in enumerate(current):
        if tile == 0:
            continue
        goal_index = goal.index(tile)
        current_row, current_col = divmod(index, 3)
        goal_row, goal_col = divmod(goal_index, 3)
        total += abs(current_row - goal_row) + abs(current_col - goal_col)
    return total


def displayResultInGrid(st, moves, current):
    for i in range(0, len(moves), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(moves):
                move = moves[i + j]
                current = current.move(move)
                cols[j].markdown(f"**Step {i + j + 1}: {move}**")
                        # Display as a compact 3x3 grid
                grid = ""
                for row in range(3):
                    row_vals = []
                    for col in range(3):
                        num = current.board[row * 3 + col]
                        display = str(num) if num != 0 else ""
                        row_vals.append(f"<td style='text-align:center; font-size:20px'>{display}</td>")
                    grid += f"<tr>{''.join(row_vals)}</tr>"
                cols[j].write(f"<table>{grid}</table>", unsafe_allow_html=True)
