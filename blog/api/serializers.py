from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):

	username = serializers.SerializerMethodField('get_username_from_author')

	class Meta:
		model = Post
		fields = ["title", "content", "date_posted", "username"]

	def get_username_from_author(self, blog_post):
		username = blog_post.author.username
		return username