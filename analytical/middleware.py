from django.shortcuts import reverse
from django.shortcuts import redirect


class AnalyticalMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = reverse('admin:index')

        response = self.get_response(request)
        print(request)
        print(self)
        return response

    def request_is_analyzable(self):
        # /api/page/
        ...

