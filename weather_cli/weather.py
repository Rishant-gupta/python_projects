import aiohttp
import asyncio
import json
import os
from utils import timer, logger, retry



class WeatherClient:
    
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CACHE_FILE = "weather_cli/cache/weather_cache.json"

    def __init__(self, api_key):
        self.api_key = api_key
        self.cache = {}
        self.session = None
        self.load_cache()

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self 
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()
        self.save_cache()
        return False
        
    @logger
    @timer
    def load_cache(self):
        
        if  os.path.exists("weather_cli/cache/") and not os.path.exists(self.CACHE_FILE):
            self.cache  = {}
        
        elif os.path.exists(self.CACHE_FILE):

            try:
                with open(self.CACHE_FILE, "r") as f:
                    self.cache = json.load(f)
            except :
                self.clear_cache()

        else:
            self.cache = {}
            folder_name = "cache"
            os.makedirs(folder_name)
            print(f"{folder_name} is created")


    @retry(3)
    @logger
    @timer
    async def fetch_city(self, city):
        city_name = city.strip()
        
        if city_name in self.cache:
            return self.cache[city_name]
        else:
            url = f"{self.BASE_URL}q={city_name},IN&appid={self.api_key}"
            
            async with self.session.get(url) as response:

                if response.status == 404:
                    print(f"city not found: {city_name}")
                    return None
                if response.status == 401:
                    raise Exception("invalid API key")
                
                data = await response.json()     
                        
            result = self.parse(data)
            self.cache[city_name] = result
            self.save_cache()

            return result         

    @retry(3)
    @logger
    @timer
    async def fetch_multiple(self, cities):
        
        
        results = await asyncio.gather(
            *[self.fetch_city(city= city) for city in cities]
        )

        return [r for r in results if r is not None]

    @logger
    @timer
    def parse(self, data):
        
        clean_dict = {

            "city":         data["name"],
            "temp":         round(data["main"]["temp"] - 273.15, 2),
            "feels_like":   round(data["main"]["feels_like"] - 273.15, 2),
            "pressure":     data["main"]["pressure"],
            "humidity":     data["main"]["humidity"],
            "wind_speed":   data["wind"]["speed"],
            "description":  data["weather"][0]["description"]
        }
        
        return clean_dict
        
    @logger
    @timer
    def display(self, results):
        if not results:
            print("no results to display")
            return
        w = 18

        # header
        headers = ["city", "temp", "feels like", "pressure", "humidity", "wind", "description"]
        print("".join(f"{h:<{w}}" for h in headers))
        print("-" * w * len(headers))

        # rows
        for row in results:
            values = [
                row['city'],
                f"{row['temp']}°C",
                f"{row['feels_like']}°C",
                f"{row['pressure']} hPa",
                f"{row['humidity']}%",
                f"{row['wind_speed']} m/s",
                row['description']
            ]
            print("".join(f"{v:<{w}}" for v in values))

    @logger
    @timer
    def compare(self, results):
        
        if not results:
            print("no results to compare")
            return

        hottest  = max(results, key=lambda x: x["temp"])
        coldest  = min(results, key=lambda x: x["temp"])
        humid    = max(results, key=lambda x: x["humidity"])

        print("\n---- COMPARISON ----")
        print(f"hottest  → {hottest['city']:<15} {hottest['temp']}°C")
        print(f"coldest  → {coldest['city']:<15} {coldest['temp']}°C")
        print(f"most humid → {humid['city']:<15} {humid['humidity']}%")

    
    @logger
    @timer
    def save_cache(self):
        with open(self.CACHE_FILE, "w") as f:
            json.dump(self.cache, f, indent=4)
            
    @logger
    @timer
    def clear_cache(self):
        self.cache = {}
        try:   
            os.remove(self.CACHE_FILE)
            print("cache is cleared")
        except FileNotFoundError:
            print("no cache file found — nothing to delete")
    
          

        

        
