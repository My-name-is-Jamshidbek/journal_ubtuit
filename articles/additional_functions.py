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


def get_last_quarter_dates():
    # Get current date
    today = timezone.now()

    # Determine the current quarter
    quarter = (today.month - 1) // 3 + 1

    # Calculate the start and end dates of the last quarter
    last_quarter_start = datetime(today.year, ((quarter - 2) % 4) * 3 + 1, 1)
    last_quarter_end = last_quarter_start.replace(month=last_quarter_start.month + 3) - timedelta(days=1)

    return last_quarter_start, last_quarter_end