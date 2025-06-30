"""
PEAS Framework for 8-Puzzle AI Agent

This file defines the PEAS (Performance, Environment, Actuators, Sensors) description
of the 8-puzzle solving intelligent agent.
"""

def get_peas_framework() -> dict:
    """
    Returns the PEAS framework for the 8-puzzle problem.
    """
    peas = {
        "Performance Measure": [
            "Minimize the number of moves to reach the goal state",
            "Minimize computation time (execution efficiency)"
        ],
        "Environment": [
            "3x3 8-puzzle grid with tiles numbered 1 to 8 and a blank space (0)",
            "Initial state is user-defined; goal state is [1, 2, 3, 4, 5, 6, 7, 8, 0]"
        ],
        "Actuators": [
            "Tile mover that can move the blank tile: up, down, left, or right"
        ],
        "Sensors": [
            "Reads the initial puzzle configuration from the user",
            "Perceives the current puzzle state at each search step"
        ]
    }
    return peas


def display_peas_framework():
    """
    Prints the PEAS framework in a readable format.
    """
    peas = get_peas_framework()
    print("PEAS Framework for 8-Puzzle AI Agent\n")
    for category, details in peas.items():
        print(f"{category}:")
        for item in details:
            print(f"  - {item}")
        print()

if name == "main":
    display_peas_framework()