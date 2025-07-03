import streamlit as st
from puzzle import EightPuzzle
from utils import displayResultInGrid, is_solvable, render_puzzle_grid
from solver import solve_puzzle

def parse_input(input_text):
    try:
        nums = list(map(int, input_text.strip().split()))
        if len(nums) != 9 or set(nums) != set(range(0, 9)):
            return None
        return nums
    except:
        return None

def display_board(board):
    size = 3
    for i in range(0, 9, size):
        row = board[i:i+size]
        st.write(" | ".join(str(num) if num != 0 else "_" for num in row))

def main():
    st.set_page_config(page_title="8 Puzzle Solver", layout="wide")

    st.markdown(
        """
        <style>
        .element-container:has(> .stContainer) {
            min-height: 800px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("AI Puzzle Solver - 8 Puzzle")
    st.markdown("Enter the puzzle board using numbers 0–8 (use 0 for the blank space).")

    example = "1 2 3 4 0 5 6 7 8"
    puzzle_input = st.text_input("Puzzle Input (e.g., 1 2 3 4 0 5 6 7 8):", value=example)
    puzzle_goal_input = st.text_input("Puzzle Goal Input (e.g., 1 2 3 4 5 6 7 8 0):", value="1 2 3 4 5 6 7 8 0")

    if st.button("Solve Puzzle"):
        board = parse_input(puzzle_input)
        goal = parse_input(puzzle_goal_input)

        if goal is None:
            goal = list(range(1, 9)) + [0]

        if board is None:
            st.error("❌ Invalid input. Please enter numbers 0–8 without duplicates.")
            return

        title_col, board_col = st.columns([3, 2])
        with title_col:
            st.subheader("Initial State:")
        with board_col:
            current = EightPuzzle(board)
            html_grid = render_puzzle_grid(current.board)
            st.markdown(html_grid, unsafe_allow_html=True)

        if not is_solvable(board, goal):
            st.error("❌ This puzzle is not solvable based on inversion parity.")
            return

        st.info("Solving with both algorithms...")

        methods = [("A* Search", "a_star"), ("Breadth-First Search", "bfs")]
        results = {}

        for alg_name, method in methods:
            moves, explored = solve_puzzle(board, goal, method)
            results[alg_name] = (moves, explored)

        col1, col2 = st.columns(2)

        for col, (alg_name, (moves, explored)) in zip([col1, col2], results.items()):
            with col:
                with st.container():
                    st.subheader(f"{alg_name} Result")
                    if moves is None:
                        st.error("❌ No solution found.")
                    else:
                        st.success(f"✅ Solved in {len(moves)} moves!")
                        st.info(f"🔍 Nodes Explored: {explored}")
                        current = EightPuzzle(board)
                        displayResultInGrid(st, moves, current)

if __name__ == "__main__":
    main()
