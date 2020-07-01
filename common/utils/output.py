from flask import make_response, current_app, request
from flask_restful.utils import PY3
from json import dumps


def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    if str(code) == '400':
        current_app.logger.warn(request.headers)
        current_app.logger.warn(request.data)
        current_app.logger.warn(str(data))

    if data is None:
        ret = {
            'status': True,
            'message': 'success',
            'data': None
        }
    elif 'message' not in data  and  data:
        ret = {
            'status':True,
            'message': 'success',
            'data': data
        }

    else:
        ret = {
            'status': False,
            'message': str(data.get('message')),
            'data': None
        }
    settings = current_app.config.get('RESTFUL_JSON', {})

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262

    dumped = dumps(ret, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp
