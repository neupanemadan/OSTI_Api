import json
from flask_classful import FlaskView

from flask import make_response


def base_representation(data, code, headers=None):
    content_type = 'application/json'
    dumped = json.dumps(data)
    if headers:
        headers.update({'Content-Type': content_type})
    else:
        headers = {'Content-Type': content_type}
    response = make_response(dumped, code, headers)
    return response


class BaseView(FlaskView):
    representations = {'application/json': base_representation}
