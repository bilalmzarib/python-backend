import requests
import smtplib
import ssl
from email.message import EmailMessage

# Configuration
API_KEY = 'your_exchange_rate_api_key'  # Get from https://www.exchangerate-api.com/
FROM_CURRENCY = 'USD'
TO_CURRENCY = 'EUR'
AMOUNT = 100

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_app_password'
RECEIVER_EMAIL = 'receiver@example.com'

def convert_currency(amount, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")
    data = response.json()
    if data['result'] != 'success':
        raise Exception("API error: " + data.get('error-type', 'Unknown error'))
    rate = data['conversion_rates'].get(to_currency)
    if rate is None:
        raise Exception(f"Currency {to_currency} not found in API response")
    converted_amount = amount * rate
    return converted_amount, rate

def send_email(subject, body, receiver):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver
    msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)

def main():
    try:
        converted, rate = convert_currency(AMOUNT, FROM_CURRENCY, TO_CURRENCY)
        subject = f"Currency Conversion: {FROM_CURRENCY} to {TO_CURRENCY}"
        body = (f"{AMOUNT} {FROM_CURRENCY} equals {converted:.2f} {TO_CURRENCY}\n"
                f"Conversion rate used: 1 {FROM_CURRENCY} = {rate} {TO_CURRENCY}")
        send_email(subject, body, RECEIVER_EMAIL)
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
