import base64
from base64 import b64encode
import UIKit


def base64_encode(string):
    result = base64.b64encode(string.encode()).decode()
    return result


def base64_encode_headers(username, password):
    headers = {"Authorization": f"Basic {base64_encode(f'{username}:{password}')}"}
    return headers
