from app.schema.weather_schema import BaseWeather
import python_weather

class WeatherService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.third-party.com"

    async def get_data(self, endpoint: str, params: dict):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/{endpoint}", params=params, headers=headers)
            response.raise_for_status()
            return response.json()