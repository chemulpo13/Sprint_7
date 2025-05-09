import pytest
import allure


@allure.feature("Получение заказа по его номеру")
class TestOrderByTrack:

    @pytest.fixture
    def create_test_order(self, order_api, data_generator):
        order_data = data_generator.generate_order_data()
        response = order_api.create_order(order_data)
        return response.json()["track"]

    @allure.title("Успешный запрос возвращает объект с заказом")
    def test_get_order_by_track_successful(self, order_api, create_test_order):
        response = order_api.get_order_by_track(create_test_order)

        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Запрос без номера заказа возвращает ошибку")
    def test_get_order_without_track(self, order_api):
        response = order_api.get_order_by_track(None)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Запрос с несуществующим заказом возвращает ошибку")
    def test_get_order_with_nonexistent_track(self, order_api):
        response = order_api.get_order_by_track(999999999)

        assert response.status_code == 404
        assert "message" in response.json()