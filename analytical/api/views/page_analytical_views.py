from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from analytical.api.serializers import ViewSerializer
from pages.models import PageModel
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PageAnalyticalView(APIView):
    lookup_field = 'slug'
    serializer_class = ViewSerializer
    permission_classes = [
        IsAuthenticated, IsAdminUser
    ]

    def get(self, *args, **kwargs):
        if (slug := kwargs.get(self.lookup_field)) and (count := kwargs.get('count')):
            page: PageModel = get_object_or_404(PageModel, name=slug)
            serializer = self.serializer_class(page.get_view(count), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
