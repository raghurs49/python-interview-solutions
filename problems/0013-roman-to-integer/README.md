# 13. Roman to Integer

## Problem

Convert a valid Roman numeral into an integer.

| Symbol | Value |
|---|---:|
| `I` | 1 |
| `V` | 5 |
| `X` | 10 |
| `L` | 50 |
| `C` | 100 |
| `D` | 500 |
| `M` | 1000 |

A smaller symbol immediately before a larger symbol is subtracted. Otherwise, it is added.

## Intuition

Each symbol's contribution can be decided by comparing it with the next symbol:

- Current value smaller than the next value: subtract it.
- Otherwise: add it.

The final symbol has no following symbol, so it is always added.

## Approach

1. Store Roman-symbol values in a dictionary.
2. Traverse all symbols except the final one.
3. Compare the current value with the next value.
4. Subtract the current value when it is smaller; otherwise add it.
5. Add the final symbol after the loop.

## Dry Run

For `MCMXCIV`:

| Current | Next | Operation | Total |
|---|---|---|---:|
| `M` = 1000 | `C` = 100 | Add 1000 | 1000 |
| `C` = 100 | `M` = 1000 | Subtract 100 | 900 |
| `M` = 1000 | `X` = 10 | Add 1000 | 1900 |
| `X` = 10 | `C` = 100 | Subtract 10 | 1890 |
| `C` = 100 | `I` = 1 | Add 100 | 1990 |
| `I` = 1 | `V` = 5 | Subtract 1 | 1989 |
| `V` = 5 | — | Add 5 | 1994 |

## Complexity

- Time: `O(n)`
- Space: `O(1)` because the symbol dictionary has a fixed size

## Solution

```python
def roman_to_integer(roman: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0

    for index in range(len(roman) - 1):
        current_value = values[roman[index]]
        next_value = values[roman[index + 1]]

        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    return result + values[roman[-1]]
```

See [solution.py](solution.py) for executable code.

