from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from blog.api.views import api_detail_post_view

urlpatterns = [
    path('', views.home, name="blog-homepage"),
    path('post/list', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('words_count/', views.words_count, name="words_count"),
    path('words_count/count/', views.count, name="count"),

    #RestFramework Urls
    path('', include('blog.api.urls')),

]