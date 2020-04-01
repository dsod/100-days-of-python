from datetime import date, datetime, timedelta

def count_days_to_christmas(compare_date: date = date.today()) -> int:
    """
    Returns the number of days until next christmas from 
    date.today() as default or the overridden date
    """
    christmas_this_year = date(compare_date.year, 12, 25)
    days_until_christmas: timedelta

    if compare_date > christmas_this_year:
        christmas_next_year = date(compare_date.year + 1, 12, 25)
        days_until_christmas = christmas_next_year - compare_date
        return days_until_christmas.days
    
    days_until_christmas = christmas_this_year - compare_date
    return days_until_christmas.days
