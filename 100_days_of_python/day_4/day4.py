"""
In this module i just played around some with the collections module.
"""
import functools
import random
import time
from collections import deque
from typing import Callable, Deque, Iterable, List, Union

from helpers import random_number_factory, timer


def main() -> None:
    test_list = random_number_factory(20000)
    test_deck = deque(test_list)

    increment_by_index(
        100, test_list
    )  # Finished 'increment_by_index' with <class 'list'> in 1.2271 secs
    increment_by_index(
        100, test_deck
    )  # Finished 'increment_by_index' with <class 'collections.deque'> in 2.5600 secs

    move_last_to_first(
        1000, test_list
    )  # Finished 'move_last_to_first' with <class 'list'> in 0.6422 secs
    move_last_to_first(
        1000, test_deck
    )  # Finished 'move_last_to_first' with <class 'collections.deque'> in 0.0164 secs

    test_list.sort()
    try:
        test_deck.sort()
    except AttributeError:
        print("Decks dont have a built-in method for sorting")

    test_list_to_add = random_number_factory(40000)
    test_deck_to_add = deque(test_list_to_add)

    extend_collection(
        test_list.copy(), test_list_to_add
    )  # Finished 'extend_collection' with <class 'list'> in 0.7809 secs
    extend_collection(
        test_deck.copy(), test_deck_to_add
    )  # Finished 'extend_collection' with <class 'collections.deque'> in 2.1560 secs

    extend_collection_by_appending(
        test_list.copy(), test_list_to_add
    )  # Finished 'extend_collection_by_appending' with <class 'list'> in 1.6643 secs
    extend_collection_by_appending(
        test_deck.copy(), test_deck_to_add
    )  # Finished 'extend_collection_by_appending' with <class 'collections.deque'> in 1.6432 secs

    first_300_list_elements = test_list[0:300]
    try:
        first_300_deck_elements = test_deck[0:300]
    except TypeError:
        print("Can't slice decks.")


@timer(num_of_times=1000)
def increment_by_index(num: int, collection: Union[List[int], Deque[int]]) -> None:
    for index, element in enumerate(collection):
        collection[index] = element + num


@timer(num_of_times=1000)
def move_last_to_first(num: int, collection: Union[List[int], Deque[int]]) -> None:
    for _ in range(num):
        element = collection.pop()
        if type(collection) == list:
            collection.insert(0, element)
        else:
            collection.appendleft(
                element
            )  # Very convenient to that the '...left' methods exist


@timer(num_of_times=10000)
def extend_collection(
    collection: Union[List[int], Deque[int]],
    collection_to_extend: Union[List[int], Deque[int]],
) -> None:
    collection.extend(collection_to_extend)


@timer(num_of_times=1000)
def extend_collection_by_appending(
    collection: Union[List[int], Deque[int]],
    collection_to_extend: Union[List[int], Deque[int]],
) -> None:
    for element in collection_to_extend:
        collection.append(element)


if __name__ == "__main__":
    main()
