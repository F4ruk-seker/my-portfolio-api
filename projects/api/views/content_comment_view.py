from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from projects.api.serializers import ContentCommentSerializer
from projects.models import ContentModel, ContentCommentModel


class CreateCommentView(CreateAPIView):
    serializer_class = ContentCommentSerializer

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)

        content_slug = kwargs.get('slug', None)
        comment_text = request.data.get('comment', None)

        if not (content_slug and comment_text):
            return Response({}, status=status.HTTP_406_NOT_ACCEPTABLE)

        content = get_object_or_404(ContentModel, slug=content_slug)
        comment = ContentCommentModel.objects.create(comment=comment_text, user=self.request.user)
        content.comments.add(comment)

        return Response(ContentCommentSerializer(instance=comment).data, status=status.HTTP_201_CREATED)
