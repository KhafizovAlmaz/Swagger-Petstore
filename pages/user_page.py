import allure
from pages.base_page import BasePage
from data.user_data import UserData


class UserPage(BasePage):
    data = UserData()

    def test_post_create_user(self):  # Все тесты можно параметризовать, но было лень делать в этой реализации)
        with allure.step('Создание пользователя методом POST'):
            post_response = self.post_request(self.data.USER)
            assert post_response.status_code == 200
            assert post_response.json().get("message") == str(self.data.USER.get("id"))  # либо сверять тело ответа
            # тут можно сделать проверку на появление пользователя в бд или проверить get запросом

    def test_post_not_create_user(self):
        with allure.step('Отправка другого типа данных методом POST'):
            post_response = self.post_request(data=[])  # передаем массив вместо словаря
            assert post_response.status_code == 500
            assert post_response.json().get("message") == "something bad happened"

    def test_get_user(self, username):
        with allure.step('Получение информации о пользователе методом GET'):
            get_response = self.get_request(username)
            assert get_response.status_code == 200
            assert get_response.json().get("id") == self.data.USER.get("id")

    def test_get_non_existent_user(self, username):
        with allure.step('Получение информации о несуществующем пользователе методом GET'):
            get_response = self.get_request(username)
            assert get_response.status_code == 404
            assert get_response.json().get("message") == "User not found"

    def test_put_update_data_user(self, username):
        with allure.step('Обновление информации пользователя методом PUT'):
            put_response = self.put_request(username, self.data.UPDATE_USER)
            self.test_get_non_existent_user(username)
            assert put_response.status_code == 200
            assert put_response.json().get("message") == str(self.data.UPDATE_USER.get("id"))

    def test_put_non_existent_user(self, username):
        with allure.step('Обновление информации пользователя пустым списком методом PUT'):
            put_response = self.put_request(username, [])
            assert put_response.status_code == 500
            assert put_response.json().get("message") == "something bad happened"

    def test_delete_user(self, username):
        with allure.step('Удаление пользователя методом DELETE'):
            delete_response = self.delete_request(username)
            self.test_get_non_existent_user(username)
            assert delete_response.status_code == 200
            assert delete_response.json().get("message") == username

    def test_delete_non_existent_user(self, username):
        with allure.step('Удаление несуществующего пользователя методом DELETE'):
            delete_response = self.delete_request(username)
            assert delete_response.status_code == 404
