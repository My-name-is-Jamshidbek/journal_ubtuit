from datetime import datetime, timedelta
import pytz
from django.utils import timezone

def get_current_quarter():
    # Get current date
    today = timezone.now()

    # Determine the current quarter
    quarter = (today.month - 1) // 3 + 1

    timezone_utc5 = pytz.timezone('Asia/Tashkent')
    # Calculate the start and end dates of the current quarter
    quarter_start = timezone.datetime(today.year, (quarter - 1) * 3 + 1, 1, tzinfo=pytz.UTC).astimezone(timezone_utc5)
    quarter_end = quarter_start.replace(month=quarter_start.month + 3) - timezone.timedelta(days=1)

    return quarter_start, quarter_end


from datetime import datetime, timedelta
from django.utils import timezone

def get_last_quarter_dates():
    # Get the current date and time
    today = timezone.now()

    # Determine the current quarter
    quarter = (today.month - 1) // 3 + 1

    # Calculate the year and month of the start of the last quarter
    if quarter == 1:
        # If the current quarter is Q1, the last quarter is Q4 of the previous year
        last_quarter_year = today.year - 1
        last_quarter_start_month = 10  # October
    else:
        # Otherwise, it's the previous quarter in the current year
        last_quarter_year = today.year
        last_quarter_start_month = (quarter - 2) * 3 + 1

    # Calculate the start date of the last quarter
    last_quarter_start = datetime(last_quarter_year, last_quarter_start_month, 1)

    # Calculate the end date of the last quarter
    # Safely handle the month wrap-around using modular arithmetic
    if last_quarter_start_month + 3 > 12:
        # If adding 3 months exceeds December, move to the next year
        next_quarter_start_month = (last_quarter_start_month + 3) % 12
        next_quarter_start_year = last_quarter_year + 1
    else:
        # Otherwise, stay in the same year
        next_quarter_start_month = last_quarter_start_month + 3
        next_quarter_start_year = last_quarter_year

    next_quarter_start = datetime(next_quarter_start_year, next_quarter_start_month, 1)
    last_quarter_end = next_quarter_start - timedelta(days=1)

    return last_quarter_start, last_quarter_end
