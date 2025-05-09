import random
import string


class DataGenerator:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_courier_data():
        login = DataGenerator.generate_random_string(10)
        password = DataGenerator.generate_random_string(10)
        first_name = DataGenerator.generate_random_string(10)
        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }

    @staticmethod
    def generate_order_data(colors=None):
        if colors is None:
            colors = []

        return {
            "firstName": DataGenerator.generate_random_string(10),
            "lastName": DataGenerator.generate_random_string(10),
            "address": DataGenerator.generate_random_string(20),
            "metroStation": "1",
            "phone": "+7" + ''.join(random.choice(string.digits) for _ in range(10)),
            "rentTime": random.randint(1, 10),
            "deliveryDate": "2023-06-06",
            "comment": DataGenerator.generate_random_string(30),
            "color": colors
        }