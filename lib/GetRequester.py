import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        content_list = []
        contents = json.loads(self.get_response_body())
        for content in contents:
            content_list.append(content)

        return content_list
