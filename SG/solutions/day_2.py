from pathlib import Path
from math import prod


def solution(input_dir, output_dir):
    input_file = Path(input_dir) / "day_2_input.txt"
    target_set = {"red": 12, "green": 13, "blue": 14}
    possible_games = sum_power_min_sets = 0

    with open(input_file, "r") as f:
        for game in f.readlines():
            game_name, game_details = game.strip().split(": ")
            game_id = int(game_name.split(" ")[-1])
            is_possible_game = True  # p1
            min_set = {"red": 0, "blue": 0, "green": 0}  # p2

            for specific_game_set in game_details.split("; "):
                for specific_cube_set in specific_game_set.split(", "):
                    cube_num, cube_name = specific_cube_set.split(" ")

                    min_set[cube_name] = max(min_set[cube_name], int(cube_num))
                    if is_possible_game and (target_set[cube_name] < int(cube_num)):
                        is_possible_game = False

            if is_possible_game:
                possible_games += game_id
            sum_power_min_sets += prod(min_set.values())

    return possible_games, sum_power_min_sets


def main(input_dir="../input", output_dir="../output"):
    res1, res2 = solution(input_dir, output_dir)
    print(res1)
    print(res2)


if __name__ == "__main__":
    main()
