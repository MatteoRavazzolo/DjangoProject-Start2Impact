from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from users.models import Profile
from django.contrib import messages


@login_required(login_url='login')
def home(request):
	ipaddress = request.META.get('REMOTE_ADDR')
	saved_ip_address = Profile.objects.filter(user=request.user).values('ipaddress')
	for object in saved_ip_address:
		if object['ipaddress'] != ipaddress:
			Profile.objects.filter(user=request.user).update(ipaddress=ipaddress)
			messages.warning(request, f'Your IP Address it\'s different')
	
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


class PostListView(ListView):
		model = Post
		template_name = "blog/home.html"
		context_object_name= "posts"
		ordering = ["-date_posted"]


class PostDetailView(DetailView):
		model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
		model = Post
		fields = ['title', 'content']

		def form_valid(self, form):
			form.instance.author = self.request.user
			return super().form_valid(form)
		

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
		model = Post
		fields = ['title', 'content']

		def form_valid(self, form):
			form.instance.author = self.request.user
			return super().form_valid(form)

		def test_func(self):
			post = self.get_object()
			if self.request.user == post.author:
				return True
			return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
		model = Post
		success_url = '/'

		def test_func(self):
			post = self.get_object()
			if self.request.user == post.author:
				return True
			return False


@login_required(login_url='login')
def words_count(request):
	return render(request, 'blog/words_count.html')

@login_required(login_url='login')
def count(request):
	fulltext = request.GET["fulltext"]
	PostsWords = serializers.serialize("python", Post.objects.all())
	word_list={}
	for object in PostsWords:
		for word in object['fields']['content'].split():
			if word in word_list:
				word_list[word] += 1
			else:
				word_list[word] = 1
	return render(request, 'blog/count.html', {'fulltext':fulltext, 'word_list':word_list.items()})



