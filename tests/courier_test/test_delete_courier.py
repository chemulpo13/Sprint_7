import pytest
import allure


@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Успешный запрос возвращает {{ ok: True }}")
    def test_successful_courier_deletion(self, courier_api, create_courier):
        response = courier_api.delete_courier(create_courier["id"])

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Запрос без id возвращает ошибку")
    def test_deletion_without_id(self, courier_api):
        response = courier_api.delete_courier(None)

        assert response.status_code in [400, 404, 500]

        assert "id" in response.text.lower()

    @allure.title("Запрос с несуществующим id возвращает ошибку")
    def test_deletion_with_nonexistent_id(self, courier_api):
        response = courier_api.delete_courier(999999)

        assert response.status_code == 404
        assert "Курьера с таким id нет" in response.json()["message"]