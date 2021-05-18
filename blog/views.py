# blog/views.py
from django.shortcuts import render

# Create your views here.

# Post List
# http://127.0.0.1:8000/blog/
def post_list(request):
	return render(request, 'blog/post_list.html')


# Post Detail: 
# http://127.0.0.1:8000/blog/2021/05/flask-essentials/
def post_detail(request):

	return render(request, 'blog/post_detail.html')  


