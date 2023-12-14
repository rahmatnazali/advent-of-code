from utilities import get_lines_from_file


max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def get_game_id(string: str):
    return int(string.split()[1])


def validate_cube(string: str) -> bool:
    cube_count, color = string.split()
    if max_cubes[color] < int(cube_count):
        return False
    return True


def validate_set(string: str) -> bool:
    cubes = [e.strip() for e in string.split(',')]
    for cube in cubes:
        is_cube_valid = validate_cube(cube)
        if not is_cube_valid:
            return False
    return True


def validate_game(string: str) -> bool:
    game_sets = [e.strip() for e in string.split(';')]
    for game_set in game_sets:
        is_set_valid = validate_set(game_set)
        if not is_set_valid:
            return False
    return True


if __name__ == "__main__":
    sum_of_valid_game_ids = 0
    input_lines = get_lines_from_file()
    for input_line in input_lines:
        game_string, set_string = [e.strip() for e in input_line.split(':')]
        game_id = get_game_id(game_string)

        is_game_valid = validate_game(set_string)
        if is_game_valid:
            sum_of_valid_game_ids += game_id

    print(sum_of_valid_game_ids)
    # 2685
