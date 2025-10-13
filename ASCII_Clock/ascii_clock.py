import time
from datetime import datetime


class ASCIIClock:
    def __init__(self):
        # ASCII representations of digits 0-9 (5 lines high)
        self.digits = {
            '0': [
                " ██████ ",
                "██    ██",
                "██    ██",
                "██    ██",
                " ██████ "
            ],
            '1': [
                "   ██   ",
                " ████   ",
                "   ██   ",
                "   ██   ",
                " ██████ "
            ],
            '2': [
                " ██████ ",
                "      ██",
                " ██████ ",
                "██      ",
                "████████"
            ],
            '3': [
                " ██████ ",
                "      ██",
                " ██████ ",
                "      ██",
                " ██████ "
            ],
            '4': [
                "██    ██",
                "██    ██",
                "████████",
                "      ██",
                "      ██"
            ],
            '5': [
                "████████",
                "██      ",
                "████████",
                "      ██",
                "████████"
            ],
            '6': [
                " ██████ ",
                "██      ",
                "████████",
                "██    ██",
                " ██████ "
            ],
            '7': [
                "████████",
                "      ██",
                "     ██ ",
                "    ██  ",
                "   ██   "
            ],
            '8': [
                " ██████ ",
                "██    ██",
                " ██████ ",
                "██    ██",
                " ██████ "
            ],
            '9': [
                " ██████ ",
                "██    ██",
                " ██████ ",
                "      ██",
                " ██████ "
            ]
        }

        # Colon separator for time
        self.colon = [
            "   ",
            " ██ ",
            "   ",
            " ██ ",
            "   "
        ]

        # Space between digits (reduced for better fit)
        self.space = [
            " ",
            " ",
            " ",
            " ",
            " "
        ]

    @staticmethod
    def get_current_time():
        """Get current time in HH:MM:SS format"""
        return datetime.now().strftime("%H:%M:%S")

    def display_bordered_clock(self):
        """Display the ASCII clock within a bordered box"""
        # Calculate the width needed for the time display
        current_time = self.get_current_time()
        time_lines = self._get_time_lines(current_time)
        max_line_width = max(len(line) for line in time_lines)
        box_width = max(60, max_line_width + 20)  # Ensure minimum width and padding

        print("╔" + "═" * box_width + "╗")
        print("║" + " " * ((box_width - 11) // 2) + "ASCII CLOCK" + " " * ((box_width - 11 + 1) // 2) + "║")
        print("╠" + "═" * box_width + "╣")
        print("║" + " " * box_width + "║")

        # Display the time (centered)
        for line in time_lines:
            padding = (box_width - len(line)) // 2
            extra_space = (box_width - len(line)) % 2
            print("║" + " " * padding + line + " " * (padding + extra_space) + "║")

        print("║" + " " * box_width + "║")
        print("╚" + "═" * box_width + "╝")

    def run_clock(self):
        """Run the live updating clock"""
        try:
            while True:
                self.display_bordered_clock()
                print("\nPress Ctrl+C to stop the clock")

                # Update every second
                time.sleep(1)

        except KeyboardInterrupt:
            print("ASCII Clock stopped. Thank you for using it!")

    def _get_time_lines(self, time_str):
        """Get the ASCII lines for the time string"""
        ascii_lines = [[] for _ in range(5)]

        for i, char in enumerate(time_str):
            if char == ':':
                for line_idx in range(5):
                    ascii_lines[line_idx].append(self.colon[line_idx])
            else:
                for line_idx in range(5):
                    ascii_lines[line_idx].append(self.digits[char][line_idx])

            if i < len(time_str) - 1:
                for line_idx in range(5):
                    ascii_lines[line_idx].append(self.space[line_idx][0])

        return [''.join(line) for line in ascii_lines]


def main():
    clock = ASCIIClock()
    clock.run_clock()


if __name__ == "__main__":
    main()
