import requests
import allure

class CourierApi:
    def __init__(self):
        self.base_url = "https://qa-scooter.praktikum-services.ru/api/v1"

    @allure.step("Создание курьера")
    def create_courier(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f"{self.base_url}/courier", json=payload)
        return response

    @allure.step("Логин курьера")
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{self.base_url}/courier/login", json=payload)
        return response

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        payload = {
            "id": courier_id
        }
        response = requests.delete(f"{self.base_url}/courier/{courier_id}", json=payload)
        return response