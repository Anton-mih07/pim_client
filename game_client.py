import json

import requests


class Game:
    BASE_API_URL = 'http://localhost:8000/api/v1/'

    def __init__(self, username, password):
        response = self.login(username, password)
        self.token = response['key']

    def login(self, username, password):
        return json.loads(
            requests.post(
                self.BASE_API_URL + 'auth/login/',
                {'username': username, 'password': password}
            ).text
        )

    def get_monsters(self):
        return json.loads(
            requests.get(
                self.BASE_API_URL + 'monsters/',
                headers={'Authorization': 'Token ' + self.token},
            ).text
        )

    def get_monster(self, monster_id):
        return json.loads(
            requests.get(
                self.BASE_API_URL + f'monsters/{monster_id}/',
                headers={'Authorization': 'Token ' + self.token},
            ).text
        )

    def attack(self, monster_id, answer):
        print(json.loads(
            requests.post(
                self.BASE_API_URL + f'monsters/{monster_id}/attack/',
                {'answer': answer},
                headers={'Authorization': 'Token '+self.token},
            ).text
        ))