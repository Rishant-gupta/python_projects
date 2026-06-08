from weather import WeatherClient
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("WEATHER_API")

async def main():
    async with WeatherClient(api_key) as client:
        current_result = []
    
        while True:
            print("\n---- WEATHER CLI ----")
            print("1. fetch multiple cities")
            print("2. fetch one city")
            print("3. compare cities")
            print("4. clear cache")
            print("5. save_cache")
            print("6. exit")

            try:
                choice = int(input("choose option: "))
            except ValueError:
                print("please enter a number")
                continue

            match choice:
                case 1:
                    cities = (input("Enter the name of cities with comma separation: ")).split(",")
                    
                    try:
                        result = await client.fetch_multiple(cities)
                        client.display(result)
                    except Exception as e:
                        print(f"error fetching weather: {e}")
                    current_result.append(result)
                case 2:
                    city = input("Enter the name of city: ")
                    result = await client.fetch_city(city)
                    if result:
                        client.display([result])
                    current_result.append(result)
                case 3:
                    cities = (input("Enter the name of cities with space separation: ")).split()
                    result = await client.fetch_multiple(cities)
                    client.compare(result)
                case 4:
                    client.clear_cache()
                case 5:
                    client.save_cache()
                case 6:
                    break
                

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())