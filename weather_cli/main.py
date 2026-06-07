from weather import WeatherClient

API_KEY = 

def main():
    client = WeatherClient(API_KEY)
    
    while True:
        print("\n---- WEATHER CLI ----")
        print("1. fetch one city")
        print("2. fetch multiple cities")
        print("3. compare cities")
        print("4. save results")
        print("5. clear cache")
        print("6. exit")

        try:
            choice = int(input("choose option: "))
        except ValueError:
            print("please enter a number")
            continue

        match choice:
            case 1:
                # get city from user
                # await client.fetch_multiple([city])
                # display result
            case 2:
                # get comma separated cities from user
                # split into list
                # await client.fetch_multiple(cities)
                # display results
            case 3:
                # fetch multiple cities
                # client.compare(results)
            case 4:
                # save current results
            case 5:
                # client.clear_cache()
            case 6:
                break

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())