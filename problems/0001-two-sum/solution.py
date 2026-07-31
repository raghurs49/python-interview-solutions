def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the indices of two distinct values that sum to target."""
    seen: dict[int, int] = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))

