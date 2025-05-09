import pytest
import allure


@allure.feature("Принятие заказа")
class TestAcceptOrder:

    @pytest.fixture
    def create_order(self, order_api, data_generator):
        order_data = data_generator.generate_order_data()
        response = order_api.create_order(order_data)
        return response.json()["track"]

    @allure.title("Успешный запрос возвращает {{ ok: True }}")
    def test_successful_order_acceptance(self, order_api, create_courier, create_order):
        order_info_response = order_api.get_order_by_track(create_order)
        order_id = order_info_response.json()["order"]["id"]

        response = order_api.accept_order(order_id, create_courier["id"])

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Если не передать id курьера, запрос вернёт ошибку")
    def test_accept_order_without_courier_id(self, order_api, create_order):
        order_info_response = order_api.get_order_by_track(create_order)
        order_id = order_info_response.json()["order"]["id"]

        response = order_api.accept_order(order_id, None)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Если передать неверный id курьера, запрос вернёт ошибку")
    def test_accept_order_with_nonexistent_courier_id(self, order_api, create_order):
        order_info_response = order_api.get_order_by_track(create_order)
        order_id = order_info_response.json()["order"]["id"]

        response = order_api.accept_order(order_id, 999999)

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Если не передать id заказа, запрос вернёт ошибку")
    def test_accept_order_without_order_id(self, order_api, create_courier):
        response = order_api.accept_order(None, create_courier["id"])

        assert response.status_code in [400, 404, 500]

        if response.status_code == 500:
            allure.attach(
                response.text,
                name="Error Response",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.title("Если передать неверный id заказа, запрос вернёт ошибку")
    def test_accept_order_with_nonexistent_order_id(self, order_api, create_courier):
        response = order_api.accept_order(999999, create_courier["id"])

        assert response.status_code == 404
        assert "message" in response.json()