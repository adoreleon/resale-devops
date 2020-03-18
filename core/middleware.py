from threading import current_thread

from django.utils.deprecation import MiddlewareMixin

_requests = {}


def get_request(*args, **kwargs):
    t = current_thread()
    if t in _requests:
        return _requests[t]


class UserRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        _requests[current_thread()] = request
