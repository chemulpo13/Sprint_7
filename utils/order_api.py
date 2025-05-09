import requests
import allure

class OrderApi:
    def __init__(self):
        self.base_url = "https://qa-scooter.praktikum-services.ru/api/v1"

    @allure.step("Создание заказа")
    def create_order(self, order_data):
        response = requests.post(f"{self.base_url}/orders", json=order_data)
        return response

    @allure.step("Получение списка заказов")
    def get_orders(self):
        response = requests.get(f"{self.base_url}/orders")
        return response

    @allure.step("Принятие заказа")
    def accept_order(self, order_id, courier_id):
        response = requests.put(f"{self.base_url}/orders/accept/{order_id}",
                               params={"courierId": courier_id})
        return response

    @allure.step("Получение заказа по номеру")
    def get_order_by_track(self, track):
        response = requests.get(f"{self.base_url}/orders/track",
                              params={"t": track})
        return response