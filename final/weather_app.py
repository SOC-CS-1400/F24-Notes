
"""Weather App to check current weather conditions"""
# install package, type on your terminal:
# pip install requests
import requests

API_KEY = 'af4f939501ebb649537e015196aedc70'  # YOUR OWN KEY
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'


def pull_weather_data(zip_code, country='us'):
    api_url = BASE_URL + 'zip=' + str(zip_code)
    api_url += f',{country}' + '&units=metric'  # add country and units
    api_url += '&appid=' + API_KEY  # add your key
    try:
        # Connect to API and get data in JSON format
        weather_data = requests.get(api_url).json()
        if weather_data['cod'] != 200:  # response code
            raise ValueError
    except ValueError:
        print('Bad response from API')

    return weather_data


def main():
    pass


if __name__ == '__main__':
    # Call main function
    main()
