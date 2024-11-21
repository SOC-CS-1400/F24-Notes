
"""Test the Weather App
"""
import weather_app as wa
from pprint import pprint as pp


def main():
    print('Testing Weather App')
    weather_data =wa.pull_weather_data(84408)
    pp(weather_data)
    print(f"The weather for {weather_data['name']}:")
    print(f"is {weather_data['main']['temp']} Celsius")


if __name__ == '__main__':
    # Call main function
    main()
