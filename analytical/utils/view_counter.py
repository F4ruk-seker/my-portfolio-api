from ..models import ViewModel
from django.utils import timezone
import logging
from .ip_data import get_ip_data
from django.conf import settings
# from config.settings.base import CUSTOM_LOGGER


class ViewCountWithRule:
    def __init__(self, page, request):
        self.page = page
        self.request = request
        self.ip_address = self.get_client_ip()
        self.logger = logging.getLogger('ViewCountWithRule')

    def can(self):

        if self.page is not None:
            now = timezone.now()
            # if vs := ViewModel.objects.filter(ip_address=self.ip_address).order_by('-visit_time').first():
            if vs := self.page.view.all().filter(ip_address=self.ip_address).order_by('-visit_time').first():
                return not vs.visit_time.hour == now.hour
            else:
                return True

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        return x_forwarded_for.split(',')[0] if x_forwarded_for else self.request.META.get('REMOTE_ADDR')

    def is_admin_user(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def get_user_agent(self):
        try:
            return self.request.META['HTTP_USER_AGENT']
        except Exception as error:
            self.logger.error(error)
            if hasattr(self.request, 'META'):
                self.logger.error(self.request.META)
            else:
                self.logger.error('request is not have META')
            return

    def get_ip_data(self):
        if settings.DEBUG:
            return {}
        try:
            return get_ip_data(self.ip_address)
        except Exception as ERR:
            ...
            # CUSTOM_LOGGER.construct(
            #     title='ip query service',
            #     error=ERR,
            #     metadata=f'{self.ip_address}'
            # )
            # CUSTOM_LOGGER.send()

    def action(self):
        if self.can():
            _ = self.create_view()
            # self.page.save()
            self.page.view.add(_)

    def create_view(self):

        return ViewModel.objects.create(
                visit_time=timezone.now(),
                ip_address=self.ip_address,
                is_i_am=self.is_admin_user(),
                ip_data=self.get_ip_data(),
                user_agent=str(self.get_user_agent()),
                query_string=self.request.META['QUERY_STRING'],
                request_type=self.request.META['REQUEST_METHOD'],
                request_data=self.request.META['HTTP_SEC_CH_UA']
            )

    def __call__(self, *args, **kwargs):
        self.action()


