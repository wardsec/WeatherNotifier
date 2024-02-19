from twilio.rest import Client
from bs4 import BeautifulSoup
import requests

class WeatherNotifier:
    def __init__(self, account_sid, auth_token, twilio_number, recipient_number, city_id):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.twilio_number = twilio_number
        self.recipient_number = recipient_number
        self.city_id = city_id
        self.client = Client(account_sid, auth_token)
        self.base_url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/"

    def fetch_weather_info(self):
        try:
            url = f"{self.base_url}{self.city_id}"
            response = requests.get(url)
            response.raise_for_status()
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')
            resume = soup.find(class_='-gray -line-height-24 _center')
            tempMin = soup.find(id='min-temp-1')
            tempMax = soup.find(id='max-temp-1')

            return resume, tempMin, tempMax
        except requests.RequestException as e:
            print("Failed to retrieve data from the website:", e)
            return None, None, None

    def send_notification(self, message_body):
        try:
            message = self.client.messages.create(
                body=message_body,
                from_=self.twilio_number,
                to=self.recipient_number
            )
            print("Message sent successfully. SID:", message.sid)
        except Exception as e:
            print("Failed to send notification:", e)

    def notify_weather(self):
        resume, tempMin, tempMax = self.fetch_weather_info()
        if resume and tempMin and tempMax:
            message_body = f"Bom dia, Temperatura Mínima prevista: {tempMin.string}\nTemperatura Máxima prevista: {tempMax.string}"
            self.send_notification(message_body)
        else:
            print("Failed to extract required information from the website.")


