import json
import random
import string

import requests
from loguru import logger

logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', rotation='10 KB')


class Client:
    def __init__(self, email, password, max_reactions):
        self.email = email,
        self.password = password
        self.max_reactions = max_reactions
        self.token = None
        self.base_url = 'http://127.0.0.1:8000/'
        self.posts_list = None
        self.headers = None

    def sign_up(self):
        url = 'api/user/create/'
        self.send_request(
            url=self.base_url + url,
            method='POST',
            data={'email': self.email, 'password': self.password}
        )

    def log_in(self):
        url = 'api/token/'
        response = self.send_request(
            url=self.base_url + url,
            method='POST',
            data={'email': self.email, 'password': self.password}
        )
        self.token = response.json()['access']
        self._set_headers()

    def _set_headers(self):
        self.headers = {'Authorization': 'Bearer ' + self.token}

    def send_request(self, url, method, data=None):
        response = requests.request(
            method,
            url=url,
            data=data,
            headers=self.headers
        )
        status = response.status_code
        if status not in [200, 201]:
            message = f'Bad response with url:{url} data:{data}, status:{status}'
            logger.error(message)
            raise ValueError(message)
        return response

    def post_creation(self):
        url = self.base_url + 'api/post/create/'
        self.send_request(
            url=url,
            method='POST',
            data={
                'title': TestSocialNetworkApi.get_random_string(),
                'text': TestSocialNetworkApi.get_random_string()
            })

    def set_posts_list(self):
        url = 'api/post/list/'
        response = self.send_request(
            method='GET',
            url=self.base_url + url,
        )
        posts = response.json()
        random.shuffle(posts)
        self.posts_list = posts

    def post_reaction(self):
        url = self.base_url + 'api/post/feedback/'
        count_of_available_reaction = random.randint(1, self.max_reactions)
        count_of_reaction = 0
        reaction = [True, False]
        for post in self.posts_list:
            self.send_request(
                method='POST',
                url=url,
                data={'post': int(post['id']), 'like': random.choice(reaction)}
            )
            count_of_reaction += 1
            if count_of_reaction == count_of_available_reaction:
                break


class TestSocialNetworkApi:
    number_of_users = 0
    max_posts_per_user = 0
    max_reactions_per_user = 0

    def _set_settings(self):
        with open('settings.json') as file:
            data = json.load(file)
            self.max_reactions_per_user = data['max_reactions_per_user']
            self.max_posts_per_user = data['max_posts_per_user']
            self.number_of_users = data['number_of_users']

    @staticmethod
    def get_random_string():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(10))

    def run_test(self):
        self._set_settings()
        for _ in range(self.number_of_users):
            email = self.get_random_string() + '@gmail.com'
            password = 'xFPATHCeWA6wWxYH'
            new_user = Client(email=email, password=password, max_reactions=self.max_reactions_per_user)
            new_user.sign_up()
            new_user.log_in()
            new_user.set_posts_list()
            count_of_available_creation_posts = random.randint(1, self.max_posts_per_user)
            for _ in range(count_of_available_creation_posts):
                new_user.post_creation()
            new_user.post_reaction()
        logger.info('Testing is over!')


tester = TestSocialNetworkApi()
tester.run_test()
