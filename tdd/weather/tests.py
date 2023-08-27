from django.test import TestCase
from django.urls import reverse
import json

class WeatherViewTest(TestCase):
    def test_valid_city(self):
        response = self.client.get(
            reverse("get-weather", kwargs={"city": "San Francisco"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding="utf8"),
            {"temperature": 14, "weather": "Cloudy"},
        )
    def test_invalid_city(self):
        response = self.client.get(
            reverse("get-weather", kwargs={"city": "InvalidCity"})
        )
        self.assertEqual(response.status_code, 404)
    def test_create_weather_data(self):
        data = {"city": "Chicago", "temperature": 18, "weather": "Cloudy"}
        response = self.client.post(
            reverse("create-weather"),
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(str(response.content, encoding="utf8"), data)

    def test_update_weather_data(self):
        updated_data = {"temperature": 25, "weather": "Sunny"}
        response = self.client.put(
            reverse("update-weather", kwargs={"city": "San Francisco"}),
            data=json.dumps(updated_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

        # Fetch the updated weather data from the server to compare
        updated_response = self.client.get(
            reverse("get-weather", kwargs={"city": "San Francisco"})
        )
        self.assertJSONEqual(
            str(updated_response.content, encoding="utf8"), updated_data
        )

    def test_delete_weather_data(self):
        response = self.client.delete(
            reverse("delete-weather", kwargs={"city": "San Francisco"})
        )
        self.assertEqual(response.status_code, 204)