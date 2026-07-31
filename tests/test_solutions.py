import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_solution(folder: str):
    path = ROOT / "problems" / folder / "solution.py"
    spec = importlib.util.spec_from_file_location(folder.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class SolutionTests(unittest.TestCase):
    def test_two_sum(self):
        module = load_solution("0001-two-sum")
        self.assertEqual(module.two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(module.two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(module.two_sum([3, 3], 6), [0, 1])

    def test_roman_to_integer(self):
        module = load_solution("0013-roman-to-integer")
        self.assertEqual(module.roman_to_integer("III"), 3)
        self.assertEqual(module.roman_to_integer("LVIII"), 58)
        self.assertEqual(module.roman_to_integer("MCMXCIV"), 1994)

    def test_longest_common_prefix(self):
        module = load_solution("0014-longest-common-prefix")
        self.assertEqual(module.longest_common_prefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(module.longest_common_prefix(["dog", "racecar", "car"]), "")
        self.assertEqual(module.longest_common_prefix(["alone"]), "alone")

    def test_valid_parentheses(self):
        module = load_solution("0020-valid-parentheses")
        self.assertTrue(module.valid_parentheses("()"))
        self.assertTrue(module.valid_parentheses("()[]{}"))
        self.assertTrue(module.valid_parentheses("([])"))
        self.assertFalse(module.valid_parentheses("(]"))
        self.assertFalse(module.valid_parentheses("([)]"))
        self.assertFalse(module.valid_parentheses("]"))
        self.assertFalse(module.valid_parentheses("(("))


if __name__ == "__main__":
    unittest.main()

