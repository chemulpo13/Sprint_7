import pytest
import allure

@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_courier_can_be_created(self, courier_api, data_generator):
        courier_data = data_generator.generate_courier_data()

        response = courier_api.create_courier(
            courier_data["login"],
            courier_data["password"],
            courier_data["firstName"]
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        login_response = courier_api.login_courier(
            courier_data["login"],
            courier_data["password"]
        )

        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            courier_api.delete_courier(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_identical_couriers(self, courier_api, data_generator):
        courier_data = data_generator.generate_courier_data()

        first_response = courier_api.create_courier(
            courier_data["login"],
            courier_data["password"],
            courier_data["firstName"]
        )

        second_response = courier_api.create_courier(
            courier_data["login"],
            courier_data["password"],
            courier_data["firstName"]
        )

        assert second_response.status_code == 409
        assert "Этот логин уже используется" in second_response.json()["message"]

        login_response = courier_api.login_courier(
            courier_data["login"],
            courier_data["password"]
        )

        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            courier_api.delete_courier(courier_id)

    @allure.title("Для создания курьера нужны все обязательные поля")
    @pytest.mark.parametrize("login,password,expected_code", [
        (None, "test_password", 400),
        ("test_login", None, 400),
    ])
    def test_required_fields_for_courier_creation(self, courier_api, login, password, expected_code):
        response = courier_api.create_courier(login, password, first_name="test_name")

        assert response.status_code == expected_code
        assert "Недостаточно данных" in response.json()["message"]