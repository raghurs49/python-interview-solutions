def valid_parentheses(value: str) -> bool:
    """Return whether all brackets are correctly matched and nested."""
    matching_open = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack: list[str] = []

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


if __name__ == "__main__":
    for example in ["()", "()[]{}", "(]", "([])", "([)]"]:
        print(example, valid_parentheses(example))

