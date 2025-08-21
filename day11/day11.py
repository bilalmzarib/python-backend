
import re
from datetime import datetime
import pytz

text = "Contact me at 987-654-3210 or 123-456-7890."
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print("Phone Numbers Found:", phones)


sentence = "Python is created by Guido van Rossum."
cap_words = re.findall(r'\b[A-Z][a-z]*\b', sentence)
print("Capitalized Words:", cap_words)




now = datetime.now()
print("Current Local Time:", now.strftime("%Y-%m-%d %H:%M:%S"))


date_str = "2025-08-19 15:30"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
print("Parsed DateTime:", parsed_date)


formatted = parsed_date.strftime("%B %d, %Y at %I:%M %p")
print("Formatted DateTime:", formatted)




utc = pytz.utc
india = pytz.timezone('Asia/Kolkata')
ny = pytz.timezone('America/New_York')
tokyo = pytz.timezone('Asia/Tokyo')


now_utc = datetime.now(utc)
time_india = now_utc.astimezone(india)
time_ny = now_utc.astimezone(ny)
time_tokyo = now_utc.astimezone(tokyo)

print("Current Time in India:", time_india.strftime("%Y-%m-%d %H:%M:%S"))
print("Current Time in New York:", time_ny.strftime("%Y-%m-%d %H:%M:%S"))
print("Current Time in Tokyo:", time_tokyo.strftime("%Y-%m-%d %H:%M:%S"))

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

emails = [
    "user@example.com",
    "invalid-email@",
    "belal.mza123@gmail.com",
    "bad@domain",
    "hello@openai.com"
]

print("\nValidating Emails:")
for email in emails:
    result = "Valid" if validate_email(email) else "Invalid"
    print(f"{email} --> {result}")


def show_timezones():
    zones = ['UTC', 'Asia/Kolkata', 'Europe/London', 'America/Los_Angeles', 'Australia/Sydney']
    now = datetime.now(pytz.utc)
    print("\nCurrent Time in Various Timezones:")
    for zone in zones:
        tz = pytz.timezone(zone)
        local_time = now.astimezone(tz)
        print(f"{zone}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

show_timezones()
