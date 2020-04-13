"""
A Pomodoro Timer and a interface the use it.
"""
import threading
from datetime import datetime, timedelta
from time import sleep
from typing import Any

import colorama

colorama.init()


class PomodoroTimer:
    def __init__(self, timer_length: timedelta = timedelta(minutes=25)) -> None:
        self.timer = timer_length
        self.timer_is_running = False

    @property
    def timer(self) -> timedelta:
        return self.__timer

    @timer.setter
    def timer(self, timer_value: timedelta) -> None:
        self.__timer = timer_value
        self.hours = self.timer.seconds // 60 // 60
        self.minutes = self.timer.seconds // 60 % 60
        self.seconds = self.timer.seconds % 60

    def run_timer(self) -> None:
        while self.timer_is_running:
            if self.timer.seconds == 0:
                print(colorama.Back.RED + "RRRRRRIIIINNGGG!!!" + colorama.Back.RESET)
                break
            print(colorama.Fore.WHITE + f"{self.hours}:{self.minutes}:{self.seconds}")
            self.timer = timedelta(seconds=self.timer.seconds - 1)
            sleep(1)


def main() -> None:
    timer_length = timedelta(seconds=10)
    timer = PomodoroTimer(timer_length)
    thread = threading.Thread(target=timer.run_timer, daemon=True)
    print(
        colorama.Fore.RED + 'Start timer with "s"',
        'Pause with "p"',
        'Reset with "r"',
        'Exit with "x"',
        f'Set timer length with "l" (Default: {timer_length})',
        sep="\n",
    )
    while True:
        command = input()
        if command == "s":
            print(colorama.Fore.GREEN + "Starting...")
            timer.timer_is_running = True

            # Edge case handling where user input reveral 's' commands in a row
            if not thread.is_alive():
                try:
                    thread.start()
                except RuntimeError:  # Previous thread was used up. Create a new one.
                    thread = threading.Thread(target=timer.run_timer, daemon=True)
                    thread.start()

        elif command == "p":
            print(colorama.Fore.YELLOW + "Pausing...")
            timer.timer_is_running = False

        elif command == "r":
            print(colorama.Fore.BLUE + "Resetting...")
            timer.timer_is_running = False
            timer = PomodoroTimer(timer_length)

        elif command == "x":
            print(colorama.Fore.CYAN + "Exiting...")
            if thread.is_alive():
                thread.join(timeout=0.001)
            break

        elif command == "l":
            new_timer_length: Any
            try:
                new_timer_length = input(
                    colorama.Fore.CYAN
                    + "Enter the timer length (hours:minutes:seconds): "
                )
                new_timer_length = new_timer_length.strip().split(":")
                new_timer_length = [int(v) for v in new_timer_length]

            except ValueError:
                print("Incorrect input.")

            timer_length = timedelta(
                hours=new_timer_length[0],
                minutes=new_timer_length[1],
                seconds=new_timer_length[2],
            )

            print(colorama.Fore.BLUE + "Resetting...")
            timer.timer_is_running = False
            timer = PomodoroTimer(timer_length)
            print(
                colorama.Fore.BLUE
                + f"The new timer are set to {timer.hours}:{timer.minutes}:{timer.seconds}..."
            )

        else:
            print(
                colorama.Fore.RED
                + "I did not understand that command. Please type in a correct command (s, p, r, x or l)."
            )


if __name__ == "__main__":
    main()
