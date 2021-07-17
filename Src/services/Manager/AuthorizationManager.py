from django.core.handlers.wsgi import WSGIRequest
from Src.config.config import api_secret
from datetime import datetime, timedelta
import jwt
from functools import wraps
from django.http import HttpResponseForbidden, HttpResponseServerError


def make_token_for_user_id(user_id: str) -> str:
    token = jwt.encode({'id': user_id, 'exp': datetime.utcnow() + timedelta(days=7)}, api_secret, algorithm='HS256')
    return token


def is_valid_request(request: WSGIRequest):
    if "Authorization" in request.headers:
        try:
            encoded_jwt = request.headers["Authorization"]
            res = jwt.decode(encoded_jwt, api_secret, algorithms=['HS256'])
            if "id" in res:
                return True
            return False
        except Exception as e:
            return False
    return False


def extract_user_id(request: WSGIRequest):
    if is_valid_request(request):
        encoded_jwt = request.headers.get("Authorization")
        res = jwt.decode(encoded_jwt, api_secret, algorithms=['HS256'])
        return str(res.get("id"))


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kws):
        # print(args, kws, func)
        request: WSGIRequest = args[1]

        if request.headers["Authorization"] is None:
            return HttpResponseForbidden()

        user_id = None
        encode_token = request.headers.get('Authorization')
        try:
            user_id = jwt.decode(encode_token, api_secret, algorithms=['HS256'])

        except:
            return HttpResponseForbidden()

        return func(*args, **kws)

    return decorated_function
#
