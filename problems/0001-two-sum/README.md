# 1. Two Sum

## Problem

Given an integer array `nums` and an integer `target`, return the indices of two different elements whose values add up to `target`.

Assume exactly one valid answer exists.

## Intuition

For the current number `value`, the required second number is:

```text
complement = target - value
```

Instead of scanning the earlier elements again, store each previously seen value and its index in a dictionary. A dictionary gives an average `O(1)` lookup.

## Approach

1. Create an empty dictionary called `seen`.
2. Traverse the array with both the index and value.
3. Calculate the complement required by the current value.
4. If the complement is already in `seen`, return its saved index and the current index.
5. Otherwise, store the current value and index.

## Dry Run

For `nums = [2, 7, 11, 15]` and `target = 9`:

| Index | Value | Complement | Seen before step | Action |
|---:|---:|---:|---|---|
| 0 | 2 | 7 | `{}` | Store `2: 0` |
| 1 | 7 | 2 | `{2: 0}` | Return `[0, 1]` |

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Solution

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value

        if complement in seen:
            return [seen[complement], index]

        seen[value] = index

    return []
```

See [solution.py](solution.py) for executable code.

