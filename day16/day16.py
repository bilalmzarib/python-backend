import requests
import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime

# === CONFIGURATION ===
API_KEY = 'your_openweathermap_api_key'
CITY = 'London'

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_app_password'
RECEIVER_EMAIL = 'receiver_email@example.com'

def fetch_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch weather data: {response.status_code}")
    return response.json()

def generate_report(data):
    report = f"Weather Report for {data['name']} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += '-' * 40 + '\n'
    report += f"Temperature: {data['main']['temp']}°C\n"
    report += f"Weather: {data['weather'][0]['description'].title()}\n"
    report += f"Humidity: {data['main']['humidity']}%\n"
    report += f"Wind Speed: {data['wind']['speed']} m/s\n"
    report += f"Pressure: {data['main']['pressure']} hPa\n"
    report += '-' * 40 + '\n'
    filename = 'weather_report.txt'
    with open(filename, 'w') as f:
        f.write(report)
    return filename

def send_email(subject, body, to_email, attachment_path):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg.set_content(body)

    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='text', subtype='plain', filename=file_name)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        print(f"Email sent successfully to {to_email}")

def main():
    try:
        print("Fetching weather data...")
        weather_data = fetch_weather(CITY)

        print("Generating report...")
        report_file = generate_report(weather_data)

        print("Sending email...")
        subject = f"Weather Report for {CITY}"
        body = f"Hi,\n\nPlease find attached the latest weather report for {CITY}.\n\nRegards,\nWeather Bot"
        send_email(subject, body, RECEIVER_EMAIL, report_file)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
