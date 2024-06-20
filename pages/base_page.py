import requests


class BasePage:
    def __init__(self, url, endpoint):
        self.url = url
        self.endpoint = endpoint

    def get_request(self, option):
        url = f"{self.url}/{self.endpoint}/{option}"
        response = requests.get(url)
        return response

    def post_request(self, data):
        url = f"{self.url}/{self.endpoint}"
        response = requests.post(url, json=data)
        return response

    def put_request(self, option, data):
        url = f"{self.url}/{self.endpoint}/{option}"
        response = requests.put(url, json=data)
        return response

    def delete_request(self, option):
        url = f"{self.url}/{self.endpoint}/{option}"
        response = requests.delete(url)
        return response

