from main import get_temperature
import pytest
from unittest.mock import patch


@pytest.mark.parametrize('lat, lng, temperature, expected', [
    (-14.235004, -51.92528, 62, 16),
    (-10.12121, -1.2112121, 32, 0),
    (0, 0, -459.67, -273),
    (0, 0, 136, 57),
])
def test_get_temperature_by_lat_lng(lat, lng, temperature, expected):
    with patch('main.requests.get') as mock_requests_get:
        mock_requests_get.return_value.json.return_value = {
            'currently': {'temperature': temperature}
        }
        assert get_temperature(lat, lng) == expected
