from django.shortcuts import render, get_object_or_404
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
def startup_detail(request, slug):
	startup = get_object_or_404(
			Startup,
			slug__iexact=slug 
			)
	context = {
		'startup':startup
	}
	return render(
			request,
			'organizer/startup_detail.html',
			context)


# Tag list 
def tag_list(request):
	return render(request, 'organizer/tag_list.html')


# Tag detail page
def tag_detail(request):
	return render(request, 'organizer/tag_detail.html')




