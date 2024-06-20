import allure
from pages.user_page import UserPage


class TestUser:
    url = "https://petstore.swagger.io/v2"
    endpoint = "user"
    user1 = "JamesBond007"
    user2 = "JohnRambo"
    user3 = "RockyBalboa"

    @allure.feature('Проверка CRUD методов')
    @allure.story('Проверка ручки user')
    def test_main(self):
        service = UserPage(url=self.url, endpoint=self.endpoint)
        service.test_post_create_user()
        service.test_post_not_create_user()
        service.test_get_user(self.user1)
        service.test_get_non_existent_user(self.user2)
        service.test_put_update_data_user(self.user1)
        service.test_put_non_existent_user(self.user3)
        service.test_delete_user(self.user2)
        service.test_delete_non_existent_user(self.user1)
