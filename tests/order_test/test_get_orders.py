import allure


@allure.feature("Получение списка заказов")
class TestOrdersList:

    @allure.title("В ответе возвращается список заказов")
    def test_get_orders_returns_orders_list(self, order_api):
        response = order_api.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)