import json

class UserData:
    def __init__(self, user):
        with open('data/user_info.json') as f:
            self.all_user_data = json.load(f)
            self.user_data = self.all_user_data[user]

    def get(self, param):
        return self.user_data[param]
