from blog.api.views import api_detail_post_view
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
	path('jsonresponse/', views.api_detail_post_view, name="json"),
]