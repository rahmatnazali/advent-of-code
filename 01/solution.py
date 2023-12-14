from utilities import get_lines_from_file


def get_summable_digits(string_line: str) -> int:
    first_digit = None
    last_digit = None

    for character in string_line:
        if character.isnumeric():
            if first_digit is None:
                first_digit = character
            last_digit = character

    return int(f"{first_digit}{last_digit}")


if __name__ == "__main__":
    lines = get_lines_from_file()
    sum_of_digits = 0

    for line in lines:
        sum_of_digits += get_summable_digits(line)

    print(sum_of_digits)
    # 57346
