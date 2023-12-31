from django.db import models
from config.settings.base import env


def default_ip_data():
    return {}


class ViewModel(models.Model):
    visit_time = models.DateTimeField(auto_now_add=True)
    reload_count_in_a_clock = models.IntegerField(default=1)
    ip_address = models.TextField()
    # ip_query_id = models.TextField(null=True, blank=True, default=None)
    ip_data = models.JSONField(null=True, default=default_ip_data, blank=True)
    is_i_am = models.BooleanField(default=False)
    user_agent = models.TextField(null=True, default=None, blank=True, editable=False)

    def __str__(self):
        visited_time = self.visit_time.strftime("%Y-%B-%d %H:%M")
        months = {
            'January': 'Ocak',
            'February': 'Şubat',
            'March': 'Mart',
            'April': 'April',
            'May': 'Mayıs',
            'June': 'Haziran',
            'July': 'Temmuz',
            'August': 'Ağustos',
            'September': 'Eylül',
            'October': 'Ekim',
            'November': 'Kasım',
            'December': 'Aralık',
        }

        for month, turkish in months.items():
            visited_time = visited_time.replace(month, turkish)

        return f'{self.ip_address} | {visited_time} '

    @staticmethod
    def ip_query_service_url() -> str:
        return env('IP_QUERY_SERVICE')

