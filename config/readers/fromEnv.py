import os
import PyPy


class Config:
    def __init__(self):
        pass

    @staticmethod()
    def get(name):
        os.environ.get(name)
