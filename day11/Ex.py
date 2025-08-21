import re
from datetime import datetime, timedelta
import pytz

def validate_email(email):
    pattern = r'^[\w.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
    return re.match(pattern, email) is not None

emails = ["user@example.com", "bad@domain", "hello@site.io", "john.doe@web-123.org", "invalid@site.c"]
print("Exercise 1: Email Validation")
for email in emails:
    print(f"{email} --> {'Valid' if validate_email(email) else 'Invalid'}")
print()


def extract_dates(text):
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)

sample_text = "Important dates: 01-01-2025, 15/08/2024, and invalid 32-13-2023."
dates_found = extract_dates(sample_text)
print("Exercise 2: Extracted Dates")
print(dates_found)
print()


def time_until_birthday():
    bday_input = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(bday_input, "%Y-%m-%d")
        today = datetime.now()
        this_year_bday = birthdate.replace(year=today.year)

        if this_year_bday < today:
            next_birthday = this_year_bday.replace(year=today.year + 1)
        else:
            next_birthday = this_year_bday

        delta = next_birthday - today
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes = remainder // 60

        print("Exercise 3: Time Until Next Birthday")
        print(f"{days} days, {hours} hours, and {minutes} minutes remaining.")
        print()
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD format.")
        print()

def convert_timezone(time_str, from_tz, to_tz):
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)

    naive_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    from_time = from_zone.localize(naive_time)
    to_time = from_time.astimezone(to_zone)

    return to_time.strftime("%Y-%m-%d %H:%M:%S")

converted = convert_timezone("2025-08-19 14:30:00", "US/Eastern", "UTC")
print("Exercise 4: Timezone Conversion")
print("Converted Time:", converted)
print()


def parse_log_timestamps(log):
    pattern = r'\[(\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\]'
    matches = re.findall(pattern, log)
    formatted_times = []
    for ts in matches:
        dt = datetime.strptime(ts, "%d/%b/%Y:%H:%M:%S")
        dt_utc = dt.replace(tzinfo=pytz.utc)
        formatted_times.append(dt_utc.strftime("%Y-%m-%d %H:%M:%S"))
    return formatted_times

log_data = """
127.0.0.1 - - [19/Aug/2025:13:45:30 +0000] "GET /index.html HTTP/1.1" 200 1024
127.0.0.1 - - [20/Aug/2025:15:22:10 +0000] "POST /submit HTTP/1.1" 200 512
"""

parsed_timestamps = parse_log_timestamps(log_data)
print("Exercise 5: Parsed Log Timestamps")
for ts in parsed_timestamps:
    print(ts)
