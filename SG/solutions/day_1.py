from pathlib import Path


class CalibrationUnscrambler:
    number_string_lookup = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    def __init__(self, calibration_file: str) -> None:
        self.calibration_file = Path(calibration_file)

    def unscramble_calibration_file(
        self,
        output_file: str,
        convert_number_strings: bool = False,
        generate_output: bool = True,
    ):
        output_lines = []
        output_path = Path(output_file)

        with open(self.calibration_file, "r") as f:
            for calibration_line in f.readlines():
                if convert_number_strings:
                    for k, v in self.number_string_lookup.items():
                        calibration_line = calibration_line.replace(
                            k, f"{k[0]}{v}{k[-1]}"
                        )  # prevents replacing parts of other numbers

                first_num = last_num = None

                # First number
                for char in calibration_line:
                    if char.isdigit():
                        first_num = char
                        break
                else:
                    continue  # no numbers found

                # Last number
                for char in calibration_line[::-1]:
                    if char.isdigit():
                        last_num = char
                        break
                else:
                    continue  # no numbers found

                output_lines.append(f"{first_num}{last_num}\n")

        if generate_output:
            with open(output_path, "w") as o:
                o.writelines(output_lines)

        return sum(int(l) for l in output_lines)


def main(input_dir="../input", output_dir="../output", create_output=True):
    unscrambler = CalibrationUnscrambler(Path(input_dir) / "day_1_input.txt")
    sol = unscrambler.unscramble_calibration_file(
        Path(output_dir) / "day_1_output_p1.txt", False, create_output
    )
    print(sol)
    sol2 = unscrambler.unscramble_calibration_file(
        Path(output_dir) / "day_1_output_p2.txt", True, create_output
    )
    print(sol2)


if __name__ == "__main__":
    main()
