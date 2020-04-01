from datetime import date

from .day1 import count_days_to_christmas

def test_count_days_to_christmas() -> None:
    this_year = date.today().year

    middle_of_current_year = date(this_year, 6, 25)
    past_christmast_current_year = date(this_year, 12, 28)
    christmas_current_year = date(this_year, 12, 25)
    middle_of_future_year = date(this_year + 5, 6, 25)

    assert type(count_days_to_christmas()) is int
    assert count_days_to_christmas(middle_of_current_year) == 183
    assert count_days_to_christmas(past_christmast_current_year) == 362 or 363
    assert count_days_to_christmas(christmas_current_year) == 0
    assert count_days_to_christmas(middle_of_current_year) != 10
    assert count_days_to_christmas(middle_of_future_year) == 183
