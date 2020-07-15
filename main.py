import requests


def get_temperature(lat: float, lng: float) -> int:
    """Returns the temperature in Celsius"""
    temperature = get_temperature_fahrenheit(lat, lng)
    return fahrenheit_to_celsius(temperature)


def get_temperature_fahrenheit(lat: float, lng: float) -> float:
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    if 'code' in data and 'error' in data:
        raise Exception(f'Error({data["code"]}): {data["error"]}')

    return data['currently']['temperature']


def fahrenheit_to_celsius(temperature: float) -> int:
    return int((temperature - 32) * 5 / 9)
