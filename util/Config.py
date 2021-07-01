import json


class Color:
    def __init__(self, json):
        self.success = int(json['success'], 16)
        self.fail = int(json['fail'], 16)


class Text:
    def __init__(self, json):
        self.fail = json['fail']


class Cosmetics:
    def __init__(self, json):
        self.color = Color(json['Color'])
        self.text = Text(json['Text'])


class Config:
    def __init__(self, json):
        self.json = json
        self.cosmetics = Cosmetics(json['Cosmetics'])


def load_config():
    with open('Main/config.json') as f:
        config = str(f.read())

    return Config(json.loads(config))
