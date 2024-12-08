def evaluate_weather_conditions(meteorological_data):
   
    # Извлечение параметров
    temp = meteorological_data.get("temperature")
    windspeed = meteorological_data.get("windspeed")
    rain_chance = meteorological_data.get("probability")
    humidity_level = meteorological_data.get("humidity")

    # Проверка наличия всех необходимых данных
    if None in (temp, windspeed, rain_chance, humidity_level):
        return "Внимание: неполные данные."

    # Оценка погодных условий
    if temp < 0 or temp > 35:
        return "Неблагоприятные условия: экстремальная температура"
    if windspeed > 50:
        return "Неблагоприятные условия: штормовой ветер"
    if rain_chance > 70:
        return "Неблагоприятные условия: высокая вероятность осадков"
    if humidity_level > 80:
        return "Неблагоприятные условия: чрезмерная влажность"

    # Если все параметры в норме
    return "Отличная погода!"
