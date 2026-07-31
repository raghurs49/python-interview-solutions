def roman_to_integer(roman: str) -> int:
    """Convert a valid Roman numeral into an integer."""
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


if __name__ == "__main__":
    print(roman_to_integer("MCMXCIV"))

