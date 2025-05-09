import pytest
import allure


@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("Заказ можно создать с различными вариантами цветов")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, order_api, data_generator, color):
        order_data = data_generator.generate_order_data(color)

        response = order_api.create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()