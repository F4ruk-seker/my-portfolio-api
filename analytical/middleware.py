from django.core.handlers.wsgi import WSGIRequest
from analytical.utils import ViewCountWithRule
from pages.models import PageModel


class AnalyticalMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        response = self.get_response(request)
        if not request.get_full_path().startswith('/api/'):
            self.save_a_normal_request(request)
            print('CREATED')
        return response

    @staticmethod
    def save_a_normal_request(request: WSGIRequest):
        ...
        # page, is_created = PageModel.objects.get_or_create(
        #     name='A-Normal', title='A Normal'
        # )
        # ViewCountWithRule(
        #     page=page,
        #     request=request,
        #     hourly_cooldown=request.user.is_superuser
        # )()
