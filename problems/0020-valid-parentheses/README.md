# 20. Valid Parentheses

## Problem

Given a string containing only `()[]{}`, determine whether every opening bracket is closed by the same bracket type and in the correct order.

## Intuition

A valid bracket string closes brackets in the reverse order in which they were opened.

In `([])`, `[` is opened after `(`, so `]` must close before `)`. This follows the **Last In, First Out (LIFO)** rule, making a stack suitable.

## Approach

1. Map each closing bracket to the opening bracket it expects.
2. Create an empty stack.
3. Traverse every character:
   - An opening bracket is appended to the stack.
   - A closing bracket must match the most recent opening bracket at `stack[-1]`.
4. Reject a closing bracket if the stack is empty or the types do not match.
5. Pop a confirmed matching opening bracket.
6. The string is valid only if the stack is empty at the end.

## Dry Run

For `([])`:

| Character | Action | Stack |
|---|---|---|
| `(` | Push | `['(']` |
| `[` | Push | `['(', '[']` |
| `]` | Matches `[`: pop | `['(']` |
| `)` | Matches `(`: pop | `[]` |

For `([)]`, `)` expects `(`, but the most recent opening bracket is `[`. The string is therefore invalid.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Solution

```python
def valid_parentheses(value: str) -> bool:
    matching_open = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []

    for character in value:
        if character not in matching_open:
            stack.append(character)
        else:
            if not stack:
                return False
            if matching_open[character] != stack[-1]:
                return False
            stack.pop()

    return not stack
```

See [solution.py](solution.py) for executable code.

## Key Python Operations

- `stack.append(character)` pushes an opening bracket.
- `stack[-1]` reads the most recent opening bracket.
- `matching_open[character]` returns the opening bracket expected by a closing bracket.
- `stack.pop()` removes a successfully matched opening bracket.
- `not stack` is `True` only when the stack is empty.

