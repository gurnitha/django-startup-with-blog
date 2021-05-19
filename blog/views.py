# blog/views.py
from django.shortcuts import render

from blog.models import Post 

# Create your views here.

# Post List
# http://127.0.0.1:8000/blog/
def post_list(request):
	post_list = Post.objects.all()
	context = {
		'post_list': post_list
	}
	return render(request, 'blog/post_list.html', context)

# Post Detail: 
# http://127.0.0.1:8000/blog/2021/05/flask-essentials/
def post_detail(request):

	return render(request, 'blog/post_detail.html')  


