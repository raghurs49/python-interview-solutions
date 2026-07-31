def longest_common_prefix(words: list[str]) -> str:
    """Return the longest prefix shared by every input word."""
    if not words:
        return ""

    reference = words[0]

    for index in range(len(reference)):
        for word in words[1:]:
            if index >= len(word) or word[index] != reference[index]:
                return reference[:index]

    return reference


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))

