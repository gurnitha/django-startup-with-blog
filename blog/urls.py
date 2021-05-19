# blog/urls.py
from django.urls import path
from django.conf.urls import url

from blog.views import post_list, post_detail

urlpatterns = [
    path('', post_list, name='blog_post_list'),
    # path('2021/5/flask-essentials/', post_detail, name='blog_post_detail'),
    # path('year/month/slug',post_list, name='blog_post_detail')
    url(r'^(?P<year>\d{4})/'
	        r'(?P<month>\d{1,2})/'
	        r'(?P<slug>[\w\-]+)/$',
	        post_detail,
	        name='blog_post_detail'),
]