# blog/urls.py
from django.urls import path
from blog.views import post_list, post_detail

urlpatterns = [
    path('', post_list, name='blog_post_list'),
    path('2021/5/flask-essentials/', post_detail, name='blog_post_detail'),
]