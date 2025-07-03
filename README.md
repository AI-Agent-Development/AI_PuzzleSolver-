# AI Puzzle Solver

An AI-powered solver for the classic 8-puzzle problem, implementing search algorithms and providing an interactive Streamlit interface.

## Project Structure

- src/: Contains all the source code modules related to the puzzle solver project.
- docs/: Contains project documentation and report PDFs.
- test/: Holds unit tests to validate solver functionality.
- requirements.txt: Lists the Python libraries your project depends on.
- README.md: Provides a project overview, setup instructions, and usage.


## Setup Instructions

1. **Clone the repository:**

  ```bash
   git clone <https://github.com/AI-Agent-Development/AI_PuzzleSolver->
   cd <AI_PuzzleSolver->

2. **Create and activate a virtual environment (recommended):**

  ```bash
   python -m venv venv
   source venv/bin/activate 
   venv\Scripts\activate    

3. **Install dependencies:**

  ```bash
   pip install -r requirements.txt
    
## Usage

 ### Run the Streamlit UI

  To start the interactive puzzle solver web app, use the following command:

  ```bash
   streamlit run src/streamlit.py

## Run the Tests


  To verify that the puzzle solver works correctly, you can run the unit tests using the following command:

   ```bash
   python -m unittest discover -s test


## Features
  
 - Supports multiple search algorithms (A*, BFS) for solving the 8-puzzle.
 - Validates puzzle solvability before solving.
 - Visualizes puzzle state transitions and solution paths.
 - Interactive interface built with Streamlit.
 - PEAS framework implementation for formal AI agent structure.
 - Well-organized and modular code structure.
 - Unit testing support for core components.

## PEAS Framework

- Performance Measure: Solves puzzle in minimum moves, efficiency (nodes explored).
- Environment: 3x3 grid with numbered tiles and one blank.
- Actuators: Move the blank tile up, down, left, or right.
- Sensors: Current state of the puzzle board.

## Dependencies

See requirements.txt for all required Python packages.
streamlit

```bash
  pip install -r requirements.txt


## Project Report

  For full documentation and analysis, refer to:
  docs/AI_puzzle_solver.pdf

## Contribution

- Contributions are welcome! To contribute:
- Fork the repository
- Create a feature branch (git checkout -b feature-name)
- Commit changes (git commit -am 'Add feature')
- Push to the branch (git push origin feature-name)
- Create a Pull Request