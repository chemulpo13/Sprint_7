import pytest
import allure


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_courier_can_login(self, courier_api, create_courier):
        response = courier_api.login_courier(
            create_courier["login"],
            create_courier["password"]
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Для авторизации нужны все обязательные поля")
    @pytest.mark.parametrize("login,password", [
        (None, "test_password"),
        ("test_login", None),
    ])
    @pytest.mark.flaky(reruns=3)
    def test_required_fields_for_login(self, courier_api, login, password):
        response = courier_api.login_courier(login, password)

        assert response.status_code in [400, 504]

        if response.status_code == 400:
            error_message = response.json().get("message", "")
            assert "Недостаточно данных" in error_message

    @allure.title("Система вернёт ошибку, если неправильно указать логин или пароль")
    def test_login_with_wrong_credentials(self, courier_api, create_courier):
        response = courier_api.login_courier(
            create_courier["login"],
            "wrong_password"
        )

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json()["message"]

    @allure.title("Авторизация несуществующего пользователя")
    def test_login_nonexistent_courier(self, courier_api, data_generator):
        courier_data = data_generator.generate_courier_data()

        response = courier_api.login_courier(
            courier_data["login"],
            courier_data["password"]
        )

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json()["message"]