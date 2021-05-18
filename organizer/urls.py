# organizer/urls.py
from django.urls import path
from organizer.views import (
		startup_list, startup_detail,
		tag_list, tag_detail)

urlpatterns = [

    path('startup/', 
    		startup_list,
	        name='organizer_startup_list'),

    path('startup/flask-for-beginners/', 
    		startup_detail,
			name='organizer_startup_detail'),

    path('tag/',
    		tag_list,
	        name='organizer_tag_list'),

    path('tag/django/',
    		tag_detail,
	        name='organizer_tag_detail'),

]