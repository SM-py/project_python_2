import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather_info(lat, lon):

    params = { #Параметры запроса
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "relative_humidity_2m,precipitation_probability", 
    }

    try:

        resp = requests.get(BASE_URL, params=params) #Отправляем запрос
        resp.raise_for_status()  #Проверяем ответ

    except requests.RequestException as e:

        raise Exception(f"Ошибка подключения к API: {e}")
    
    weather_info = resp.json() #Получаем данные

    if not weather_info :

        raise Exception("API не отвечает") #Если данные недоступны
    
    return weather_info #Возвращаем данные


def parse_weather(raw_data): #Функция для парсинга данных

    curr = raw_data.get("current_weather", {}) #Получаем данные
    hourly = raw_data.get("hourly", {})

    hum = hourly.get("relative_humidity_2m", [None])[0]  #Влажность
    probability = hourly.get("precipitation_probability", [None])[0] #Вероятность дождя

    return { #Возвращаем данные
        "temperature": curr.get("temperature"),
        "probability": probability,
        "humidity": hum,
        "windspeed": curr.get("windspeed")
        }


