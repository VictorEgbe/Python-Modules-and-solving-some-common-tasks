# Number of days in a month. First value placeholder value for indexing

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Returns True for a leap, False for a non-leap year. """

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def day_in_month(year, month):
    """Returns number of days in that month in that year."""

    if not 1 <= month <= 12:
        return f'Month {month} is an Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(day_in_month(1992, 20))
