import aiohttp
import asyncio
import json
import os
from d
from utils import timer, logger, retry

class WeatherClient:
    
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    CACHE_FILE = "cache/weather_cache.json"

    def __init__(self, api_key):
        self.api_key = api_key
        self.cache = {}
        self.load_cache()

    def load_cache(self):
        # loads cache from JSON file if it exists
        # stores in self.cache dict

    async def fetch_city(self, session, city):
        # checks cache first — returns cached result if exists
        # if not cached — makes API call using aiohttp
        # stores result in cache
        # returns weather data dict

    async def fetch_multiple(self, cities):
        # creates one aiohttp session
        # uses asyncio.gather to fetch all cities simultaneously
        # returns list of results

    def parse(self, data):
        # extracts relevant fields from raw API response
        # returns clean dict:
        # {city, temp_celsius, feels_like, humidity, wind_speed, description}

    def display(self, results):
        # prints results as clean aligned table

    def compare(self, results):
        # shows which city is hottest, coldest, most humid

    def save(self, results, filepath):
        # saves results to JSON file

    def save_cache(self):
        # writes self.cache to cache JSON file

    def clear_cache(self):
        # empties self.cache
        # deletes cache file