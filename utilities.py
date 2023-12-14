from typing import List


def get_lines_from_input(filename: str = 'input', strip: bool = True) -> List[str]:
    with open(filename) as input_file:
        raw_lines: List[str] = input_file.readlines()

    if strip:
        return [line.strip() for line in raw_lines]
    else:
        return raw_lines
