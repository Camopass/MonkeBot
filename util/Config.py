import json


class Color:
    def __init__(self, json):
        self.success = int(json['success'], 16)
        self.fail = int(json['fail'], 16)
        self.starboard = int(json['starboard'], 16)


class Text:
    def __init__(self, json):
        self.fail = json['fail']
        self.starboard_remove = json['starboard_remove']

class Emoji:
    def __init__(self, json):
        self.accept = json['accept']
        self.deny = json['deny']


class Cosmetics:
    def __init__(self, json):
        self.color = Color(json['Color'])
        self.text = Text(json['Text'])
        self.emoji = Emoji(json['Emoji'])


class SQL:
    def __init__(self, json):
        self.db_name = json['db_name']


class Functionality:
    def __init__(self, json):
        self.SQL = SQL(json['SQL'])


class Config:
    def __init__(self, json):
        self.json = json
        self.cosmetics = Cosmetics(json['Cosmetics'])
        self.functionality = Functionality(json['Functionality'])


def load_config():
    with open('Main/config.json', 'rb') as f:
        config = str(f.read(), 'utf-8')

    return Config(json.loads(config))
