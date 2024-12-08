from flask import Flask, render_template, request

from services.weather import get_weather_info, parse_weather
from services.model import evaluate_weather_conditions

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"]) 
def index():

    if request.method == "POST": # При POST запросе

        try:

            # Получение координат начальной и конечной точек
            start_lat = request.form.get("start_lat", type=float)
            start_lon = request.form.get("start_lon", type=float)
            end_lat = request.form.get("end_lat", type=float)
            end_lon = request.form.get("end_lon", type=float)
            # Получение данных из API для обеих точек
            start_raw_weather = get_weather_info(start_lat, start_lon)
            end_raw_weather = get_weather_info(end_lat, end_lon)
            
            # Парсинг данных
            start_weather = parse_weather(start_raw_weather)
            end_weather = parse_weather(end_raw_weather)
            
            # Анализ погоды
            start_result = evaluate_weather_conditions(start_weather)
            end_result = evaluate_weather_conditions(end_weather)

            # Передача данных в шаблон
            return render_template(
                "result.html", 
                start_weather=start_weather, 
                start_result=start_result,
                end_weather=end_weather, 
                end_result=end_result
            )
        except Exception as e:

            return render_template("error.html", error=str(e)), 500 # 500 - internal server error
        
    return render_template("index.html") # Случай по умолчанию при GET запросе

if __name__ == "__main__":

    app.run()