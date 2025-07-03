from typing import List, Tuple

def count_inversions(arr: List[int]) -> int:
    arr = [x for x in arr if x != 0]
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

def is_solvable(start: List[int], goal: List[int]) -> bool:
    return count_inversions(start) % 2 == count_inversions(goal) % 2

def manhattan_distance(current: Tuple[int], goal: Tuple[int] = (1, 2, 3, 4, 5, 6, 7, 8, 0)) -> int:
    total = 0
    for index, tile in enumerate(current):
        if tile == 0:
            continue
        goal_index = goal.index(tile)
        current_row, current_col = divmod(index, 3)
        goal_row, goal_col = divmod(goal_index, 3)
        total += abs(current_row - goal_row) + abs(current_col - goal_col)
    return total

def render_puzzle_grid(board: List[int]) -> str:
    grid = ""
    for row in range(3):
        row_vals = []
        for col in range(3):
            num = board[row * 3 + col]
            display = str(num) if num != 0 else ""
            row_vals.append(
                f"<td style='text-align:center; font-size:24px; width:50px; height:50px; "
                f"border:1px solid #ccc; vertical-align:middle'>{display}</td>"
            )
        grid += f"<tr>{''.join(row_vals)}</tr>"

    return f"<table style='border-collapse:collapse; margin-top:5px'>{grid}</table>"

def displayResultInGrid(st, moves: List[str], current) -> None:
    original = current
    move_sequence = []
    for i in range(0, len(moves), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(moves):
                move = moves[i + j]
                current = current.move(move)
                move_sequence.append(move)
                label = f"S {i + j + 1}: {move}"
                html_grid = render_puzzle_grid(current.board)
                html = f"""
                <div style="
                    max-width: 100%;
                    width: 180px;
                    margin: 0 auto;
                    text-align: center;
                    box-sizing: border-box;
                ">
                    <div style="font-weight: bold; margin-bottom: 5px; white-space: nowrap; overflow-wrap: break-word;">
                        {label}
                    </div>
                    {html_grid}
                </div>
                """
                cols[j].write(html, unsafe_allow_html=True)
    # Show the moves at the end
    move_str = " > ".join(move_sequence)
    st.markdown(f"**Moves:** {move_str}")
