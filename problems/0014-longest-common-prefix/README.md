# 14. Longest Common Prefix

## Problem

Given an array of strings, return the longest prefix shared by every string. Return an empty string when no common prefix exists.

## Intuition

The longest possible answer cannot be longer than the first string. Use the first string as the reference and compare every character position against the remaining words.

The first mismatch determines the end of the common prefix.

## Approach

1. Return `""` if the input list is empty.
2. Use the first word as the reference.
3. Traverse each character position in the reference.
4. For every remaining word, check:
   - Whether that position exists.
   - Whether its character equals the reference character.
5. On the first failure, return the reference slice before that index.
6. If every comparison succeeds, return the whole reference word.

## Dry Run

For `['flower', 'flow', 'flight']`:

| Index | Reference character | Comparison | Result |
|---:|---|---|---|
| 0 | `f` | Present in every word | Continue |
| 1 | `l` | Present in every word | Continue |
| 2 | `o` | `flight[2]` is `i` | Return `fl` |

## Complexity

- Time: `O(S)`, where `S` is the total number of characters inspected
- Space: `O(1)` auxiliary space, excluding the returned substring

## Solution

```python
def longest_common_prefix(words: list[str]) -> str:
    if not words:
        return ""

    reference = words[0]

    for index in range(len(reference)):
        for word in words[1:]:
            if index >= len(word) or word[index] != reference[index]:
                return reference[:index]

    return reference
```

See [solution.py](solution.py) for executable code.

