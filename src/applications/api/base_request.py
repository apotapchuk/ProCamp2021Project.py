import logging
import requests as r
import random
import time
import session
from selenium import webdriver
from selenium.webdriver import ActionChain
from selenium.webdriver.support.select import Select
from config.config import Config


class BaseRequest:
    def __init__(self):
        self.session = None

    def session(self):
        self.loggin()
        self.session = requests.Session()

# initialize webdriver
    driver = webdriver.Chrome()

# open URL and maximize window
    driver.get(BASE_URL)
    driver.maximize.window()


def post(*args, **kwargs):
    r = requests.post(*args, *kwargs)
    logging.DEBUG("sending_requests, *args, **kwargs")

    if r.status_code == 409:
        raise logging.WARNING("Response status_code is in black list.retrying")
        time.sleep(1)
        raise logging.DEBUG("response: r")
    elif r.status_code == 430:
        raise logging.ERROR("Error during POST request to url, request response: r")
    else:
        raise logging.DEBUG("response status_code is in black_list.retrying")
