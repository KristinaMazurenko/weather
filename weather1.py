import requests
from plyer import notification

CITY = "Краснодар"
API_KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANGUAGE = "ru"

url = rf'https://api.openweathermap.org/data/2.5/weather?q=Краснодар&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru'

def get_weather(city: str=CITY, api_key: str = API_KEY, 
                units: str = UNITS, language: str = LANGUAGE) -> dict:

  url = rf"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}&lang={language}"
  response = requests.get(url)
  return response.json()

response = requests.get(url)
weather_dict = response.json()
temp = weather_dict['main']['temp']
feels_like = weather_dict['main']['feels_like']
description = weather_dict['weather'][0]['description']

print(f'Температура: {temp}℃\nОщущается как: {feels_like}℃\nОписание: {description}')

notification.notify(
  title=f"Погода в {CITY}",
  message = f"Температура: {temp}℃\nОщущается как: {feels_like}℃\nОписание: {description}",
  app_name="Погода",
  app_icon=None,
  timeout=60,
  toast=True,
)

def format_weather_message(weather_dict: dict) -> str:
  
  temp = weather_dict['main']['temp']
  feels_like = weather_dict['main']['feels_like']
  description = weather_dict['weather'][0]['description']
  
  return f'Температура: {temp}℃\nОщущается как: {feels_like}℃\nОписание: {description}'


def notify_weather(message: str) -> None:
  notification.notify(
  message=message,
  app_name="Погода",
  app_icon=None,
  timeout=60,
  toast=True,
)

if __name__ == "__main__":
  weather_dict = get_weather()
  message = format_weather_message(weather_dict)
  notify_weather(message)

