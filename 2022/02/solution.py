from utilities import get_lines_from_file


map_choice = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def decide_shape_score(mine: str) -> int:
    if mine == 'X':
        return 1
    elif mine == 'Y':
        return 2
    elif mine == 'Z':
        return 3
    else:
        raise ValueError(f'Invalid parameter 2: {mine}')


def decide_outcome_score(theirs: str, mine: str) -> int:
    theirs = map_choice[theirs]
    mine = map_choice[mine]

    if theirs == mine:
        return 3
    elif mine - theirs == 1 or mine - theirs == -2:
        return 6
    else:
        return 0


def calculate_score(theirs: str, mine: str) -> int:
    print(theirs, mine)
    shape_score = map_choice[mine]
    outcome_score = decide_outcome_score(theirs, mine)
    print(shape_score, outcome_score)

    return shape_score + outcome_score


if __name__ == '__main__':
    raw_lines = get_lines_from_file()

    total_scores = 0
    for single_round in raw_lines:
        total_scores += calculate_score(*single_round.split())
        print()

    print(total_scores)
    # 12794
