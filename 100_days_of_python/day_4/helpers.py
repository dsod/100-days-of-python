from typing import Callable, List
from functools import wraps
import time
import random


def random_number_factory(numer_of_elements: int) -> List:
    return [random.randrange(100, 1000000) for _ in range(numer_of_elements)]


def timer(num_of_times: int) -> Callable:
    """A helper decorator to calculate runtime of a function num_of_times"""

    def wrapper_timer(func: Callable) -> Callable:
        @wraps(func)
        def wrapped_timer(*args, **kwargs):
            start_time = time.perf_counter()
            for _ in range(num_of_times):
                result = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(
                f"Finished {func.__name__!r} with {type(args[1])} in {run_time:.4f} secs"
            )
            return result

        return wrapped_timer

    return wrapper_timer
