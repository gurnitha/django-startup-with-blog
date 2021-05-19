from django.shortcuts import render
from organizer.models import Startup 

# Create your views here.

# Startup List
def startup_list(request):
	startups = Startup.objects.all()
	context = {
		'startups':startups
	}
	return render(request,'organizer/startup_list.html', context)


# Startup Detail
def startup_detail(request):
	return render(request,'organizer/startup_detail.html')


# Tag list 
def tag_list(request):
	return render(request, 'organizer/tag_list.html')


# Tag detail page
def tag_detail(request):
	return render(request, 'organizer/tag_detail.html')




