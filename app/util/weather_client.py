from app.schema.weather_schema import BaseWeather
import python_weather

async def get_weather(city):
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    response = await client.get(city)
    current_weather = response.current
    return BaseWeather(temperature=current_weather.temperature, description = current_weather.description, kind = str(current_weather.kind).replace("kind.",""))
