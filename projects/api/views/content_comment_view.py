from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from projects.api.serializers import ContentCommentSerializer
from projects.models import ContentModel, ContentCommentModel


class CreateCommentView(CreateAPIView):
    model = ContentCommentModel
    serializer_class = ContentCommentSerializer
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        content_slug = kwargs.get('slug', None)
        content = get_object_or_404(ContentModel, slug=content_slug, show=True)
        content_comment_serializer: ContentCommentSerializer = self.get_serializer(data=request.data)
        if content_comment_serializer.is_valid():
            new_comment = content_comment_serializer.save()
            content.comments.add(new_comment)
            return Response(content_comment_serializer.data, status=status.HTTP_201_CREATED)
        return Response(content_comment_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

