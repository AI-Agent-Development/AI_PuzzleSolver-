import streamlit as st
from puzzle import EightPuzzle
from utils import is_solvable
from solver import solve_puzzle

def parse_input(input_text):
    try:
        nums = list(map(int, input_text.strip().split()))
        if len(nums) != 9 or set(nums) != set(range(9)):
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
    st.title("AI Puzzle Solver - 8 Puzzle")
    st.markdown("Enter the puzzle board using numbers 0–8 (use 0 for the blank space).")

    example = "1 2 3 4 0 5 6 7 8"
    puzzle_input = st.text_input("Puzzle Input (e.g., 1 2 3 4 0 5 6 7 8):", value=example)
    puzzle_goal_input = st.text_input("Puzzle Goal Input (e.g., 1 2 3 4 5 6 7 8 0):", value="1 2 3 4 5 6 7 8 0")

    algorithm = st.radio("Choose Algorithm", ["A* Search", "Breadth-First Search"])

    if st.button("Solve Puzzle"):
        board = parse_input(puzzle_input)
        goal = parse_input(puzzle_goal_input)

        if goal is None:
            goal = list(range(1, 9)) + [0]

        if board is None:
            st.error("❌ Invalid input. Please enter numbers 0–8 without duplicates.")
            return

        st.subheader("Initial State:")
        display_board(board)
        print("Initial Board:", board)

        if not is_solvable(board, goal):
            st.error("❌ This puzzle is not solvable based on inversion parity.")
            return

        method = "a_star" if algorithm == "A* Search" else "bfs"

        st.info("Solving...")
        moves = solve_puzzle(board, goal, method)

        if moves is None:
            st.error("❌ No solution found.")
        else:
            st.success(f"✅ Solved in {len(moves)} moves!")
            current = EightPuzzle(board)
            for i, move in enumerate(moves, 1):
                current = current.move(move)
                st.markdown(f"Step {i}: {move}")
                display_board(current.board)

if __name__ == "__main__":
    main()
