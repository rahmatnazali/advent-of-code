from typing import List


def get_lines() -> List[str]:
    with open('input') as input_file:
        raw_lines: List[str] = input_file.readlines()

    return [line.strip() for line in raw_lines]


def get_summable_digits(line: str) -> int:
    first_digit = None
    last_digit = None

    for character in line:
        if character.isnumeric():
            if first_digit is None:
                first_digit = character
            last_digit = character

    return int(f"{first_digit}{last_digit}")


if __name__ == "__main__":
    lines = get_lines()
    sum_of_digits = 0

    for line in lines:
        sum_of_digits += get_summable_digits(line)

    print(sum_of_digits)
    # 57346
