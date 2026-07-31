# Python Interview Solutions

A growing collection of Python interview problems explained from first principles.

Each solution includes:

- The original problem contract
- Intuition and pattern recognition
- A step-by-step approach
- Complexity analysis
- A worked dry run
- Clean, executable Python
- Focused test cases

The purpose of this repository is not to claim novel algorithms. It documents how I understand, explain, implement, and test common interview patterns.

## Problem Index

| # | Problem | Pattern | Difficulty | Time | Space |
|---:|---|---|---|---|---|
| 1 | [Two Sum](problems/0001-two-sum/README.md) | Hash map | Easy | `O(n)` | `O(n)` |
| 13 | [Roman to Integer](problems/0013-roman-to-integer/README.md) | Hash map and scan | Easy | `O(n)` | `O(1)` |
| 14 | [Longest Common Prefix](problems/0014-longest-common-prefix/README.md) | String scanning | Easy | `O(S)` | `O(1)` |
| 20 | [Valid Parentheses](problems/0020-valid-parentheses/README.md) | Stack | Easy | `O(n)` | `O(n)` |

`S` is the total number of characters inspected across all input strings.

## Run the Tests

The repository uses only Python's standard library.

```bash
python3 -m unittest discover -s tests -v
```

## Repository Structure

```text
python-interview-solutions/
├── problems/
│   ├── 0001-two-sum/
│   ├── 0013-roman-to-integer/
│   ├── 0014-longest-common-prefix/
│   └── 0020-valid-parentheses/
├── tests/
└── README.md
```

## Learning Method

For every problem, I follow the same sequence:

1. Restate the input and output.
2. Walk through a small example.
3. Describe a correct brute-force approach.
4. Identify repeated work or a useful ordering property.
5. Select the appropriate data structure.
6. Implement and test the optimized solution.
7. State time and auxiliary-space complexity.

## Disclaimer

Problem names and descriptions refer to common programming-interview exercises. Explanations and implementations in this repository are written for personal learning and interview preparation.

