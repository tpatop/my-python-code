from calendar import monthrange
from datetime import date, timedelta


def get_all_mondays(year: int):
    first_day = monthrange(year, 1)
    diff = (7 - first_day[0]) % 7
    first_list = [date(year, 1, 1 + diff) + timedelta(days=7 * x) for x in range(52)]
    if first_list[-1].year != year:
        first_list = first_list[:-1]
    return first_list


print(get_all_mondays(2018))