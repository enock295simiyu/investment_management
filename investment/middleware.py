# investment/middleware.py

import threading

_local = threading.local()


class CurrentUserMiddleware:
    """
    Get the current logged in user.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _local.user = request.user
        response = self.get_response(request)
        return response


def get_current_user():
    return getattr(_local, 'user', None)
