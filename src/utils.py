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


def render_puzzle_grid(board):
    """Return HTML for a 3x3 puzzle grid given a flat board list."""
    grid = ""
    for row in range(3):
        row_vals = []
        for col in range(3):
            num = board[row * 3 + col]
            display = str(num) if num != 0 else ""
            row_vals.append(f"<td style='text-align:center; font-size:20px; width:30px; height:30px'>{display}</td>")
        grid += f"<tr>{''.join(row_vals)}</tr>"
    return f"<table>{grid}</table>"

def displayResultInGrid(st, moves, current):
    for i in range(0, len(moves), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(moves):
                move = moves[i + j]
                current = current.move(move)
                cols[j].markdown(f"**S {i + j + 1}: {move}**")
                # Use the extracted function to render the grid
                html_grid = render_puzzle_grid(current.board)
                cols[j].write(
                    f"<div style='display:inline-block; margin:15px 10px 30px 10px;'>{html_grid}</div>",
                    unsafe_allow_html=True
                )
