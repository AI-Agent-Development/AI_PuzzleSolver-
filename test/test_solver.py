import unittest
from src.puzzle import EightPuzzle
from src.algorithms import bfs, a_star

class TestPuzzleSolvers(unittest.TestCase):
    def test_solved_puzzle(self):
        start = EightPuzzle([1, 2, 3, 4, 5, 6, 7, 8, 0])
        bfs_path, bfs_nodes = bfs(start)
        a_star_path, a_star_nodes = a_star(start)

        self.assertEqual(bfs_path, [])
        self.assertEqual(a_star_path, [])
        self.assertEqual(bfs_nodes, 1)
        self.assertEqual(a_star_nodes, 1)

    def test_easy_puzzle(self):
        start = EightPuzzle([1, 2, 3, 4, 5, 6, 7, 0, 8])
        bfs_path, _ = bfs(start)
        a_star_path, _ = a_star(start)

        self.assertEqual(bfs_path, ['right'])
        self.assertEqual(a_star_path, ['right'])

    def test_medium_puzzle(self):
        start = EightPuzzle([1, 2, 3, 4, 5, 6, 0, 7, 8])
        bfs_path, bfs_nodes = bfs(start)
        a_star_path, a_star_nodes = a_star(start)

        self.assertEqual(len(bfs_path), len(a_star_path))
        self.assertLessEqual(a_star_nodes, bfs_nodes)

    def test_unsolvable_puzzle(self):
        start = EightPuzzle([1, 2, 3, 4, 5, 6, 8, 7, 0])
        bfs_path, _ = bfs(start)
        a_star_path, _ = a_star(start)

        self.assertIsNone(bfs_path)
        self.assertIsNone(a_star_path)

if __name__ == '__main__':
    unittest.main()
