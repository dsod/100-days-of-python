from datetime import timedelta
from time import sleep
from .day3 import PomodoroTimer
import threading


def test_pomodoro_timer() -> None:
    timer_length: timedelta = timedelta(seconds=5)
    timer = PomodoroTimer(timer_length)
    thread = threading.Thread(target=timer.run_timer, daemon=True)

    assert type(timer.timer) == timedelta
    assert type(timer.timer_is_running) == bool
    assert timer.timer.seconds == 5

    timer.timer_is_running = True

    thread.start()
    sleep(0.1)
    assert timer.timer.seconds == 4
    timer.timer_is_running = False

    sleep(1)
    assert timer.timer.seconds == 4

    thread = threading.Thread(target=timer.run_timer, daemon=True)
    timer.timer_is_running = True
    thread.start()
    sleep(5)
    assert timer.timer.seconds == 0
    assert not thread.is_alive()

