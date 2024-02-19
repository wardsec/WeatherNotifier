# WeatherNotifier

## Overview
WeatherNotifier é uma classe Python que busca informações meteorológicas do site Climatempo e as envia como uma notificação via Twilio SMS.

## Dependencias
- [twilio](https://www.twilio.com/docs/usage/installing-the-python-twilio-sdk)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests](https://pypi.org/project/requests/)

```bash
pip install -r requirements.txt
```
## Exemplo de uso
```
from WeatherNotifier import WeatherNotifier
account_sid = # Conta sid
auth_token = # Token da conta
twilio_number = #Numero fornecido pela twilio
recipient_number = # Numero em que irá chegar a mensagem
city_id = "458"  # Id provido na url do site climatempo

weather_notifier = WeatherNotifier(account_sid, auth_token, twilio_number, recipient_number, city_id)
weather_notifier.notify_weather()

```
Result:  <p>

<img src="https://i.ibb.co/89cGCWw/185124822-825131791747122-8350592680893754408-n.jpg" height="600">
