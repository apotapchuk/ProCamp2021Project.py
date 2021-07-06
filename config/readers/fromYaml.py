import pyaml


class Config:
    def __init__(self):
        pass

    @staticmethod()
    def get(name):
        _dict = pyaml.load(name)
        _dict.get(name)

    def convert_to_dict(path):
        return yaml.load(path)