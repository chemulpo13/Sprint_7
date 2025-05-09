import pytest
from helpers.data_generator import DataGenerator
from utils.courier_api import CourierApi
from utils.order_api import OrderApi

@pytest.fixture
def courier_api():
    return CourierApi()


@pytest.fixture
def order_api():
    return OrderApi()


@pytest.fixture
def data_generator():
    return DataGenerator


@pytest.fixture
def create_courier(courier_api, data_generator):
    courier_data = data_generator.generate_courier_data()

    response = courier_api.create_courier(
        courier_data["login"],
        courier_data["password"],
        courier_data["firstName"]
    )

    if response.status_code == 201:
        login_response = courier_api.login_courier(
            courier_data["login"],
            courier_data["password"]
        )
        if login_response.status_code == 200:
            courier_data["id"] = login_response.json()["id"]

    yield courier_data

    if "id" in courier_data:
        courier_api.delete_courier(courier_data["id"])