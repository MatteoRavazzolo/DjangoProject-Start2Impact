from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from blog.api.serializers import PostSerializer
from datetime import timedelta
from django.utils import timezone


@api_view(['GET', ])
def api_detail_post_view(request):

	try:
		blog_post = Post.objects.filter(date_posted__gte=timezone.now()-timedelta(hours=1))
	except Post.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = PostSerializer(blog_post, many=True)
	return Response(serializer.data)




