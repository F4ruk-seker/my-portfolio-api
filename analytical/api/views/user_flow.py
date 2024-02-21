from datetime import timedelta
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from analytical.models import ViewModel
from pages.models import PageModel
from projects.models import ContentModel
from game.models import GameVideoModel
from analytical.api.serializers import ViewSerializer


class UserFlow(APIView):
    authentication_classes = []

    models_with_view_reference = [
        PageModel,
        ContentModel,
        GameVideoModel
    ]

    def get(self, request, *args, **kwargs):
        time_ranges = {
            'h': timezone.now() - timedelta(hours=1),
            'd': timezone.now() - timedelta(days=1),
            'w': timezone.now() - timedelta(weeks=1),
            'm': timezone.now() - timedelta(weeks=4)
        }
        one_hour_ago = time_ranges.get(request.query_params.get('last'), 'h')
        order = request.query_params.get('order', 'ascend')
        user_ip = kwargs.get('ip')
        views = ViewModel.objects.filter(
            ip_address=user_ip,
            visit_time__gte=one_hour_ago,
        ).order_by('visit_time' if order == 'ascend' else '-visit_time')
        view_data = ViewSerializer(views, many=True).data
        for view in view_data:
            view['action'] = self.get_view_type(view.get('id'))
        return Response(view_data)

    def get_view_type(self, id):
        for model in self.models_with_view_reference:
            if model.objects.filter(view__id=id).exists():
                view = model.objects.filter(view__id=id).first()
                return {
                    'type': str(view),
                    'title': view.title,
                }


